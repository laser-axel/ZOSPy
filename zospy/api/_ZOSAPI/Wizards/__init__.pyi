"""This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from typing import Iterable, overload

__all__ = (
    "CriterionTypes",
    "DefaultAndDegrees",
    "DefaultAndFringes",
    "IImageData",
    "INSCBitmapWizard",
    "INSCOptimizationWizard",
    "INSCRoadwayLightingWizard",
    "INSCToleranceWizard",
    "INSCWizard",
    "ISEQOptimizationWizard",
    "ISEQOptimizationWizard2",
    "ISEQToleranceWizard",
    "IToleranceWizard",
    "IWizard",
    "OptimizationTypes",
    "PupilArmsCount",
    "ReferenceTypes",
    "ToleranceGrade",
    "ToleranceVendor",
    "WizardType",
)

class CriterionTypes:
    Wavefront = 0
    Contrast = 1
    Spot = 2
    Angular = 3

class DefaultAndDegrees:
    Default = 0
    Degrees = 1

class DefaultAndFringes:
    Default = 0
    Fringes = 1
    Percent = 2

class IImageData:
    @property
    def ImageName(self) -> str: ...
    @property
    def Width(self) -> int: ...
    @property
    def Height(self) -> int: ...
    @property
    def BitsPerPixel(self) -> int: ...
    @property
    def Channels(self) -> int: ...
    @property
    def Stride(self) -> int: ...
    @property
    def IsRGB(self) -> bool: ...
    def GetPixels(self) -> list[int]: ...
    def GetPixelsSafe(self, totalSize: int, height: int, width: int) -> tuple[list[int]]: ...
    def GetRawData(self) -> list[int]: ...
    def GetRawDataSafe(self, totalSize: int, height: int, width: int) -> tuple[list[int]]: ...

class INSCBitmapWizard(INSCWizard, IWizard):
    @property
    def NSCSettings(self) -> INSCWizard: ...
    @property
    def CommonSettings(self) -> IWizard: ...
    @property
    def NumberOfBitmapFiles(self) -> int: ...
    def GetBitmapFileAt(self, idx: int) -> str: ...
    def GetPreviewImage(self) -> IImageData: ...

class INSCOptimizationWizard(INSCWizard, IWizard):
    @property
    def NSCSettings(self) -> INSCWizard: ...
    @property
    def CommonSettings(self) -> IWizard: ...

class INSCRoadwayLightingWizard(IWizard):
    @property
    def CommonSettings(self) -> IWizard: ...
    @property
    def IsNSCRoadwayLightingWizard(self) -> bool: ...
    @property
    def IsSplitRaysUsed(self) -> bool: ...
    @IsSplitRaysUsed.setter
    def IsSplitRaysUsed(self, value: bool) -> None: ...
    @property
    def IsScatterRaysUsed(self) -> bool: ...
    @IsScatterRaysUsed.setter
    def IsScatterRaysUsed(self, value: bool) -> None: ...
    @property
    def IsUsePolarizationUsed(self) -> bool: ...
    @IsUsePolarizationUsed.setter
    def IsUsePolarizationUsed(self, value: bool) -> None: ...
    @property
    def IsIgnoreErrorsUsed(self) -> bool: ...
    @IsIgnoreErrorsUsed.setter
    def IsIgnoreErrorsUsed(self, value: bool) -> None: ...
    @property
    def Arrangement(self) -> int: ...
    @Arrangement.setter
    def Arrangement(self, value: int) -> None: ...
    @property
    def Origin(self) -> int: ...
    @Origin.setter
    def Origin(self, value: int) -> None: ...
    @property
    def NumberOfLanes(self) -> int: ...
    @NumberOfLanes.setter
    def NumberOfLanes(self, value: int) -> None: ...
    @property
    def SurfaceClassification(self) -> int: ...
    @SurfaceClassification.setter
    def SurfaceClassification(self, value: int) -> None: ...
    @property
    def RoadClass(self) -> int: ...
    @RoadClass.setter
    def RoadClass(self, value: int) -> None: ...
    @property
    def StartAt(self) -> int: ...
    @StartAt.setter
    def StartAt(self, value: int) -> None: ...
    @property
    def Configuration(self) -> int: ...
    @Configuration.setter
    def Configuration(self, value: int) -> None: ...
    @property
    def MountingHeight(self) -> float: ...
    @MountingHeight.setter
    def MountingHeight(self, value: float) -> None: ...
    @property
    def LongitudinalSpacing(self) -> float: ...
    @LongitudinalSpacing.setter
    def LongitudinalSpacing(self, value: float) -> None: ...
    @property
    def LateralOffset(self) -> float: ...
    @LateralOffset.setter
    def LateralOffset(self, value: float) -> None: ...
    @property
    def LaneWidth(self) -> float: ...
    @LaneWidth.setter
    def LaneWidth(self, value: float) -> None: ...
    @property
    def OverallWeight(self) -> float: ...
    @OverallWeight.setter
    def OverallWeight(self, value: float) -> None: ...
    @property
    def NumberOfOrigins(self) -> int: ...
    @property
    def NumberOfConfigurations(self) -> int: ...
    @property
    def NumberOfArrangements(self) -> int: ...
    @property
    def NumberOfClassifications(self) -> int: ...
    @property
    def NumberOfRoadClasses(self) -> int: ...
    def GetArrangementAt(self, idx: int) -> str: ...
    def GetClassificationAt(self, idx: int) -> str: ...
    def GetConfigurationAt(self, idx: int) -> str: ...
    def GetOriginAt(self, idx: int) -> str: ...
    def GetRoadClassAt(self, idx: int) -> str: ...

class INSCToleranceWizard(IToleranceWizard, IWizard):
    @property
    def ToleranceSettings(self) -> IToleranceWizard: ...

class INSCWizard(IWizard):
    @property
    def IsNSCOptimizingWizard(self) -> bool: ...
    @property
    def IsNSCBitmapWizard(self) -> bool: ...
    @property
    def IsClearDataSettingsUsed(self) -> bool: ...
    @IsClearDataSettingsUsed.setter
    def IsClearDataSettingsUsed(self, value: bool) -> None: ...
    @property
    def IsRaytraceSettingsUsed(self) -> bool: ...
    @IsRaytraceSettingsUsed.setter
    def IsRaytraceSettingsUsed(self, value: bool) -> None: ...
    @property
    def IsSplitRaysUsed(self) -> bool: ...
    @IsSplitRaysUsed.setter
    def IsSplitRaysUsed(self, value: bool) -> None: ...
    @property
    def IsUsePolarizationUsed(self) -> bool: ...
    @IsUsePolarizationUsed.setter
    def IsUsePolarizationUsed(self, value: bool) -> None: ...
    @property
    def IsScatterRaysUsed(self) -> bool: ...
    @IsScatterRaysUsed.setter
    def IsScatterRaysUsed(self, value: bool) -> None: ...
    @property
    def IsIgnoreErrorsUsed(self) -> bool: ...
    @IsIgnoreErrorsUsed.setter
    def IsIgnoreErrorsUsed(self, value: bool) -> None: ...
    @property
    def IsUseLightningTraceUsed(self) -> bool: ...
    @IsUseLightningTraceUsed.setter
    def IsUseLightningTraceUsed(self, value: bool) -> None: ...
    @property
    def IsCriterionSettingsUsed(self) -> bool: ...
    @IsCriterionSettingsUsed.setter
    def IsCriterionSettingsUsed(self, value: bool) -> None: ...
    @property
    def IsMinimumFluxUsed(self) -> bool: ...
    @IsMinimumFluxUsed.setter
    def IsMinimumFluxUsed(self, value: bool) -> None: ...
    @property
    def IsOverwriteUsed(self) -> bool: ...
    @IsOverwriteUsed.setter
    def IsOverwriteUsed(self, value: bool) -> None: ...
    @property
    def IsTargetSettingsUsed(self) -> bool: ...
    @IsTargetSettingsUsed.setter
    def IsTargetSettingsUsed(self, value: bool) -> None: ...
    @property
    def IsColorTargetsUsed(self) -> bool: ...
    @IsColorTargetsUsed.setter
    def IsColorTargetsUsed(self, value: bool) -> None: ...
    @property
    def IsResampleDetectorUsed(self) -> bool: ...
    @IsResampleDetectorUsed.setter
    def IsResampleDetectorUsed(self, value: bool) -> None: ...
    @property
    def ClearDetector(self) -> int: ...
    @ClearDetector.setter
    def ClearDetector(self, value: int) -> None: ...
    @property
    def Criterion(self) -> int: ...
    @Criterion.setter
    def Criterion(self, value: int) -> None: ...
    @property
    def UseSource(self) -> int: ...
    @UseSource.setter
    def UseSource(self, value: int) -> None: ...
    @property
    def UseDetector(self) -> int: ...
    @UseDetector.setter
    def UseDetector(self, value: int) -> None: ...
    @property
    def Boundary(self) -> int: ...
    @Boundary.setter
    def Boundary(self, value: int) -> None: ...
    @property
    def StartAt(self) -> int: ...
    @StartAt.setter
    def StartAt(self, value: int) -> None: ...
    @property
    def Configuration(self) -> int: ...
    @Configuration.setter
    def Configuration(self, value: int) -> None: ...
    @property
    def BitmapFile(self) -> int: ...
    @BitmapFile.setter
    def BitmapFile(self, value: int) -> None: ...
    @property
    def RaySampling(self) -> int: ...
    @RaySampling.setter
    def RaySampling(self, value: int) -> None: ...
    @property
    def EdgeSampling(self) -> int: ...
    @EdgeSampling.setter
    def EdgeSampling(self, value: int) -> None: ...
    @property
    def Target(self) -> float: ...
    @Target.setter
    def Target(self, value: float) -> None: ...
    @property
    def MinimumFlux(self) -> float: ...
    @MinimumFlux.setter
    def MinimumFlux(self, value: float) -> None: ...
    @property
    def OverallWeight(self) -> float: ...
    @OverallWeight.setter
    def OverallWeight(self, value: float) -> None: ...
    @property
    def TotalFlux(self) -> float: ...
    @TotalFlux.setter
    def TotalFlux(self, value: float) -> None: ...
    @property
    def NumberOfSources(self) -> int: ...
    @property
    def NumberOfDetectors(self) -> int: ...
    @property
    def NumberOfCriterion(self) -> int: ...
    @property
    def NumberOfConfigurations(self) -> int: ...
    @property
    def NumberOfRaySamplings(self) -> int: ...
    @property
    def NumberOfEdgeSamplings(self) -> int: ...
    @property
    def NumberOfBoundaries(self) -> int: ...
    def GetBoundaryAt(self, idx: int) -> str: ...
    def GetConfigurationAt(self, idx: int) -> str: ...
    def GetCriterionAt(self, idx: int) -> str: ...
    def GetDetectorAt(self, idx: int) -> str: ...
    def GetEdgeSamplingAt(self, idx: int) -> str: ...
    def GetRaySamplingAt(self, idx: int) -> str: ...
    def GetSourceAt(self, idx: int) -> str: ...

class ISEQOptimizationWizard(IWizard):
    @property
    def CommonSettings(self) -> IWizard: ...
    @property
    def IsSEQOptimizationWizard(self) -> bool: ...
    @property
    def IsDeleteVignetteUsed(self) -> bool: ...
    @IsDeleteVignetteUsed.setter
    def IsDeleteVignetteUsed(self, value: bool) -> None: ...
    @property
    def IsGlassUsed(self) -> bool: ...
    @IsGlassUsed.setter
    def IsGlassUsed(self, value: bool) -> None: ...
    @property
    def IsAirUsed(self) -> bool: ...
    @IsAirUsed.setter
    def IsAirUsed(self, value: bool) -> None: ...
    @property
    def IsAssumeAxialSymmetryUsed(self) -> bool: ...
    @IsAssumeAxialSymmetryUsed.setter
    def IsAssumeAxialSymmetryUsed(self, value: bool) -> None: ...
    @property
    def IsIgnoreLateralColorUsed(self) -> bool: ...
    @IsIgnoreLateralColorUsed.setter
    def IsIgnoreLateralColorUsed(self, value: bool) -> None: ...
    @property
    def IsAddFavoriteOperandsUsed(self) -> bool: ...
    @IsAddFavoriteOperandsUsed.setter
    def IsAddFavoriteOperandsUsed(self, value: bool) -> None: ...
    @property
    def IsRelativeXWeightUsed(self) -> bool: ...
    @IsRelativeXWeightUsed.setter
    def IsRelativeXWeightUsed(self, value: bool) -> None: ...
    @property
    def Type(self) -> int: ...
    @Type.setter
    def Type(self, value: int) -> None: ...
    @property
    def Data(self) -> int: ...
    @Data.setter
    def Data(self, value: int) -> None: ...
    @property
    def Reference(self) -> int: ...
    @Reference.setter
    def Reference(self, value: int) -> None: ...
    @property
    def PupilIntegrationMethod(self) -> int: ...
    @PupilIntegrationMethod.setter
    def PupilIntegrationMethod(self, value: int) -> None: ...
    @property
    def Ring(self) -> int: ...
    @Ring.setter
    def Ring(self, value: int) -> None: ...
    @property
    def Arm(self) -> int: ...
    @Arm.setter
    def Arm(self, value: int) -> None: ...
    @property
    def Grid(self) -> int: ...
    @Grid.setter
    def Grid(self, value: int) -> None: ...
    @property
    def Configuration(self) -> int: ...
    @Configuration.setter
    def Configuration(self, value: int) -> None: ...
    @property
    def StartAt(self) -> int: ...
    @StartAt.setter
    def StartAt(self, value: int) -> None: ...
    @property
    def Obscuration(self) -> float: ...
    @Obscuration.setter
    def Obscuration(self, value: float) -> None: ...
    @property
    def GlassMin(self) -> float: ...
    @GlassMin.setter
    def GlassMin(self, value: float) -> None: ...
    @property
    def GlassMax(self) -> float: ...
    @GlassMax.setter
    def GlassMax(self, value: float) -> None: ...
    @property
    def GlassEdge(self) -> float: ...
    @GlassEdge.setter
    def GlassEdge(self, value: float) -> None: ...
    @property
    def AirMin(self) -> float: ...
    @AirMin.setter
    def AirMin(self, value: float) -> None: ...
    @property
    def AirMax(self) -> float: ...
    @AirMax.setter
    def AirMax(self, value: float) -> None: ...
    @property
    def AirEdge(self) -> float: ...
    @AirEdge.setter
    def AirEdge(self, value: float) -> None: ...
    @property
    def RelativeXWeight(self) -> float: ...
    @RelativeXWeight.setter
    def RelativeXWeight(self, value: float) -> None: ...
    @property
    def OverallWeight(self) -> float: ...
    @OverallWeight.setter
    def OverallWeight(self, value: float) -> None: ...
    @property
    def NumberOfTypes(self) -> int: ...
    @property
    def NumberOfDataTypes(self) -> int: ...
    @property
    def NumberOfReferences(self) -> int: ...
    @property
    def NumberOfPupilIntegrationMethods(self) -> int: ...
    @property
    def NumberOfRings(self) -> int: ...
    @property
    def NumberOfArms(self) -> int: ...
    @property
    def NumberOfGrids(self) -> int: ...
    @property
    def NumberOfConfigurations(self) -> int: ...
    def GetArmAt(self, idx: int) -> str: ...
    def GetConfigurationAt(self, idx: int) -> str: ...
    def GetDataTypeAt(self, idx: int) -> str: ...
    def GetGridAt(self, idx: int) -> str: ...
    def GetPupilIntegrationMethodAt(self, idx: int) -> str: ...
    def GetReferenceAt(self, idx: int) -> str: ...
    def GetRingAt(self, idx: int) -> str: ...
    def GetTypeAt(self, idx: int) -> str: ...

class ISEQOptimizationWizard2(IWizard):
    @property
    def CommonSettings(self) -> IWizard: ...
    @property
    def Criterion(self) -> CriterionTypes: ...
    @Criterion.setter
    def Criterion(self, value: CriterionTypes) -> None: ...
    @property
    def SpatialFrequency(self) -> float: ...
    @SpatialFrequency.setter
    def SpatialFrequency(self, value: float) -> None: ...
    @property
    def XSWeight(self) -> float: ...
    @XSWeight.setter
    def XSWeight(self, value: float) -> None: ...
    @property
    def YTWeight(self) -> float: ...
    @YTWeight.setter
    def YTWeight(self, value: float) -> None: ...
    @property
    def Type(self) -> OptimizationTypes: ...
    @Type.setter
    def Type(self, value: OptimizationTypes) -> None: ...
    @property
    def Reference(self) -> ReferenceTypes: ...
    @Reference.setter
    def Reference(self, value: ReferenceTypes) -> None: ...
    @property
    def UseGaussianQuadrature(self) -> bool: ...
    @UseGaussianQuadrature.setter
    def UseGaussianQuadrature(self, value: bool) -> None: ...
    @property
    def UseRectangularArray(self) -> bool: ...
    @UseRectangularArray.setter
    def UseRectangularArray(self, value: bool) -> None: ...
    @property
    def Rings(self) -> int: ...
    @Rings.setter
    def Rings(self, value: int) -> None: ...
    @property
    def Arms(self) -> PupilArmsCount: ...
    @Arms.setter
    def Arms(self, value: PupilArmsCount) -> None: ...
    @property
    def Obscuration(self) -> float: ...
    @Obscuration.setter
    def Obscuration(self, value: float) -> None: ...
    @property
    def GridSizeNxN(self) -> int: ...
    @GridSizeNxN.setter
    def GridSizeNxN(self, value: int) -> None: ...
    @property
    def DeleteVignetted(self) -> bool: ...
    @DeleteVignetted.setter
    def DeleteVignetted(self, value: bool) -> None: ...
    @property
    def UseGlassBoundaryValues(self) -> bool: ...
    @UseGlassBoundaryValues.setter
    def UseGlassBoundaryValues(self, value: bool) -> None: ...
    @property
    def GlassMin(self) -> float: ...
    @GlassMin.setter
    def GlassMin(self, value: float) -> None: ...
    @property
    def GlassMax(self) -> float: ...
    @GlassMax.setter
    def GlassMax(self, value: float) -> None: ...
    @property
    def GlassEdgeThickness(self) -> float: ...
    @GlassEdgeThickness.setter
    def GlassEdgeThickness(self, value: float) -> None: ...
    @property
    def UseAirBoundaryValues(self) -> bool: ...
    @UseAirBoundaryValues.setter
    def UseAirBoundaryValues(self, value: bool) -> None: ...
    @property
    def AirMin(self) -> float: ...
    @AirMin.setter
    def AirMin(self, value: float) -> None: ...
    @property
    def AirMax(self) -> float: ...
    @AirMax.setter
    def AirMax(self, value: float) -> None: ...
    @property
    def AirEdgeThickness(self) -> float: ...
    @AirEdgeThickness.setter
    def AirEdgeThickness(self, value: float) -> None: ...
    @property
    def StartAt(self) -> int: ...
    @StartAt.setter
    def StartAt(self, value: int) -> None: ...
    @property
    def OverallWeight(self) -> float: ...
    @OverallWeight.setter
    def OverallWeight(self, value: float) -> None: ...
    @property
    def ConfigurationNumber(self) -> int: ...
    @ConfigurationNumber.setter
    def ConfigurationNumber(self, value: int) -> None: ...
    @property
    def UseAllConfigurations(self) -> bool: ...
    @UseAllConfigurations.setter
    def UseAllConfigurations(self, value: bool) -> None: ...
    @property
    def FieldNumber(self) -> int: ...
    @FieldNumber.setter
    def FieldNumber(self, value: int) -> None: ...
    @property
    def UseAllFields(self) -> bool: ...
    @UseAllFields.setter
    def UseAllFields(self, value: bool) -> None: ...
    @property
    def AssumeAxialSymmetry(self) -> bool: ...
    @AssumeAxialSymmetry.setter
    def AssumeAxialSymmetry(self, value: bool) -> None: ...
    @property
    def IgnoreLateralColor(self) -> bool: ...
    @IgnoreLateralColor.setter
    def IgnoreLateralColor(self, value: bool) -> None: ...
    @property
    def AddFavoriteOperands(self) -> bool: ...
    @AddFavoriteOperands.setter
    def AddFavoriteOperands(self, value: bool) -> None: ...
    @property
    def IsHighManufacturingYieldAvailable(self) -> bool: ...
    @property
    def OptimizeForBestNominalPerformance(self) -> bool: ...
    @OptimizeForBestNominalPerformance.setter
    def OptimizeForBestNominalPerformance(self, value: bool) -> None: ...
    @property
    def OptimizeForManufacturingYield(self) -> bool: ...
    @OptimizeForManufacturingYield.setter
    def OptimizeForManufacturingYield(self, value: bool) -> None: ...
    @property
    def ManufacturingYieldWeight(self) -> float: ...
    @ManufacturingYieldWeight.setter
    def ManufacturingYieldWeight(self, value: float) -> None: ...
    @property
    def UseMaximumDistortion(self) -> bool: ...
    @UseMaximumDistortion.setter
    def UseMaximumDistortion(self, value: bool) -> None: ...
    @property
    def MaxDistortionPct(self) -> float: ...
    @MaxDistortionPct.setter
    def MaxDistortionPct(self, value: float) -> None: ...

class ISEQToleranceWizard(IToleranceWizard, IWizard):
    @property
    def ToleranceSettings(self) -> IToleranceWizard: ...

class IToleranceWizard(IWizard):
    @property
    def CommonSettings(self) -> IWizard: ...
    @property
    def IsSEQToleranceWizard(self) -> bool: ...
    @property
    def IsSurfaceRadiusUsed(self) -> bool: ...
    @IsSurfaceRadiusUsed.setter
    def IsSurfaceRadiusUsed(self, value: bool) -> None: ...
    @property
    def IsSurfaceThicknessUsed(self) -> bool: ...
    @IsSurfaceThicknessUsed.setter
    def IsSurfaceThicknessUsed(self, value: bool) -> None: ...
    @property
    def IsSurfaceDecenterXUsed(self) -> bool: ...
    @IsSurfaceDecenterXUsed.setter
    def IsSurfaceDecenterXUsed(self, value: bool) -> None: ...
    @property
    def IsSurfaceDecenterYUsed(self) -> bool: ...
    @IsSurfaceDecenterYUsed.setter
    def IsSurfaceDecenterYUsed(self, value: bool) -> None: ...
    @property
    def IsSurfaceTiltXUsed(self) -> bool: ...
    @IsSurfaceTiltXUsed.setter
    def IsSurfaceTiltXUsed(self, value: bool) -> None: ...
    @property
    def IsSurfaceTiltYUsed(self) -> bool: ...
    @IsSurfaceTiltYUsed.setter
    def IsSurfaceTiltYUsed(self, value: bool) -> None: ...
    @property
    def IsSurfaceSandAIrregularityUsed(self) -> bool: ...
    @IsSurfaceSandAIrregularityUsed.setter
    def IsSurfaceSandAIrregularityUsed(self, value: bool) -> None: ...
    @property
    def IsSurfaceZernikeIrregularityUsed(self) -> bool: ...
    @IsSurfaceZernikeIrregularityUsed.setter
    def IsSurfaceZernikeIrregularityUsed(self, value: bool) -> None: ...
    @property
    def IsElementDecenterXUsed(self) -> bool: ...
    @IsElementDecenterXUsed.setter
    def IsElementDecenterXUsed(self, value: bool) -> None: ...
    @property
    def IsElementDecenterYUsed(self) -> bool: ...
    @IsElementDecenterYUsed.setter
    def IsElementDecenterYUsed(self, value: bool) -> None: ...
    @property
    def IsElementTiltXUsed(self) -> bool: ...
    @IsElementTiltXUsed.setter
    def IsElementTiltXUsed(self, value: bool) -> None: ...
    @property
    def IsElementTiltYUsed(self) -> bool: ...
    @IsElementTiltYUsed.setter
    def IsElementTiltYUsed(self, value: bool) -> None: ...
    @property
    def IsIndexUsed(self) -> bool: ...
    @IsIndexUsed.setter
    def IsIndexUsed(self, value: bool) -> None: ...
    @property
    def IsIndexAbbePercentageUsed(self) -> bool: ...
    @IsIndexAbbePercentageUsed.setter
    def IsIndexAbbePercentageUsed(self, value: bool) -> None: ...
    @property
    def IsFocusCompensationUsed(self) -> bool: ...
    @IsFocusCompensationUsed.setter
    def IsFocusCompensationUsed(self, value: bool) -> None: ...
    @property
    def SurfaceRadiusUnitType(self) -> DefaultAndFringes: ...
    @SurfaceRadiusUnitType.setter
    def SurfaceRadiusUnitType(self, value: DefaultAndFringes) -> None: ...
    @property
    def SurfaceTiltXUnitType(self) -> DefaultAndDegrees: ...
    @SurfaceTiltXUnitType.setter
    def SurfaceTiltXUnitType(self, value: DefaultAndDegrees) -> None: ...
    @property
    def SurfaceTiltYUnitType(self) -> DefaultAndDegrees: ...
    @SurfaceTiltYUnitType.setter
    def SurfaceTiltYUnitType(self, value: DefaultAndDegrees) -> None: ...
    @property
    def StartAt(self) -> int: ...
    @StartAt.setter
    def StartAt(self, value: int) -> None: ...
    @property
    def StartAtSurface(self) -> int: ...
    @StartAtSurface.setter
    def StartAtSurface(self, value: int) -> None: ...
    @property
    def StopAtSurface(self) -> int: ...
    @StopAtSurface.setter
    def StopAtSurface(self, value: int) -> None: ...
    @property
    def SurfaceRadius(self) -> float: ...
    @SurfaceRadius.setter
    def SurfaceRadius(self, value: float) -> None: ...
    @property
    def SurfaceRadiusFringes(self) -> float: ...
    @SurfaceRadiusFringes.setter
    def SurfaceRadiusFringes(self, value: float) -> None: ...
    @property
    def SurfaceThickness(self) -> float: ...
    @SurfaceThickness.setter
    def SurfaceThickness(self, value: float) -> None: ...
    @property
    def SurfaceDecenterX(self) -> float: ...
    @SurfaceDecenterX.setter
    def SurfaceDecenterX(self, value: float) -> None: ...
    @property
    def SurfaceDecenterY(self) -> float: ...
    @SurfaceDecenterY.setter
    def SurfaceDecenterY(self, value: float) -> None: ...
    @property
    def SurfaceTiltX(self) -> float: ...
    @SurfaceTiltX.setter
    def SurfaceTiltX(self, value: float) -> None: ...
    @property
    def SurfaceTiltXDegrees(self) -> float: ...
    @SurfaceTiltXDegrees.setter
    def SurfaceTiltXDegrees(self, value: float) -> None: ...
    @property
    def SurfaceTiltY(self) -> float: ...
    @SurfaceTiltY.setter
    def SurfaceTiltY(self, value: float) -> None: ...
    @property
    def SurfaceTiltYDegrees(self) -> float: ...
    @SurfaceTiltYDegrees.setter
    def SurfaceTiltYDegrees(self, value: float) -> None: ...
    @property
    def SurfaceSandAIrregularityFringes(self) -> float: ...
    @SurfaceSandAIrregularityFringes.setter
    def SurfaceSandAIrregularityFringes(self, value: float) -> None: ...
    @property
    def SurfaceZernikeIrregularityFringes(self) -> float: ...
    @SurfaceZernikeIrregularityFringes.setter
    def SurfaceZernikeIrregularityFringes(self, value: float) -> None: ...
    @property
    def ElementDecenterX(self) -> float: ...
    @ElementDecenterX.setter
    def ElementDecenterX(self, value: float) -> None: ...
    @property
    def ElementDecenterY(self) -> float: ...
    @ElementDecenterY.setter
    def ElementDecenterY(self, value: float) -> None: ...
    @property
    def ElementTiltXDegrees(self) -> float: ...
    @ElementTiltXDegrees.setter
    def ElementTiltXDegrees(self, value: float) -> None: ...
    @property
    def ElementTiltYDegrees(self) -> float: ...
    @ElementTiltYDegrees.setter
    def ElementTiltYDegrees(self, value: float) -> None: ...
    @property
    def Index(self) -> float: ...
    @Index.setter
    def Index(self, value: float) -> None: ...
    @property
    def IndexAbbePercentage(self) -> float: ...
    @IndexAbbePercentage.setter
    def IndexAbbePercentage(self, value: float) -> None: ...
    @property
    def TestWavelength(self) -> float: ...
    @TestWavelength.setter
    def TestWavelength(self, value: float) -> None: ...
    @property
    def SurfaceRadiusPercent(self) -> float: ...
    @SurfaceRadiusPercent.setter
    def SurfaceRadiusPercent(self, value: float) -> None: ...
    def SelectTolerancePreset(self, vendor: ToleranceVendor, grade: ToleranceGrade) -> None: ...

class IWizard:
    @property
    def Wizard(self) -> WizardType: ...
    def Apply(self) -> None: ...
    def Initialize(self) -> None: ...
    def LoadSettings(self) -> None: ...
    def OK(self) -> None: ...
    def ResetSettings(self) -> None: ...
    def SaveSettings(self) -> None: ...

class OptimizationTypes:
    RMS = 0
    PTV = 1

class PupilArmsCount:
    Arms_6 = 0
    Arms_8 = 1
    Arms_10 = 2
    Arms_12 = 3

class ReferenceTypes:
    Centroid = 0
    ChiefRay = 1
    Unreferenced = 2

class ToleranceGrade:
    Commercial = 0
    Precision = 1
    HighPrecision = 2
    CellPhoneLens = 3

class ToleranceVendor:
    Asphericon = 0
    EdmundOptics = 1
    Generic = 2
    LaCroix = 3
    Optimax = 4

class WizardType:
    NSCOptimization = 0
    NSCBitmap = 1
    NSCRoadwayLighting = 2
    SEQOptimization = 3
    NSCTolerance = 4
    SEQTolerance = 5
