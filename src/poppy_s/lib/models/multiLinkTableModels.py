#!/bin/env python3

from typing import Optional #, TYPE_CHECKING
from sqlmodel import Field #, SQLModel, Relationship

from poppy_s.lib.models.base import (
    MedicationLinkBaseAsPrimaryKey, 
    PrescriptionLinkBaseAsPrimaryKey, 
    InteractionLinkBaseAsPrimaryKey
)


class PrescriptionMedicationLink(
    MedicationLinkBaseAsPrimaryKey, 
    PrescriptionLinkBaseAsPrimaryKey, 
    table=True
):
    # is_pending : bool = Field(default=True)
    pending_id : Optional[int] = Field(
        default=None
        # , 
        # foreign_key="prescription.id", 
        # primary_key=True
    )


class InteractionMedicationLink(MedicationLinkBaseAsPrimaryKey, InteractionLinkBaseAsPrimaryKey, table=True):
    pass

class InteractionPrescriptionLink(PrescriptionLinkBaseAsPrimaryKey, InteractionLinkBaseAsPrimaryKey, table=True):
    pass
