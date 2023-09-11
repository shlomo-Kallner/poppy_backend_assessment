#!/bin/env python3

from typing import Optional, TYPE_CHECKING
from datetime import timedelta
# from pydantic import conint
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    # from poppy_s.lib.models.doctors import Doctor
    from poppy_s.lib.models.prescriptions import Prescription, PrescriptionBase
    from poppy_s.lib.models.medications import Medication, MedicationBase

class PrescriptionsMedicationDosageBase(SQLModel):

    dose: float
    unit: str
    frequency: str
    # every: timedelta
    medication_id : Optional[int] = Field(
        default=None, 
        foreign_key="medication.id"
        # , 
        # primary_key=True
    )
    prescription_id : Optional[int] = Field(
        default=None, 
        foreign_key="prescription.id"
        # , 
        # primary_key=True
    )


class PrescriptionsMedicationDosage(PrescriptionsMedicationDosageBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    medication : "Medication" = Relationship()
    prescription : "Prescription" = Relationship(back_populates="dosages")


class PrescriptionsMedicationDosageRead(PrescriptionsMedicationDosageBase):
    id: int

    medication : Optional["Medication"] = None
    prescription : Optional["Prescription"] = None



