#!/bin/env python3

from typing import Optional, TypeVar
from sqlmodel import SQLModel, Field

class MedicationLinkBase(SQLModel):
    medication_id : Optional[int] = Field(
        default=None, 
        foreign_key="medication.id"
    )

class MedicationLinkBaseWithRequiredID(SQLModel):
    medication_id : int = Field(
        foreign_key="medication.id"
    )

class MedicationLinkBaseAsPrimaryKey(SQLModel):
    medication_id : Optional[int] = Field(
        default=None, 
        foreign_key="medication.id", 
        primary_key=True
    )

class MedicationLinkBaseAsPrimaryKeyWithRequiredID(SQLModel):
    medication_id : int = Field(
        foreign_key="medication.id", 
        primary_key=True
    )

T_MedicationLink_TypeVar = TypeVar(
    "T_MedicationLink_TypeVar", 
    bound=MedicationLinkBase|MedicationLinkBaseAsPrimaryKey|MedicationLinkBaseWithRequiredID|MedicationLinkBaseAsPrimaryKeyWithRequiredID
)
