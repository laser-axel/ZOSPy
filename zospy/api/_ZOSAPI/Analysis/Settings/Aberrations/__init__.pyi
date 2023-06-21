"""
This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from zospy.api._ZOSAPI.Analysis import SampleSizes
from zospy.api._ZOSAPI.Analysis.Settings import (
    IAS_,
    IAS_Field,
    IAS_Surface,
    IAS_Wavelength,
)

__all__ = (
    "DisplayAsTypes",
    "Distortions",
    "FFA_AberrationTypes",
    "FFA_DecompositionTypes",
    "FFA_DisplayTypes",
    "FFA_FieldShapes",
    "FFA_ShowAsTypes",
    "FieldScanDirections",
    "IAS_FieldCurvatureAndDistortion",
    "IAS_FocalShiftDiagram",
    "IAS_FullFieldAberration",
    "IAS_GridDistortion",
    "IAS_LateralColor",
    "IAS_LongitudinalAberration",
    "IAS_RayTrace",
    "IAS_SeidelCoefficients",
    "IAS_SeidelDiagram",
    "IAS_ZernikeAnnularCoefficients",
    "IAS_ZernikeCoefficientsVsField",
    "IAS_ZernikeFringeCoefficients",
    "IAS_ZernikeStandardCoefficients",
    "RayTraceType",
    "ZernikeCoefficientTypes",
)

class DisplayAsTypes:
    Percent = 0
    Absolute = 1

class Distortions:
    F_TanTheta = 0
    F_Theta = 1
    Cal_F_Theta = 2
    Cal_F_TanTheta = 3
    SMIA_TV = 4

class FFA_AberrationTypes:
    Defocus = 0
    PrimaryAstigmatism = 1
    PrimaryComa = 2
    SpecifiedTerm = 3

class FFA_DecompositionTypes:
    ZernikeTerms = 0

class FFA_DisplayTypes:
    Absolute = 0
    Relative = 1
    Average = 2

class FFA_FieldShapes:
    Rectangular = 0
    Elliptical = 1

class FFA_ShowAsTypes:
    GreyScale = 0
    GreyScaleInverted = 1
    FalseColor = 2
    FalseColorInverted = 3
    Icons = 4

class FieldScanDirections:
    Plus_Y = 0
    Plus_X = 1
    Minus_Y = 2
    Minus_X = 3

class IAS_FieldCurvatureAndDistortion(IAS_):
    @property
    def DisplayAs(self) -> DisplayAsTypes: ...
    @property
    def Distortion(self) -> Distortions: ...
    @property
    def FieldAspectRatio(self) -> float: ...
    @property
    def IgnoreVignette(self) -> bool: ...
    @property
    def MaximumCurvature(self) -> float: ...
    @property
    def MaximumDistortion(self) -> float: ...
    @property
    def ReferenceField(self) -> IAS_Field: ...
    @property
    def ScanType(self) -> FieldScanDirections: ...
    @property
    def UseDashes(self) -> bool: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @DisplayAs.setter
    def DisplayAs(self, value: DisplayAsTypes) -> None: ...
    @Distortion.setter
    def Distortion(self, value: Distortions) -> None: ...
    @FieldAspectRatio.setter
    def FieldAspectRatio(self, value: float) -> None: ...
    @IgnoreVignette.setter
    def IgnoreVignette(self, value: bool) -> None: ...
    @MaximumCurvature.setter
    def MaximumCurvature(self, value: float) -> None: ...
    @MaximumDistortion.setter
    def MaximumDistortion(self, value: float) -> None: ...
    @ScanType.setter
    def ScanType(self, value: FieldScanDirections) -> None: ...
    @UseDashes.setter
    def UseDashes(self, value: bool) -> None: ...

class IAS_FocalShiftDiagram(IAS_):
    @property
    def MaximumShift(self) -> float: ...
    @property
    def PupilZone(self) -> float: ...
    @MaximumShift.setter
    def MaximumShift(self, value: float) -> None: ...
    @PupilZone.setter
    def PupilZone(self, value: float) -> None: ...

class IAS_FullFieldAberration(IAS_):
    @property
    def AberrationNumber(self) -> int: ...
    @property
    def AberrationType(self) -> FFA_AberrationTypes: ...
    @property
    def Decomposition(self) -> FFA_DecompositionTypes: ...
    @property
    def Display(self) -> FFA_DisplayTypes: ...
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def FieldShape(self) -> FFA_FieldShapes: ...
    @property
    def MaximumTerm(self) -> int: ...
    @property
    def PupilSampling(self) -> SampleSizes: ...
    @property
    def ShowAs(self) -> FFA_ShowAsTypes: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @property
    def XFieldSampling(self) -> int: ...
    @property
    def XFieldWidth(self) -> float: ...
    @property
    def YFieldSampling(self) -> int: ...
    @property
    def YFieldWidth(self) -> float: ...
    @Decomposition.setter
    def Decomposition(self, value: FFA_DecompositionTypes) -> None: ...
    @Display.setter
    def Display(self, value: FFA_DisplayTypes) -> None: ...
    @FieldShape.setter
    def FieldShape(self, value: FFA_FieldShapes) -> None: ...
    @MaximumTerm.setter
    def MaximumTerm(self, value: int) -> None: ...
    @PupilSampling.setter
    def PupilSampling(self, value: SampleSizes) -> None: ...
    @ShowAs.setter
    def ShowAs(self, value: FFA_ShowAsTypes) -> None: ...
    @XFieldSampling.setter
    def XFieldSampling(self, value: int) -> None: ...
    @XFieldWidth.setter
    def XFieldWidth(self, value: float) -> None: ...
    @YFieldSampling.setter
    def YFieldSampling(self, value: int) -> None: ...
    @YFieldWidth.setter
    def YFieldWidth(self, value: float) -> None: ...
    def SetAberrationByNumber(self, aberrationNumber: int) -> bool: ...
    def SetAberrationByType(self, type: FFA_AberrationTypes) -> bool: ...

class IAS_GridDistortion(IAS_):
    @property
    def Aspect(self) -> float: ...
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def FieldWidth(self) -> float: ...
    @property
    def GridNumber(self) -> int: ...
    @property
    def Method(self) -> int: ...
    @property
    def RotateText(self) -> int: ...
    @property
    def ScaleFactor(self) -> float: ...
    @property
    def SymmetricMagnification(self) -> bool: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @Aspect.setter
    def Aspect(self, value: float) -> None: ...
    @FieldWidth.setter
    def FieldWidth(self, value: float) -> None: ...
    @GridNumber.setter
    def GridNumber(self, value: int) -> None: ...
    @Method.setter
    def Method(self, value: int) -> None: ...
    @RotateText.setter
    def RotateText(self, value: int) -> None: ...
    @ScaleFactor.setter
    def ScaleFactor(self, value: float) -> None: ...
    @SymmetricMagnification.setter
    def SymmetricMagnification(self, value: bool) -> None: ...

class IAS_LateralColor(IAS_):
    @property
    def AllWavelengths(self) -> bool: ...
    @property
    def PlotScale(self) -> float: ...
    @property
    def ShowAiryDisk(self) -> bool: ...
    @property
    def UseRealRays(self) -> bool: ...
    @AllWavelengths.setter
    def AllWavelengths(self, value: bool) -> None: ...
    @PlotScale.setter
    def PlotScale(self, value: float) -> None: ...
    @ShowAiryDisk.setter
    def ShowAiryDisk(self, value: bool) -> None: ...
    @UseRealRays.setter
    def UseRealRays(self, value: bool) -> None: ...

class IAS_LongitudinalAberration(IAS_):
    @property
    def PlotScale(self) -> float: ...
    @property
    def UseDashes(self) -> bool: ...
    @PlotScale.setter
    def PlotScale(self, value: float) -> None: ...
    @UseDashes.setter
    def UseDashes(self, value: bool) -> None: ...

class IAS_RayTrace(IAS_):
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def Hx(self) -> float: ...
    @property
    def Hy(self) -> float: ...
    @property
    def Px(self) -> float: ...
    @property
    def Py(self) -> float: ...
    @property
    def Type(self) -> RayTraceType: ...
    @property
    def UseGlobal(self) -> bool: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @Hx.setter
    def Hx(self, value: float) -> None: ...
    @Hy.setter
    def Hy(self, value: float) -> None: ...
    @Px.setter
    def Px(self, value: float) -> None: ...
    @Py.setter
    def Py(self, value: float) -> None: ...
    @Type.setter
    def Type(self, value: RayTraceType) -> None: ...
    @UseGlobal.setter
    def UseGlobal(self, value: bool) -> None: ...
    def UseArbitraryRay(self) -> None: ...

class IAS_SeidelCoefficients(IAS_):
    @property
    def Wavelength(self) -> IAS_Wavelength: ...

class IAS_SeidelDiagram(IAS_):
    @property
    def IgnoreChromatic(self) -> bool: ...
    @property
    def IgnoreDistortion(self) -> bool: ...
    @property
    def PlotScale(self) -> float: ...
    @property
    def SuppressFrame(self) -> bool: ...
    @IgnoreChromatic.setter
    def IgnoreChromatic(self, value: bool) -> None: ...
    @IgnoreDistortion.setter
    def IgnoreDistortion(self, value: bool) -> None: ...
    @PlotScale.setter
    def PlotScale(self, value: float) -> None: ...
    @SuppressFrame.setter
    def SuppressFrame(self, value: bool) -> None: ...

class IAS_ZernikeAnnularCoefficients(IAS_):
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def MaximumNumberOfTerms(self) -> int: ...
    @property
    def Obscuration(self) -> float: ...
    @property
    def ReferenceOBDToVertex(self) -> bool: ...
    @property
    def SampleSize(self) -> SampleSizes: ...
    @property
    def Sr(self) -> float: ...
    @property
    def Surface(self) -> IAS_Surface: ...
    @property
    def Sx(self) -> float: ...
    @property
    def Sy(self) -> float: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @MaximumNumberOfTerms.setter
    def MaximumNumberOfTerms(self, value: int) -> None: ...
    @Obscuration.setter
    def Obscuration(self, value: float) -> None: ...
    @ReferenceOBDToVertex.setter
    def ReferenceOBDToVertex(self, value: bool) -> None: ...
    @SampleSize.setter
    def SampleSize(self, value: SampleSizes) -> None: ...
    @Sr.setter
    def Sr(self, value: float) -> None: ...
    @Sx.setter
    def Sx(self, value: float) -> None: ...
    @Sy.setter
    def Sy(self, value: float) -> None: ...

class IAS_ZernikeCoefficientsVsField(IAS_):
    @property
    def Coefficients(self) -> str: ...
    @property
    def FieldDensity(self) -> int: ...
    @property
    def FieldScanDirection(self) -> FieldScanDirections: ...
    @property
    def ObscurationFactor(self) -> float: ...
    @property
    def SampleSize(self) -> SampleSizes: ...
    @property
    def ScaleMaximum(self) -> float: ...
    @property
    def ScaleMinimum(self) -> float: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @property
    def ZernikeCoefficientType(self) -> ZernikeCoefficientTypes: ...
    @Coefficients.setter
    def Coefficients(self, value: str) -> None: ...
    @FieldDensity.setter
    def FieldDensity(self, value: int) -> None: ...
    @FieldScanDirection.setter
    def FieldScanDirection(self, value: FieldScanDirections) -> None: ...
    @ObscurationFactor.setter
    def ObscurationFactor(self, value: float) -> None: ...
    @SampleSize.setter
    def SampleSize(self, value: SampleSizes) -> None: ...
    @ScaleMaximum.setter
    def ScaleMaximum(self, value: float) -> None: ...
    @ScaleMinimum.setter
    def ScaleMinimum(self, value: float) -> None: ...
    @ZernikeCoefficientType.setter
    def ZernikeCoefficientType(self, value: ZernikeCoefficientTypes) -> None: ...

class IAS_ZernikeFringeCoefficients(IAS_):
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def MaximumNumberOfTerms(self) -> int: ...
    @property
    def ReferenceOBDToVertex(self) -> bool: ...
    @property
    def SampleSize(self) -> SampleSizes: ...
    @property
    def Sr(self) -> float: ...
    @property
    def Surface(self) -> IAS_Surface: ...
    @property
    def Sx(self) -> float: ...
    @property
    def Sy(self) -> float: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @MaximumNumberOfTerms.setter
    def MaximumNumberOfTerms(self, value: int) -> None: ...
    @ReferenceOBDToVertex.setter
    def ReferenceOBDToVertex(self, value: bool) -> None: ...
    @SampleSize.setter
    def SampleSize(self, value: SampleSizes) -> None: ...
    @Sr.setter
    def Sr(self, value: float) -> None: ...
    @Sx.setter
    def Sx(self, value: float) -> None: ...
    @Sy.setter
    def Sy(self, value: float) -> None: ...

class IAS_ZernikeStandardCoefficients(IAS_):
    @property
    def Epsilon(self) -> float: ...
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def MaximumNumberOfTerms(self) -> int: ...
    @property
    def ReferenceOBDToVertex(self) -> bool: ...
    @property
    def SampleSize(self) -> SampleSizes: ...
    @property
    def Sr(self) -> float: ...
    @property
    def Surface(self) -> IAS_Surface: ...
    @property
    def Sx(self) -> float: ...
    @property
    def Sy(self) -> float: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @Epsilon.setter
    def Epsilon(self, value: float) -> None: ...
    @MaximumNumberOfTerms.setter
    def MaximumNumberOfTerms(self, value: int) -> None: ...
    @ReferenceOBDToVertex.setter
    def ReferenceOBDToVertex(self, value: bool) -> None: ...
    @SampleSize.setter
    def SampleSize(self, value: SampleSizes) -> None: ...
    @Sr.setter
    def Sr(self, value: float) -> None: ...
    @Sx.setter
    def Sx(self, value: float) -> None: ...
    @Sy.setter
    def Sy(self, value: float) -> None: ...

class RayTraceType:
    DirectionCosines = 0
    TangentAngle = 1
    YmUmYcUc = 2

class ZernikeCoefficientTypes:
    Fringe = 0
    Standard = 1
    Annular = 2