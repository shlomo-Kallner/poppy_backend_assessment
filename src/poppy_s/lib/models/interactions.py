#!/bin/env python3

from typing import Optional, TYPE_CHECKING
# from pydantic import conint
from sqlmodel import Field, Relationship #, SQLModel 

from poppy_s.lib.models.prescriptionValidationErrors import (
    PrescriptionValidationErrorsBase
)
from poppy_s.lib.models.base import (
    MedicationLinkBaseAsPrimaryKey,
    PrescriptionLinkBaseAsPrimaryKey
)

if TYPE_CHECKING:
    from poppy_s.lib.models.prescriptions import Prescription
    from poppy_s.lib.models.medications import Medication, MedicationBase

class InteractionBase(PrescriptionValidationErrorsBase):
    pass


class InteractionMedicationLink(MedicationLinkBaseAsPrimaryKey, table=True):
    interaction_id : Optional[int] = Field(
        default=None, 
        foreign_key="interaction.id", 
        primary_key=True
    )

class InteractionPrescriptionLink(PrescriptionLinkBaseAsPrimaryKey, table=True):
    interaction_id : Optional[int] = Field(
        default=None, 
        foreign_key="interaction.id", 
        primary_key=True
    )

class Interaction(InteractionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    medications : list["Medication"] = Relationship(
        # back_populates="interactions",
        link_model=InteractionMedicationLink
    )



class InteractionRead(InteractionBase):
    id: int


class InteractionCreate(InteractionBase):
    # rxcuis: list[int]
    pass


class InteractionReadWithMedications(InteractionRead):
    medications : list["MedicationBase"] = []