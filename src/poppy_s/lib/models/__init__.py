#!/bin/env python3


from poppy_s.lib.models.base import (
    T_SQLModel_TypeVar,
    MedicationLinkBase, 
    MedicationLinkBaseWithRequiredID,
    MedicationLinkBaseAsPrimaryKey, 
    MedicationLinkBaseAsPrimaryKeyWithRequiredID,
    T_MedicationLink_TypeVar,
    PrescriptionLinkBase,
    PrescriptionLinkBaseWithRequiredID,
    PrescriptionLinkBaseAsPrimaryKey,
    PrescriptionLinkBaseAsPrimaryKeyWithRequiredID,
    T_PrescriptionLink_TypeVar,
    InteractionLinkBase,
    InteractionLinkBaseAsPrimaryKey,
    InteractionLinkBaseWithRequiredID,
    InteractionLinkBaseAsPrimaryKeyWithRequiredID,
    T_InteractionLink_TypeVar
)
from poppy_s.lib.models.doctors import (
    Doctor, 
    DoctorRead, 
    DoctorCreate
)
from poppy_s.lib.models.medications import (
    Medication, 
    MedicationBase, 
    MedicationRead, 
    MedicationCreate
)
from poppy_s.lib.models.patients import (
    Patient, 
    PatientRead, 
    PatientCreate
)
from poppy_s.lib.models.prescriptions import (
    Prescription, 
    PrescriptionRead, 
    PrescriptionReadFullData, 
    PrescriptionCreate
)

from poppy_s.lib.models.prescriptionsMedicationDosage import (
    PrescriptionsMedicationDosage, 
    PrescriptionsMedicationDosageRead,
    PrescriptionsMedicationDosageCreate,
    PrescriptionsMedicationDosageBaseWithMedicationID,
    PrescriptionsMedicationDosageReadFull
)
from poppy_s.lib.models.interactions import (
    Interaction, 
    InteractionRead, 
    InteractionCreate, 
    InteractionReadWithMedications
)

from poppy_s.lib.models.multiLinkTableModels import (
    PrescriptionMedicationLink,
    InteractionMedicationLink,
    InteractionPrescriptionLink
)
from poppy_s.lib.models.prescriptionValidationErrors import PrescriptionValidationErrorsBase

###################
# NOTE: current error "issubclass() arg 1 must be a class" from `pydantic.schema.field_singleton_schema`
#   may be solved using the comments [here](https://github.com/tiangolo/sqlmodel/issues/121)
#   and [here](https://github.com/pydantic/pydantic/issues/1298).. 

InteractionReadWithMedications.update_forward_refs(
    MedicationBase=MedicationBase
)
Interaction.update_forward_refs(
    Medication=Medication
)


PrescriptionsMedicationDosageReadFull.update_forward_refs(
    MedicationRead=MedicationRead,
    PrescriptionRead=PrescriptionRead
)
PrescriptionsMedicationDosageRead.update_forward_refs(
    MedicationRead=MedicationRead
)
PrescriptionsMedicationDosage.update_forward_refs(
    Prescription=Prescription,
    Medication=Medication
)


PrescriptionReadFullData.update_forward_refs(
    MedicationRead=MedicationRead,
    DoctorRead=DoctorRead,
    PatientRead=PatientRead
)
Prescription.update_forward_refs(
    Medication=Medication,
    Doctor=Doctor,
    Patient=Patient
)


Patient.update_forward_refs(
    Prescription=Prescription
)


Medication.update_forward_refs(
    Interaction=Interaction
)


Doctor.update_forward_refs(
    Prescription=Prescription
)

###################

__all__ = (
    "Doctor", 
    "DoctorRead",
    "DoctorCreate",
    "Interaction", 
    "InteractionRead", 
    "InteractionCreate",
    "InteractionReadWithMedications",
    "InteractionMedicationLink",
    "InteractionPrescriptionLink",
    "Medication",
    "MedicationRead",
    "MedicationCreate",
    "Patient",
    "PatientRead",
    "PatientCreate",
    "Prescription",
    "PrescriptionRead",
    "PrescriptionCreate",
    "PrescriptionReadFullData",
    "PrescriptionsMedicationDosage",
    "PrescriptionsMedicationDosageRead",
    "PrescriptionsMedicationDosageCreate",
    "PrescriptionsMedicationDosageReadFull",
    "PrescriptionsMedicationDosageBaseWithMedicationID",
    "PrescriptionMedicationLink",
    "PrescriptionValidationErrorsBase",
    "T_SQLModel_TypeVar",
    "MedicationLinkBase", 
    "MedicationLinkBaseWithRequiredID",
    "MedicationLinkBaseAsPrimaryKey", 
    "MedicationLinkBaseAsPrimaryKeyWithRequiredID",
    "T_MedicationLink_TypeVar",
    "PrescriptionLinkBase",
    "PrescriptionLinkBaseWithRequiredID",
    "PrescriptionLinkBaseAsPrimaryKey",
    "PrescriptionLinkBaseAsPrimaryKeyWithRequiredID",
    "T_PrescriptionLink_TypeVar",
    "InteractionLinkBase",
    "InteractionLinkBaseAsPrimaryKey",
    "InteractionLinkBaseWithRequiredID",
    "InteractionLinkBaseAsPrimaryKeyWithRequiredID",
    "T_InteractionLink_TypeVar"
)