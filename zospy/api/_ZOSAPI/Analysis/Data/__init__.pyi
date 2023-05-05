"""
This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from zospy.api._ZOSAPI.Analysis import IColorTranslator, IMessage
from zospy.api._ZOSAPI.Common import IMatrixData, IVectorData
from zospy.api._ZOSAPI.Tools import CriticalRayType
from zospy.api._ZOSAPI.Tools.RayTrace import RayStatus

__all__ = (
    "IAR_",
    "IAR_",
    "IAR_CriticalRayData",
    "IAR_CriticalRayData",
    "IAR_CriticalRayInfo",
    "IAR_CriticalRayInfo",
    "IAR_DataGrid",
    "IAR_DataGrid",
    "IAR_DataGridRgb",
    "IAR_DataGridRgb",
    "IAR_DataGridVector",
    "IAR_DataGridVector",
    "IAR_DataScatterPoints",
    "IAR_DataScatterPoints",
    "IAR_DataScatterPointsRgb",
    "IAR_DataScatterPointsRgb",
    "IAR_DataSeries",
    "IAR_DataSeries",
    "IAR_DataSeriesRgb",
    "IAR_DataSeriesRgb",
    "IAR_HeaderData",
    "IAR_HeaderData",
    "IAR_MetaData",
    "IAR_MetaData",
    "IAR_NSCSingleRayTraceData",
    "IAR_NSCSingleRayTraceData",
    "IAR_PathAnalysisData",
    "IAR_PathAnalysisData",
    "IAR_PathAnalysisEntry",
    "IAR_PathAnalysisEntry",
    "IAR_RayData",
    "IAR_RayData",
    "IAR_RayInfo",
    "IAR_RayInfo",
    "IAR_Rgb",
    "IAR_Rgb",
    "IAR_ScatterPoint",
    "IAR_ScatterPoint",
    "IAR_ScatterPointRgb",
    "IAR_ScatterPointRgb",
    "IAR_SpotDataResult",
    "IAR_SpotDataResult",
    "IAR_SpotDataResultMatrix",
    "IAR_SpotDataResultMatrix",
    "IAR_Vector2D",
    "IAR_Vector2D",
    "IAR_XYZ",
    "IAR_XYZ",
)

class IAR_:
    @property
    def CriticalRayData(self) -> IAR_CriticalRayData: ...
    @property
    def DataGrids(self) -> list[IAR_DataGrid]: ...
    @property
    def DataGridsRgb(self) -> list[IAR_DataGridRgb]: ...
    @property
    def DataScatterPoints(self) -> list[IAR_DataScatterPoints]: ...
    @property
    def DataScatterPointsRgb(self) -> list[IAR_DataScatterPointsRgb]: ...
    @property
    def DataSeries(self) -> list[IAR_DataSeries]: ...
    @property
    def DataSeriesRgb(self) -> list[IAR_DataSeriesRgb]: ...
    @property
    def HeaderData(self) -> IAR_HeaderData: ...
    @property
    def Messages(self) -> list[IMessage]: ...
    @property
    def MetaData(self) -> IAR_MetaData: ...
    @property
    def NSCSingleRayTraceData(self) -> IAR_NSCSingleRayTraceData: ...
    @property
    def NumberOfDataGrids(self) -> int: ...
    @property
    def NumberOfDataGridsRgb(self) -> int: ...
    @property
    def NumberOfDataScatterPoints(self) -> int: ...
    @property
    def NumberOfDataScatterPointsRgb(self) -> int: ...
    @property
    def NumberOfDataSeries(self) -> int: ...
    @property
    def NumberOfDataSeriesRgb(self) -> int: ...
    @property
    def NumberOfMessages(self) -> int: ...
    @property
    def NumberOfRayData(self) -> int: ...
    @property
    def PathAnalysisData(self) -> IAR_PathAnalysisData: ...
    @property
    def RayData(self) -> list[IAR_RayData]: ...
    @property
    def SpotData(self) -> IAR_SpotDataResultMatrix: ...
    def GetDataGrid(self, index: int) -> IAR_DataGrid: ...
    def GetDataGridRgb(self, index: int) -> IAR_DataGridRgb: ...
    def GetDataScatterPoint(self, index: int) -> IAR_DataScatterPoints: ...
    def GetDataScatterPointRgb(self, index: int) -> IAR_DataScatterPointsRgb: ...
    def GetDataSeries(self, index: int) -> IAR_DataSeries: ...
    def GetDataSeriesRgb(self, index: int) -> IAR_DataSeriesRgb: ...
    def GetMessageAt(self, index: int) -> IMessage: ...
    def GetRayData(self, index: int) -> IAR_RayData: ...
    def GetTextFile(self, Filename: str) -> bool: ...

class IAR_CriticalRayData:
    @property
    def HeaderLabels(self) -> list[str]: ...
    @property
    def NumRays(self) -> int: ...
    @property
    def Rays(self) -> list[IAR_CriticalRayInfo]: ...
    def GetRay(self, idx: int) -> IAR_CriticalRayInfo: ...

class IAR_CriticalRayInfo:
    @property
    def FieldPoint(self) -> int: ...
    @property
    def LActual(self) -> float: ...
    @property
    def LIn(self) -> float: ...
    @property
    def LTarget(self) -> float: ...
    @property
    def MActual(self) -> float: ...
    @property
    def MIn(self) -> float: ...
    @property
    def MTarget(self) -> float: ...
    @property
    def NActual(self) -> float: ...
    @property
    def NIn(self) -> float: ...
    @property
    def NTarget(self) -> float: ...
    @property
    def Pass(self) -> bool: ...
    @property
    def RayType(self) -> CriticalRayType: ...
    @property
    def TerminationObject(self) -> int: ...
    @property
    def Wavelength(self) -> float: ...
    @property
    def XActual(self) -> float: ...
    @property
    def XIn(self) -> float: ...
    @property
    def XTarget(self) -> float: ...
    @property
    def YActual(self) -> float: ...
    @property
    def YIn(self) -> float: ...
    @property
    def YTarget(self) -> float: ...
    @property
    def ZActual(self) -> float: ...
    @property
    def ZIn(self) -> float: ...
    @property
    def ZTarget(self) -> float: ...

class IAR_DataGrid:
    def ConvertToRGB(self, translator: IColorTranslator) -> IAR_DataGridRgb: ...
    @property
    def Description(self) -> str: ...
    @property
    def Dx(self) -> float: ...
    @property
    def Dy(self) -> float: ...
    @property
    def MinX(self) -> float: ...
    @property
    def MinY(self) -> float: ...
    @property
    def Nx(self) -> int: ...
    @property
    def Ny(self) -> int: ...
    @property
    def ValueData(self) -> IMatrixData: ...
    @property
    def ValueLabel(self) -> str: ...
    @property
    def Values(self) -> list[list[float]]: ...
    @property
    def XLabel(self) -> str: ...
    @property
    def YLabel(self) -> str: ...
    def X(self, rowX: int) -> float: ...
    def XYZ(self, rowX: int, colY: int) -> IAR_XYZ: ...
    def Y(self, colY: int) -> float: ...
    def Z(self, rowX: int, colY: int) -> float: ...

class IAR_DataGridRgb:
    def FillValues(self, fullSize: int) -> tuple[list[float], list[float], list[float]]: ...
    @property
    def Description(self) -> str: ...
    @property
    def Dx(self) -> float: ...
    @property
    def Dy(self) -> float: ...
    @property
    def MinX(self) -> float: ...
    @property
    def MinY(self) -> float: ...
    @property
    def Nx(self) -> int: ...
    @property
    def Ny(self) -> int: ...
    @property
    def ValueLabel(self) -> str: ...
    @property
    def Values(self) -> list[list[IAR_Rgb]]: ...
    @property
    def XLabel(self) -> str: ...
    @property
    def YLabel(self) -> str: ...
    def GetValue(self, x: int, y: int) -> IAR_Rgb: ...

class IAR_DataGridVector:
    def DeltaX(self, rowX: int, colY: int) -> float: ...
    def DeltaY(self, rowX: int, colY: int) -> float: ...
    @property
    def DeltaXValueData(self) -> IMatrixData: ...
    @property
    def DeltaXValues(self) -> list[list[float]]: ...
    @property
    def DeltaYValueData(self) -> IMatrixData: ...
    @property
    def DeltaYValues(self) -> list[list[float]]: ...
    @property
    def Description(self) -> str: ...
    @property
    def Dx(self) -> float: ...
    @property
    def Dy(self) -> float: ...
    @property
    def MinX(self) -> float: ...
    @property
    def MinY(self) -> float: ...
    @property
    def Nx(self) -> int: ...
    @property
    def Ny(self) -> int: ...
    @property
    def ValueLabel(self) -> str: ...
    @property
    def XLabel(self) -> str: ...
    @property
    def YLabel(self) -> str: ...
    def X(self, rowX: int) -> float: ...
    def Y(self, colY: int) -> float: ...

class IAR_DataScatterPoints:
    def ConvertToRGB(self, translator: IColorTranslator) -> IAR_DataScatterPointsRgb: ...
    def FillPointValues(self, fullSize: int) -> tuple[list[float], list[float], list[float]]: ...
    @property
    def Description(self) -> str: ...
    @property
    def NumPoints(self) -> int: ...
    @property
    def Points(self) -> list[IAR_ScatterPoint]: ...
    @property
    def ValueLabel(self) -> str: ...
    @property
    def XLabel(self) -> str: ...
    @property
    def YLabel(self) -> str: ...
    def GetPoint(self, idx: int) -> IAR_ScatterPoint: ...

class IAR_DataScatterPointsRgb:
    def FillPointValues(
        self, fullSize: int
    ) -> tuple[list[float], list[float], list[float], list[float], list[float]]: ...
    @property
    def Description(self) -> str: ...
    @property
    def NumPoints(self) -> int: ...
    @property
    def Points(self) -> list[IAR_ScatterPointRgb]: ...
    @property
    def ValueLabel(self) -> str: ...
    @property
    def XLabel(self) -> str: ...
    @property
    def YLabel(self) -> str: ...
    def GetPoint(self, idx: int) -> IAR_ScatterPointRgb: ...

class IAR_DataSeries:
    def ConvertToRGB(self, translator: IColorTranslator) -> IAR_DataSeriesRgb: ...
    @property
    def Description(self) -> str: ...
    @property
    def NumSeries(self) -> int: ...
    @property
    def SeriesLabels(self) -> list[str]: ...
    @property
    def XData(self) -> IVectorData: ...
    @property
    def XLabel(self) -> str: ...
    @property
    def YData(self) -> IMatrixData: ...

class IAR_DataSeriesRgb:
    def FillYValues(self, fullSize: int) -> tuple[list[float], list[float], list[float]]: ...
    @property
    def Description(self) -> str: ...
    @property
    def NumberOfRows(self) -> int: ...
    @property
    def NumSeries(self) -> int: ...
    @property
    def SeriesLabels(self) -> list[str]: ...
    @property
    def XData(self) -> IVectorData: ...
    @property
    def XLabel(self) -> str: ...
    @property
    def YVals(self) -> list[list[IAR_Rgb]]: ...
    def GetYPoint(self, row: int, col: int) -> IAR_Rgb: ...

class IAR_HeaderData:
    @property
    def Lines(self) -> list[str]: ...

class IAR_MetaData:
    @property
    def Date(self) -> DateTime: ...
    @property
    def FeatureDescription(self) -> str: ...
    @property
    def LensFile(self) -> str: ...
    @property
    def LensTitle(self) -> str: ...

class IAR_NSCSingleRayTraceData:
    @property
    def IsValid(self) -> bool: ...
    @property
    def NumberOfSegments(self) -> int: ...
    @property
    def WaveIndex(self) -> int: ...
    @property
    def WavelengthUM(self) -> float: ...
    @property
    def ZRDFile(self) -> str: ...
    def ReadSegmentFull(
        self, segmentNumber: int
    ) -> tuple[
        bool,
        int,
        int,
        int,
        int,
        int,
        RayStatus,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        int,
        int,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ]: ...

class IAR_PathAnalysisData:
    @property
    def NumPaths(self) -> int: ...
    @property
    def Paths(self) -> list[IAR_PathAnalysisEntry]: ...
    @property
    def TotalFluxIn(self) -> float: ...
    @property
    def TotalFluxOut(self) -> float: ...
    @property
    def TotalHits(self) -> int: ...
    @property
    def TotalRays(self) -> int: ...
    def GetPathNumber(self, idx: int) -> IAR_PathAnalysisEntry: ...

class IAR_PathAnalysisEntry:
    @property
    def GhostsInPath(self) -> int: ...
    @property
    def HitsInPath(self) -> int: ...
    @property
    def NumberOfObjectsInPath(self) -> int: ...
    @property
    def PathNumber(self) -> int: ...
    @property
    def PathObjectList(self) -> list[int]: ...
    @property
    def PathSource(self) -> int: ...
    @property
    def RaysInPath(self) -> int: ...
    @property
    def TotalPathFlux(self) -> float: ...
    @property
    def UniqueObjectsInPath(self) -> int: ...
    def GetPathObjectNumber(self, objectNumber: int) -> int: ...

class IAR_RayData:
    @property
    def Description(self) -> str: ...
    @property
    def NumRays(self) -> int: ...
    @property
    def Rays(self) -> list[IAR_RayInfo]: ...
    def GetRay(self, idx: int) -> IAR_RayInfo: ...

class IAR_RayInfo:
    @property
    def Error(self) -> int: ...
    @property
    def Ex(self) -> float: ...
    @property
    def Ey(self) -> float: ...
    @property
    def Ez(self) -> float: ...
    @property
    def Hit_face(self) -> int: ...
    @property
    def Hit_object(self) -> int: ...
    @property
    def In_object(self) -> int: ...
    @property
    def L(self) -> float: ...
    @property
    def Level(self) -> int: ...
    @property
    def M(self) -> float: ...
    @property
    def N(self) -> float: ...
    @property
    def Nx(self) -> float: ...
    @property
    def Ny(self) -> float: ...
    @property
    def Nz(self) -> float: ...
    @property
    def OpticalPathLength(self) -> float: ...
    @property
    def Parent(self) -> int: ...
    @property
    def PathLength(self) -> float: ...
    @property
    def RayIndex(self) -> int: ...
    @property
    def Segment(self) -> int: ...
    @property
    def Vignetted(self) -> int: ...
    @property
    def Wavelength(self) -> float: ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...
    @property
    def Z(self) -> float: ...

class IAR_Rgb:
    @property
    def B(self) -> float: ...
    @property
    def G(self) -> float: ...
    @property
    def R(self) -> float: ...

class IAR_ScatterPoint:
    @property
    def Value(self) -> float: ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...

class IAR_ScatterPointRgb:
    @property
    def Value(self) -> IAR_Rgb: ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...

class IAR_SpotDataResult:
    @property
    def Detector_X(self) -> float: ...
    @property
    def Detector_Y(self) -> float: ...
    @property
    def Detector_Z(self) -> float: ...
    @property
    def GeoSpotSize(self) -> float: ...
    @property
    def L(self) -> float: ...
    @property
    def M(self) -> float: ...
    @property
    def N(self) -> float: ...
    @property
    def RefCoord_X(self) -> float: ...
    @property
    def RefCoord_Y(self) -> float: ...
    @property
    def RMSSpot_X(self) -> float: ...
    @property
    def RMSSpot_Y(self) -> float: ...
    @property
    def RMSSpotSize(self) -> float: ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...
    @property
    def Z(self) -> float: ...
    @Detector_X.setter
    def Detector_X(self, value: float) -> None: ...
    @Detector_Y.setter
    def Detector_Y(self, value: float) -> None: ...
    @Detector_Z.setter
    def Detector_Z(self, value: float) -> None: ...
    @GeoSpotSize.setter
    def GeoSpotSize(self, value: float) -> None: ...
    @L.setter
    def L(self, value: float) -> None: ...
    @M.setter
    def M(self, value: float) -> None: ...
    @N.setter
    def N(self, value: float) -> None: ...
    @RefCoord_X.setter
    def RefCoord_X(self, value: float) -> None: ...
    @RefCoord_Y.setter
    def RefCoord_Y(self, value: float) -> None: ...
    @RMSSpot_X.setter
    def RMSSpot_X(self, value: float) -> None: ...
    @RMSSpot_Y.setter
    def RMSSpot_Y(self, value: float) -> None: ...
    @RMSSpotSize.setter
    def RMSSpotSize(self, value: float) -> None: ...
    @X.setter
    def X(self, value: float) -> None: ...
    @Y.setter
    def Y(self, value: float) -> None: ...
    @Z.setter
    def Z(self, value: float) -> None: ...

class IAR_SpotDataResultMatrix:
    @property
    def HalfWidth_X(self) -> float: ...
    @property
    def HalfWidth_Y(self) -> float: ...
    def Get_L_For(self, fieldN: int, waveN: int) -> float: ...
    def Get_M_For(self, fieldN: int, waveN: int) -> float: ...
    @property
    def MaxRadius(self) -> float: ...
    @property
    def MeanRadius(self) -> float: ...
    def Get_N_For(self, fieldN: int, waveN: int) -> float: ...
    @property
    def NumberOfFields(self) -> int: ...
    @property
    def NumberOfWavelengths(self) -> int: ...
    def Get_X_For(self, fieldN: int, waveN: int) -> float: ...
    def Get_Y_For(self, fieldN: int, waveN: int) -> float: ...
    def Get_Z_For(self, fieldN: int, waveN: int) -> float: ...
    def GetDetector_X_For(self, fieldN: int, waveN: int) -> float: ...
    def GetDetector_Y_For(self, fieldN: int, waveN: int) -> float: ...
    def GetDetector_Z_For(self, fieldN: int, waveN: int) -> float: ...
    def GetGeoSpotSizeFor(self, fieldN: int, waveN: int) -> float: ...
    def GetReferenceCoordinate_X_For(self, fieldN: int, waveN: int) -> float: ...
    def GetReferenceCoordinate_Y_For(self, fieldN: int, waveN: int) -> float: ...
    def GetRMSSpot_X_For(self, fieldN: int, waveN: int) -> float: ...
    def GetRMSSpot_Y_For(self, fieldN: int, waveN: int) -> float: ...
    def GetRMSSpotSizeFor(self, fieldN: int, waveN: int) -> float: ...

class IAR_Vector2D:
    @property
    def dx(self) -> float: ...
    @property
    def dy(self) -> float: ...

class IAR_XYZ:
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...
    @property
    def Z(self) -> float: ...
