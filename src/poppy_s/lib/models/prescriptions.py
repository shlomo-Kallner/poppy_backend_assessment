#!/bin/env python3

from typing import Optional, TYPE_CHECKING, Any
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

# from poppy_s.lib.models.prescriptionsMedicationLink import PrescriptionMedicationLink
from poppy_s.lib.models.prescriptionsMedicationDosage import (
    PrescriptionsMedicationDosage,
    PrescriptionsMedicationDosageRead
)

if TYPE_CHECKING:
    from poppy_s.lib.models.doctors import Doctor, DoctorRead
    from poppy_s.lib.models.patients import Patient, PatientRead
    from poppy_s.lib.models.medications import Medication, MedicationRead

class PrescriptionBase(SQLModel):

    doctor_id : int = Field(default=None, foreign_key="doctor.id")
    patient_id : int = Field(default=None, foreign_key="patient.id")

class Prescription(PrescriptionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # created_at : datetime
    # modified_at : datetime
    sealed_at : Optional[datetime] = None
    # deleted_at : Optional[datetime] = None

    dosages : list[PrescriptionsMedicationDosage] = Relationship(back_populates="prescription")
    medications : list["Medication"] = Relationship(
        link_model=PrescriptionsMedicationDosage, 
        sa_relationship_kwargs={"overlaps":"dosages,prescription"}
    )
    doctor : "Doctor" = Relationship(back_populates="prescriptions")
    patient : "Patient" = Relationship(back_populates="prescriptions")
    warnings: list[str] = []

class PrescriptionRead(PrescriptionBase):
    id: int
    # created_at : datetime
    # modified_at : datetime
    sealed_at : Optional[datetime] = None
    # deleted_at : Optional[datetime] = None

class PrescriptionCreate(PrescriptionBase):
    pass

class PrescriptionReadFullData(PrescriptionRead):
    medications: list["MedicationRead"] = []
    dosages : list[PrescriptionsMedicationDosageRead] = []
    doctor: "DoctorRead"
    patient : "PatientRead"
    warnings: list[str] = []