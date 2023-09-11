#!/bin/env python3

from typing import Optional
from sqlmodel import SQLModel, Field

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

