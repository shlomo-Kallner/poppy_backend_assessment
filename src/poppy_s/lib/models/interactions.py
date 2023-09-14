#!/bin/env python3

from typing import Optional, Type, cast, TYPE_CHECKING
# from pydantic import conint
from sqlmodel import Field, Relationship, SQLModel 

from poppy_s.lib.models.prescriptionValidationErrors import (
    PrescriptionValidationErrorsBase
)
from poppy_s.lib.models.base import (
    generateMedicationLinkRelationship
    # MedicationLinkBaseAsPrimaryKey,
    # PrescriptionLinkBaseAsPrimaryKey,
    # InteractionLinkBaseAsPrimaryKey
)
from poppy_s.lib.models.multiLinkTableModels import InteractionMedicationLink

if TYPE_CHECKING:
    from poppy_s.lib.models.prescriptions import Prescription
    from poppy_s.lib.models.medications import MedicationBase #, Medication

class InteractionBase(PrescriptionValidationErrorsBase):
    pass




Interaction_s_Medications_Field_BaseClass = cast(
    Type[SQLModel],
    generateMedicationLinkRelationship(
        back_population_field="interactions",
        link_model=InteractionMedicationLink
    )
)


class Interaction(InteractionBase, Interaction_s_Medications_Field_BaseClass, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # medications : list["Medication"] = Relationship(
    #     back_populates="interactions",
    #     link_model=InteractionMedicationLink
    # )



class InteractionRead(InteractionBase):
    id: int


class InteractionCreate(InteractionBase):
    # rxcuis: list[int]
    pass


class InteractionReadWithMedications(InteractionRead):
    medications : list["MedicationBase"] = []