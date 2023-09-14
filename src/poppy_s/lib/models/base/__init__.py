#!/bin/env python3

from poppy_s.lib.models.base.base import T_SQLModel_TypeVar
from poppy_s.lib.models.base.medications import (
    MedicationLinkBase, 
    MedicationLinkBaseWithRequiredID,
    MedicationLinkBaseAsPrimaryKey, 
    MedicationLinkBaseAsPrimaryKeyWithRequiredID,
    # generateMedicationLinkRelationship,
    T_MedicationLink_TypeVar
    # ,
    # SimpleMedicationLinkRelationship,
    # SimpleMedicationsLinkRelationship,
    # SimpleMedicationLinkRelationshipWithSQLModelBase,
    # SimpleMedicationsLinkRelationshipWithSQLModelBase
)
from poppy_s.lib.models.base.prescriptions import (
    PrescriptionLinkBase,
    PrescriptionLinkBaseWithRequiredID,
    PrescriptionLinkBaseAsPrimaryKey,
    PrescriptionLinkBaseAsPrimaryKeyWithRequiredID,
    # generatePrescriptionLinkRelationship,
    T_PrescriptionLink_TypeVar
    # ,
    # SimplePrescriptionsLinkRelationship,
    # SimplePrescriptionLinkRelationship,
    # SimplePrescriptionLinkRelationshipWithSQLModelBase,
    # SimplePrescriptionsLinkRelationshipWithSQLModelBase
)
from poppy_s.lib.models.base.interactions import (
    InteractionLinkBase,
    InteractionLinkBaseAsPrimaryKey,
    InteractionLinkBaseWithRequiredID,
    InteractionLinkBaseAsPrimaryKeyWithRequiredID,
    # generateInteractionLinkRelationship,
    T_InteractionLink_TypeVar,
#     SimpleInteractionLinkRelationship,
#     SimpleInteractionsLinkRelationship,
#     SimpleInteractionLinkRelationshipWithSQLModelBase,
#     SimpleInteractionsLinkRelationshipWithSQLModelBase
)

__all__ = (
    "T_SQLModel_TypeVar",
    "MedicationLinkBase", 
    "MedicationLinkBaseWithRequiredID",
    "MedicationLinkBaseAsPrimaryKey", 
    "MedicationLinkBaseAsPrimaryKeyWithRequiredID",
    # "generateMedicationLinkRelationship",
    "T_MedicationLink_TypeVar",
    # "SimpleMedicationLinkRelationship",
    # "SimpleMedicationsLinkRelationship",
    # "SimpleMedicationLinkRelationshipWithSQLModelBase",
    # "SimpleMedicationsLinkRelationshipWithSQLModelBase",
    "PrescriptionLinkBase",
    "PrescriptionLinkBaseWithRequiredID",
    "PrescriptionLinkBaseAsPrimaryKey",
    "PrescriptionLinkBaseAsPrimaryKeyWithRequiredID",
    # "generatePrescriptionLinkRelationship",
    "T_PrescriptionLink_TypeVar",
    # "SimplePrescriptionLinkRelationship",
    # "SimplePrescriptionsLinkRelationship",
    # "SimplePrescriptionLinkRelationshipWithSQLModelBase",
    # "SimplePrescriptionsLinkRelationshipWithSQLModelBase",
    "InteractionLinkBase",
    "InteractionLinkBaseAsPrimaryKey",
    "InteractionLinkBaseWithRequiredID",
    "InteractionLinkBaseAsPrimaryKeyWithRequiredID",
    # "generateInteractionLinkRelationship",
    "T_InteractionLink_TypeVar"
    # ,
    # "SimpleInteractionLinkRelationship",
    # "SimpleInteractionsLinkRelationship",
    # "SimpleInteractionLinkRelationshipWithSQLModelBase",
    # "SimpleInteractionsLinkRelationshipWithSQLModelBase"
)