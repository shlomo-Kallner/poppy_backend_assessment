#!/bin/env python3

from typing import Optional, TYPE_CHECKING
from datetime import timedelta
# from pydantic import conint
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    # from poppy_s.lib.models.doctors import Doctor
    from poppy_s.lib.models.prescriptions import Prescription, PrescriptionBase, PrescriptionRead
    from poppy_s.lib.models.medications import Medication, MedicationBase, MedicationRead

class PrescriptionsMedicationDosageBase(SQLModel):

    dose: int
    # unit: str
    frequency: str
    # every: timedelta
    medication_id : int = Field(
        foreign_key="medication.id"
    )
    prescription_id : int = Field(
        foreign_key="prescription.id"
    )


class PrescriptionsMedicationDosage(PrescriptionsMedicationDosageBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    medication : "Medication" = Relationship()
    prescription : "Prescription" = Relationship(back_populates="dosages")


class PrescriptionsMedicationDosageRead(PrescriptionsMedicationDosageBase):
    id: int

    medication : "MedicationRead"
    prescription : "PrescriptionRead"



