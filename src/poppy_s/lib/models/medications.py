#!/bin/env python3

from typing import Optional, Type, cast #, TYPE_CHECKING
# from pydantic import conint
from sqlmodel import SQLModel, Field #, Relationship

from poppy_s.lib.models.base import generateInteractionLinkRelationship
from poppy_s.lib.models.multiLinkTableModels import InteractionMedicationLink

# if TYPE_CHECKING:
#     # from poppy_s.lib.models.doctors import Doctor
#     # from poppy_s.lib.models.prescriptions import Prescription
#     from poppy_s.lib.models.interactions import Interaction

class MedicationBase(SQLModel):
    # name: str = Field(index=True, unique=True, min_length=1)
    name: str = Field(min_length=1)
    rxcui: int = Field(index=True, unique=True, gt=0
        # , alias="RXCUIS"
    )
    description: str


Medication_s_Interactions_Field_BaseClass = cast(
    Type[SQLModel],
    generateInteractionLinkRelationship(
        back_population_field="medications",
        link_model=InteractionMedicationLink
    )
)

class Medication(MedicationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    ## Query: re-evaluate why/if this should be here!!
    ## Answer: We need them for the plugin's interactions fetcher...

    # interactions : list["Interaction"] = Relationship(
    #     back_populates="medications", 
    #     link_model=InteractionMedicationLink
    # )


class MedicationRead(MedicationBase):
    id: int


class MedicationCreate(MedicationBase):
    pass
