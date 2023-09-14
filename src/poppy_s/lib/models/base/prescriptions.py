#!/bin/env python3

from typing import Optional, TypeVar
from sqlmodel import SQLModel, Field

class PrescriptionLinkBase(SQLModel):
    prescription_id : Optional[int] = Field(
        default=None, 
        foreign_key="prescription.id"
    )

class PrescriptionLinkBaseWithRequiredID(SQLModel):
    prescription_id : int = Field(
        foreign_key="prescription.id"
    )

class PrescriptionLinkBaseAsPrimaryKey(SQLModel):
    prescription_id : Optional[int] = Field(
        default=None, 
        foreign_key="prescription.id", 
        primary_key=True
    )

class PrescriptionLinkBaseAsPrimaryKeyWithRequiredID(SQLModel):
    prescription_id : int = Field(
        foreign_key="prescription.id", 
        primary_key=True
    )

T_PrescriptionLink_TypeVar = TypeVar(
    "T_PrescriptionLink_TypeVar", 
    bound=PrescriptionLinkBase|PrescriptionLinkBaseAsPrimaryKey|PrescriptionLinkBaseWithRequiredID|PrescriptionLinkBaseAsPrimaryKeyWithRequiredID
)

