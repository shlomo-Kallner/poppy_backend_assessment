#!/bin/env python3

from typing import Optional, cast, Type # , TYPE_CHECKING
from sqlmodel import SQLModel, Field #, Relationship
from pydantic import EmailStr

from poppy_s.lib.models.base import generatePrescriptionLinkRelationship

# if TYPE_CHECKING:
#     # from poppy_s.lib.models.patients import Patient, PatientBase
#     from poppy_s.lib.models.prescriptions import PrescriptionBase, Prescription

class DoctorBase(SQLModel):
    name: str = Field(index=True, unique=True, min_length=1)
    email: EmailStr = Field(index=True, unique=True)


Doctor_s_Prescriptions_Field_BaseClass = cast(
    Type[SQLModel],
    generatePrescriptionLinkRelationship(
        back_population_field="doctor"
    )
)

class Doctor(DoctorBase, Doctor_s_Prescriptions_Field_BaseClass, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # password_hashed: str

    # patients : list["Patient"] = Relationship(back_populates="doctor")
    # prescriptions : list["Prescription"] = Relationship(back_populates=)

class DoctorRead(DoctorBase):
    id: int

class DoctorCreate(DoctorBase):
    # password: str
    pass