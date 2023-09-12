#!/bin/env python3

from typing import Optional, TYPE_CHECKING
# from pydantic import conint
from sqlmodel import SQLModel, Field, Relationship

from poppy_s.lib.models.interactionsMedicationLink import InteractionMedicationLink

if TYPE_CHECKING:
    # from poppy_s.lib.models.doctors import Doctor
    # from poppy_s.lib.models.prescriptions import Prescription
    from poppy_s.lib.models.medications import Medication, MedicationBase

class InteractionBase(SQLModel):
    warning: str = Field(
        min_length=1 #, index=True, unique=True
    )


class Interaction(InteractionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    medications : list["Medication"] = Relationship(
        back_populates="interactions",
        link_model=InteractionMedicationLink
    )


class InteractionRead(InteractionBase):
    id: int


class InteractionCreate(InteractionBase):
    rxcuis: list[int]


class InteractionReadWithMedications(InteractionRead):
    medications : list["MedicationBase"] = []