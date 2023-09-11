#!/bin/env python3

from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    # from poppy_s.lib.models.doctors import Doctor
    from poppy_s.lib.models.prescriptions import Prescription

class PatientBase(SQLModel):
    name: str = Field(index=True, unique=True, min_length=1)

class Patient(PatientBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # doctors : list["Doctor"] = Relationship(back_populates="patient")
    prescriptions : list["Prescription"] = Relationship(back_populates="patient")

class PatientRead(PatientBase):
    id: int