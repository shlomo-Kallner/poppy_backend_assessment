#!/bin/env python3

from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr

if TYPE_CHECKING:
    # from poppy_s.lib.models.patients import Patient, PatientBase
    from poppy_s.lib.models.prescriptions import PrescriptionBase, Prescription

class DoctorBase(SQLModel):
    name: str = Field(index=True, unique=True, min_length=1)
    email: EmailStr = Field(index=True, unique=True)

class Doctor(DoctorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # password_hashed: str

    # patients : list["Patient"] = Relationship(back_populates="doctor")
    prescriptions : list["Prescription"] = Relationship(back_populates="doctor")

class DoctorRead(DoctorBase):
    id: int

class DoctorCreate(DoctorBase):
    # password: str
    pass