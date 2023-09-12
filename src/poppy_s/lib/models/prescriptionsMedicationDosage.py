#!/bin/env python3

from typing import Optional, TYPE_CHECKING
from datetime import timedelta
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from poppy_s.lib.models.prescriptions import Prescription, PrescriptionRead #, PrescriptionBase
    from poppy_s.lib.models.medications import Medication, MedicationRead #, MedicationBase

class PrescriptionsMedicationDosageBase(SQLModel):

    # unit: str ## NOt needed! Medications are one per rxcui which INCLUDES a specific Dose Unit!
    doses: int ## this is multiples of the Specifc Dose specified by the RXCUI!
    frequency: Optional[str] = None
    every: Optional[timedelta] = None
    prescription_id : int = Field(
        foreign_key="prescription.id"
    )


class PrescriptionsMedicationDosageCreate(PrescriptionsMedicationDosageBase):
    medication: str

class PrescriptionsMedicationDosageBaseWithMedicationID(PrescriptionsMedicationDosageBase):
    
    medication_id : int = Field(
        foreign_key="medication.id"
    )

class PrescriptionsMedicationDosage(PrescriptionsMedicationDosageBaseWithMedicationID, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    medication : "Medication" = Relationship()
    prescription : "Prescription" = Relationship(back_populates="dosages")


class PrescriptionsMedicationDosageRead(PrescriptionsMedicationDosageBaseWithMedicationID):
    id: int

    medication : "MedicationRead"


class PrescriptionsMedicationDosageReadFull(PrescriptionsMedicationDosageBaseWithMedicationID):
    id: int

    medication : "MedicationRead"
    prescription : "PrescriptionRead"



