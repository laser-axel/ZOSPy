"""This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from typing import Iterable, overload

from zospy.api._ZOSAPI.Analysis.Settings import IAS_, AxisType

__all__ = ("IAS_GrinProfile", "IAS_InternalTransmissionvsWavelength")

class IAS_GrinProfile(IAS_):
    @property
    def Surface(self) -> IAS_Surface: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @property
    def ShowIndexVs(self) -> AxisType: ...
    @ShowIndexVs.setter
    def ShowIndexVs(self, value: AxisType) -> None: ...
    @property
    def MinimumX(self) -> float: ...
    @MinimumX.setter
    def MinimumX(self, value: float) -> None: ...
    @property
    def MaximumX(self) -> float: ...
    @MaximumX.setter
    def MaximumX(self, value: float) -> None: ...
    @property
    def MinimumY(self) -> float: ...
    @MinimumY.setter
    def MinimumY(self, value: float) -> None: ...
    @property
    def MaximumY(self) -> float: ...
    @MaximumY.setter
    def MaximumY(self, value: float) -> None: ...
    @property
    def MinimumZ(self) -> float: ...
    @MinimumZ.setter
    def MinimumZ(self, value: float) -> None: ...
    @property
    def MaximumZ(self) -> float: ...
    @MaximumZ.setter
    def MaximumZ(self, value: float) -> None: ...
    @property
    def X_Value(self) -> float: ...
    @X_Value.setter
    def X_Value(self, value: float) -> None: ...
    @property
    def Y_Value(self) -> float: ...
    @Y_Value.setter
    def Y_Value(self, value: float) -> None: ...
    @property
    def Z_Value(self) -> float: ...
    @Z_Value.setter
    def Z_Value(self, value: float) -> None: ...
    @property
    def MinimumIndex(self) -> float: ...
    @MinimumIndex.setter
    def MinimumIndex(self, value: float) -> None: ...
    @property
    def MaximumIndex(self) -> float: ...
    @MaximumIndex.setter
    def MaximumIndex(self, value: float) -> None: ...

class IAS_InternalTransmissionvsWavelength(IAS_):
    @property
    def Glass1(self) -> str: ...
    @Glass1.setter
    def Glass1(self, value: str) -> None: ...
    @property
    def Glass2(self) -> str: ...
    @Glass2.setter
    def Glass2(self, value: str) -> None: ...
    @property
    def Glass3(self) -> str: ...
    @Glass3.setter
    def Glass3(self, value: str) -> None: ...
    @property
    def Glass4(self) -> str: ...
    @Glass4.setter
    def Glass4(self, value: str) -> None: ...
    @property
    def MinimumWave(self) -> float: ...
    @MinimumWave.setter
    def MinimumWave(self, value: float) -> None: ...
    @property
    def MaximumWave(self) -> float: ...
    @MaximumWave.setter
    def MaximumWave(self, value: float) -> None: ...
    @property
    def MinimumTransmission(self) -> float: ...
    @MinimumTransmission.setter
    def MinimumTransmission(self, value: float) -> None: ...
    @property
    def MaximumTransmission(self) -> float: ...
    @MaximumTransmission.setter
    def MaximumTransmission(self, value: float) -> None: ...
    @property
    def Thickness(self) -> float: ...
    @Thickness.setter
    def Thickness(self, value: float) -> None: ...
