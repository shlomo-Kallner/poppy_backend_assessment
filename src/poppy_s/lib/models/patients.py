#!/bin/env python3

from typing import Optional, cast, Type, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

# from poppy_s.lib.models.base import generatePrescriptionLinkRelationship

if TYPE_CHECKING:
#     # from poppy_s.lib.models.doctors import Doctor
    from poppy_s.lib.models.prescriptions import Prescription, PrescriptionRead

class PatientBase(SQLModel):
    name: str = Field(index=True, unique=True, min_length=1)


# Patient_s_Prescriptions_Field_BaseClass = cast(
#     Type[SQLModel],
#     generatePrescriptionLinkRelationship(
#         back_population_field="patient"
#     )
# )

class Patient(
    PatientBase, 
    # Patient_s_Prescriptions_Field_BaseClass, 
    table=True
):
    id: Optional[int] = Field(default=None, primary_key=True)

    # doctors : list["Doctor"] = Relationship(back_populates="patient")
    prescriptions : list["Prescription"] = Relationship(
        back_populates="patient"
    )

class PatientRead(PatientBase):
    id: int

class PatientCreate(PatientBase):
    pass