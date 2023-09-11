#!/bin/env python3

from typing import Optional #, TYPE_CHECKING
# from pydantic import conint
from sqlmodel import SQLModel, Field #, Relationship

# if TYPE_CHECKING:
    # # from poppy_s.lib.models.doctors import Doctor
    # from poppy_s.lib.models.prescriptions import Prescription
    # from poppy_s.lib.models.medications import Medication, MedicationBase

class InteractionMedicationLink(SQLModel, table=True):
    medication_id : Optional[int] = Field(
        default=None, 
        foreign_key="medication.id", 
        primary_key=True
    )
    interaction_id : Optional[int] = Field(
        default=None, 
        foreign_key="interaction.id", 
        primary_key=True
    )


# class InteractionsMedicationLink(InteractionMedicationLinkBase):
#     id: Optional[int] = Field(default=None, primary_key=True)

