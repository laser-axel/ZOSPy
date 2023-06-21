"""
This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from zospy.api._ZOSAPI.Analysis import (
    DetectorViewerShowAsTypes,
    DetectorViewerShowDataTypes,
)
from zospy.api._ZOSAPI.Analysis.Settings import (
    IAS_,
    DetectorViewerScaleTypes,
    IAS_Detector,
    IAS_Surface,
    IAS_Wavelength,
)

__all__ = ("IAS_DetectorViewer", "IAS_NSCSingleRayTrace")

class IAS_DetectorViewer(IAS_):
    @property
    def AngleList(self) -> list[UInt16]: ...
    @property
    def Configuration(self) -> int: ...
    @property
    def Contrast(self) -> UInt16: ...
    @property
    def DataType(self) -> DetectorViewerShowDataTypes: ...
    @property
    def Detector(self) -> IAS_Detector: ...
    @property
    def ExtraProperty(self) -> int: ...
    @property
    def Filter(self) -> str: ...
    @property
    def MaxSpatialFrequency(self) -> float: ...
    @property
    def NumberOfDetectorsOnSurface(self) -> int: ...
    @property
    def NumberOfNonSequentialSurfaces(self) -> int: ...
    @property
    def NumberOfShowAsTypes(self) -> int: ...
    @property
    def OutFile(self) -> str: ...
    @property
    def PlotScaleMaximum(self) -> float: ...
    @property
    def PlotScaleMinimum(self) -> float: ...
    @property
    def RayDatabaseFilename(self) -> str: ...
    @property
    def RowCol(self) -> int: ...
    @property
    def Scale(self) -> DetectorViewerScaleTypes: ...
    @property
    def ShowAs(self) -> DetectorViewerShowAsTypes: ...
    @property
    def Smoothing(self) -> int: ...
    @property
    def SuppressFrame(self) -> bool: ...
    @property
    def Surface(self) -> IAS_Surface: ...
    @property
    def SymbolType(self) -> int: ...
    @property
    def Zplane(self) -> int: ...
    def GetDetectorName(self, index: int) -> str: ...
    def GetDetectorObjectNumber(self, index: int) -> int: ...
    def GetNonSequentialSurfaceName(self, index: int) -> str: ...
    def GetNonSequentialSurfaceNumber(self, index: int) -> int: ...
    def GetShowAsTypeNameAt(self, idx: int) -> str: ...
    def IsValidDetector(self, N: int) -> bool: ...
    @AngleList.setter
    def AngleList(self, value: list[UInt16]) -> None: ...
    @Configuration.setter
    def Configuration(self, value: int) -> None: ...
    @Contrast.setter
    def Contrast(self, value: UInt16) -> None: ...
    @DataType.setter
    def DataType(self, value: DetectorViewerShowDataTypes) -> None: ...
    @ExtraProperty.setter
    def ExtraProperty(self, value: int) -> None: ...
    @Filter.setter
    def Filter(self, value: str) -> None: ...
    @MaxSpatialFrequency.setter
    def MaxSpatialFrequency(self, value: float) -> None: ...
    @OutFile.setter
    def OutFile(self, value: str) -> None: ...
    @PlotScaleMaximum.setter
    def PlotScaleMaximum(self, value: float) -> None: ...
    @PlotScaleMinimum.setter
    def PlotScaleMinimum(self, value: float) -> None: ...
    @RayDatabaseFilename.setter
    def RayDatabaseFilename(self, value: str) -> None: ...
    @RowCol.setter
    def RowCol(self, value: int) -> None: ...
    @Scale.setter
    def Scale(self, value: DetectorViewerScaleTypes) -> None: ...
    @ShowAs.setter
    def ShowAs(self, value: DetectorViewerShowAsTypes) -> None: ...
    @Smoothing.setter
    def Smoothing(self, value: int) -> None: ...
    @SuppressFrame.setter
    def SuppressFrame(self, value: bool) -> None: ...
    @SymbolType.setter
    def SymbolType(self, value: int) -> None: ...
    @Zplane.setter
    def Zplane(self, value: int) -> None: ...

class IAS_NSCSingleRayTrace(IAS_):
    @property
    def DecimalPrecision(self) -> int: ...
    @property
    def ExpandIntoBranches(self) -> bool: ...
    @property
    def RaySourceL(self) -> float: ...
    @property
    def RaySourceM(self) -> float: ...
    @property
    def RaySourceN(self) -> float: ...
    @property
    def RaySourceX(self) -> float: ...
    @property
    def RaySourceY(self) -> float: ...
    @property
    def RaySourceZ(self) -> float: ...
    @property
    def RefObject(self) -> int: ...
    @property
    def SaveRaysFile(self) -> str: ...
    @property
    def ScatterNSCRays(self) -> bool: ...
    @property
    def ShowExyz(self) -> bool: ...
    @property
    def ShowLMN(self) -> bool: ...
    @property
    def ShowNormal(self) -> bool: ...
    @property
    def ShowPath(self) -> bool: ...
    @property
    def ShowXYZ(self) -> bool: ...
    @property
    def SplitNSCRays(self) -> bool: ...
    @property
    def UsePolarization(self) -> bool: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @DecimalPrecision.setter
    def DecimalPrecision(self, value: int) -> None: ...
    @ExpandIntoBranches.setter
    def ExpandIntoBranches(self, value: bool) -> None: ...
    @RaySourceL.setter
    def RaySourceL(self, value: float) -> None: ...
    @RaySourceM.setter
    def RaySourceM(self, value: float) -> None: ...
    @RaySourceN.setter
    def RaySourceN(self, value: float) -> None: ...
    @RaySourceX.setter
    def RaySourceX(self, value: float) -> None: ...
    @RaySourceY.setter
    def RaySourceY(self, value: float) -> None: ...
    @RaySourceZ.setter
    def RaySourceZ(self, value: float) -> None: ...
    @RefObject.setter
    def RefObject(self, value: int) -> None: ...
    @SaveRaysFile.setter
    def SaveRaysFile(self, value: str) -> None: ...
    @ScatterNSCRays.setter
    def ScatterNSCRays(self, value: bool) -> None: ...
    @ShowExyz.setter
    def ShowExyz(self, value: bool) -> None: ...
    @ShowLMN.setter
    def ShowLMN(self, value: bool) -> None: ...
    @ShowNormal.setter
    def ShowNormal(self, value: bool) -> None: ...
    @ShowPath.setter
    def ShowPath(self, value: bool) -> None: ...
    @ShowXYZ.setter
    def ShowXYZ(self, value: bool) -> None: ...
    @SplitNSCRays.setter
    def SplitNSCRays(self, value: bool) -> None: ...
    @UsePolarization.setter
    def UsePolarization(self, value: bool) -> None: ...