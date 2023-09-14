#!/bin/env python3

from typing import Optional, TYPE_CHECKING
from datetime import timedelta
from sqlmodel import SQLModel, Field, Relationship

from poppy_s.lib.models.base import (
    MedicationLinkBaseWithRequiredID, 
    PrescriptionLinkBaseWithRequiredID
)

if TYPE_CHECKING:
    from poppy_s.lib.models.prescriptions import Prescription, PrescriptionRead #, PrescriptionBase
    from poppy_s.lib.models.medications import Medication, MedicationRead #, MedicationBase

class PrescriptionsMedicationDosageBase(PrescriptionLinkBaseWithRequiredID):

    # unit: str ## NOt needed! Medications are one per rxcui which INCLUDES a specific Dose Unit!
    doses: int ## this is multiples of the Specifc Dose specified by the RXCUI!
    frequency: Optional[str] = None
    every: Optional[timedelta] = None


class PrescriptionsMedicationDosageCreate(PrescriptionsMedicationDosageBase):
    medication: str

class PrescriptionsMedicationDosageBaseWithMedicationID(
    PrescriptionsMedicationDosageBase, 
    MedicationLinkBaseWithRequiredID
):
    pass

class PrescriptionsMedicationDosage(
    PrescriptionsMedicationDosageBaseWithMedicationID, 
    table=True
):
    id: Optional[int] = Field(default=None, primary_key=True)

    prescription : "Prescription" = Relationship(
        back_populates="dosages"
    )
    medication : "Medication" = Relationship()



class PrescriptionsMedicationDosageRead(PrescriptionsMedicationDosageBaseWithMedicationID):
    id: int

    medication : "MedicationRead"


class PrescriptionsMedicationDosageReadFull(PrescriptionsMedicationDosageBaseWithMedicationID):
    id: int

    medication : "MedicationRead"
    prescription : "PrescriptionRead"



