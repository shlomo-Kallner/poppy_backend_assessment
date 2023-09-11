#!/bin/env python3

from typing import Optional, TYPE_CHECKING, Any
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

# from poppy_s.lib.models.prescriptionsMedicationLink import PrescriptionMedicationLink
from poppy_s.lib.models.prescriptionsMedicationDosage import PrescriptionsMedicationDosage

if TYPE_CHECKING:
    from poppy_s.lib.models.doctors import Doctor, DoctorRead
    from poppy_s.lib.models.patients import Patient, PatientRead
    from poppy_s.lib.models.medications import Medication, MedicationRead

class PrescriptionBase(SQLModel):
    created_at : datetime
    modified_at : datetime
    deleted_at : Optional[datetime] = None

    doctor_id : Optional[int] = Field(default=None, foreign_key="doctor.id")
    patient_id : Optional[int] = Field(default=None, foreign_key="patient.id")

class Prescription(PrescriptionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    dosages : list[PrescriptionsMedicationDosage] = Relationship(back_populates="prescriptions")
    medications : list["Medication"] = Relationship(link_model=PrescriptionsMedicationDosage)
    doctor: Optional["Doctor"] = Relationship(back_populates="prescriptions")
    patient : Optional["Patient"] = Relationship(back_populates="prescriptions")

class PrescriptionRead(PrescriptionBase):
    id: int

class PrescriptionReadFullData(PrescriptionRead):
    medications: list["MedicationRead"] = []
    doctor: Optional["DoctorRead"] = None
    patient : Optional["PatientRead"] = None