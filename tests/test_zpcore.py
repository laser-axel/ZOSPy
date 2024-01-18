import locale
from pathlib import Path
from types import SimpleNamespace

import pytest

import zospy as zp
from zospy import constants


def patch_zos(zos: zp.ZOS, monkeypatch: pytest.MonkeyPatch):
    patch_application = SimpleNamespace(IsValidLicenseForAPI=False)
    patch_connection = SimpleNamespace(
        IsAlive=False, ConnectAsExtension=lambda n: patch_application, CreateNewApplication=lambda: patch_application
    )

    def patch_assign_connection(self: zp.ZOS):
        self.Connection = patch_connection

    # Patch ZOS class so ZOS.Application.IsValidLicenseForAPI is False
    monkeypatch.setattr(zos, "_assign_connection", patch_assign_connection.__get__(zos, zp.ZOS))
    # All attributes need to be patched explicitly, otherwise they won't be restored
    monkeypatch.setattr(zos, "Application", patch_application)
    monkeypatch.setattr(zos, "Connection", patch_connection)


def test_connect_without_valid_license_raises_exception(zos, connection_mode, monkeypatch):
    patch_zos(zos, monkeypatch)

    with pytest.raises(ConnectionRefusedError):
        zos.connect(connection_mode)


def test_load_zos_dlls_with_nethelper_and_opticstudio_directory_raises_valueerror(zos):
    with pytest.raises(ValueError):
        zos._load_zos_dlls(zosapi_nethelper="dummy/path", opticstudio_directory="dummy/path")


@pytest.mark.must_pass
def test_can_connect(oss):
    assert oss._System is not None


def test_can_disconnect(zos, oss):
    assert zos.Application is not None  # The Application object should be available

    zos.disconnect()

    assert zos.Application is None


@pytest.mark.require_mode("extension")
def test_get_primary_system_populates_openfile(zos, oss):
    assert oss._OpenFile == oss.SystemFile


@pytest.mark.must_pass
def test_create_simple_system(simple_system):
    assert simple_system.LDE.NumberOfSurfaces == 5


def test_version(optic_studio_version):
    assert optic_studio_version


def test_new(simple_system):
    # Replace with a new system
    simple_system.new()

    assert simple_system.LDE.NumberOfSurfaces == 3


XFAIL_ZOS_REASON = "The .zos file format is only supported by OpticStudio 21.3 and higher"


@pytest.mark.parametrize(
    "filename",
    [
        "simple_system.zmx",
        pytest.param(
            "simple_system.zos", marks=pytest.mark.xfail_for_opticstudio_versions(["<21.3.0"], XFAIL_ZOS_REASON)
        ),
    ],
)
class TestLoad:
    @pytest.fixture
    def demo_systems_folder(self, request) -> Path:
        return request.config.rootpath / "tests/data/optical_systems"

    def test_load(self, oss, demo_systems_folder, filename):
        path = (demo_systems_folder / filename).resolve()

        oss.load(path)

        assert oss.LDE.NumberOfSurfaces == 5
        assert oss.LDE.GetSurfaceAt(2).Radius == 20.0

    def test_load_relative(self, oss, demo_systems_folder, filename, monkeypatch):
        monkeypatch.chdir(demo_systems_folder)

        oss.load(filename)

        assert oss.LDE.NumberOfSurfaces == 5
        assert oss.LDE.GetSurfaceAt(2).Radius == 20.0


@pytest.mark.parametrize(
    "filename",
    [
        "TEST.ZMX",
        pytest.param("TEST.ZOS", marks=pytest.mark.xfail_for_opticstudio_versions(["<21.3.0"], XFAIL_ZOS_REASON)),
    ],
)
class TestSaveAs:
    def test_save_as(self, simple_system, tmp_path, filename):
        save_path = tmp_path / filename

        simple_system.save_as(save_path.resolve())

        assert save_path.exists()

    def test_save_as_relative_path(self, simple_system, tmp_path, filename, monkeypatch):
        monkeypatch.chdir(tmp_path)

        save_path = tmp_path / filename

        simple_system.save_as(filename)

        assert save_path.exists()


def test_get_system(zos, oss, connection_mode):
    system = zos.get_system(0)

    assert system._System is not None
    assert system.SystemID == oss.SystemID


@pytest.mark.require_mode("standalone")
def test_create_new_system(zos, oss, connection_mode):
    new_system = zos.create_new_system()

    assert zos.Application.NumberOfOpticalSystems == 2
    assert oss.SystemID != new_system.SystemID


@pytest.mark.require_mode("extension")
def test_create_new_system_raises_valueerror(zos, simple_system, connection_mode):
    with pytest.raises(ValueError):
        zos.create_new_system()


@pytest.fixture()
@pytest.mark.require_mode("standalone")
def oss_with_modifiable_config(zos: zp.ZOS, connection_mode, tmp_path) -> zp.zpcore.OpticStudioSystem:
    config_file = tmp_path / "opticstudio_config_file.CFG"
    zos.Connection.PreferencesFile = str(config_file)

    oss = zos.connect(connection_mode)

    yield oss

    # Close the system
    if oss is not None:
        zos.Application.CloseApplication()


@pytest.mark.require_mode("standalone")
class TestTxtFileEncoding:
    @pytest.mark.parametrize(
        "txtfile_encoding,expected_encoding", [("Unicode", "UTF-16-le"), ("ANSI", "LocalePreferredEncoding")]
    )
    def test_get_txtfile_encoding_returns_correct_result(
        self, oss_with_modifiable_config, txtfile_encoding, expected_encoding, monkeypatch: pytest.MonkeyPatch
    ):
        def getpreferredencoding(**kwargs):
            return "LocalePreferredEncoding"

        monkeypatch.setattr(locale, "getpreferredencoding", getpreferredencoding)

        oss_with_modifiable_config._ZOS.Application.Preferences.General.TXTFileEncoding = getattr(
            constants.Preferences.EncodingType, txtfile_encoding
        )

        returned_encoding = oss_with_modifiable_config._ZOS.get_txtfile_encoding()

        assert returned_encoding == expected_encoding

    @pytest.mark.parametrize("txtfile_encoding", ["Unicode", "ANSI"])
    def test_analysis_result_parsed_with_correct_encoding(self, oss_with_modifiable_config, txtfile_encoding, tmp_path):
        oss_with_modifiable_config._ZOS.Application.Preferences.General.TXTFileEncoding = getattr(
            constants.Preferences.EncodingType, txtfile_encoding
        )

        analysis = zp.analyses.base.new_analysis(
            oss_with_modifiable_config, zp.constants.Analysis.AnalysisIDM.SystemData
        )
        analysis.ApplyAndWaitForCompletion()
        txtoutfile = str(tmp_path / "test_analysis_result_parsed_with_correct_encoding.txt")
        analysis.Results.GetTextFile(txtoutfile)

        with open(txtoutfile, "r", encoding=oss_with_modifiable_config._ZOS.get_txtfile_encoding()) as txtfile:
            assert "System/Prescription Data" in txtfile.readline()
