#!/bin/env python3

from typing import Optional, TypeVar
from sqlmodel import SQLModel, Field


class InteractionLinkBase(SQLModel):
    interaction_id : Optional[int] = Field(
        default=None, 
        foreign_key="interaction.id"
    )

class InteractionLinkBaseWithRequiredID(SQLModel):
    interaction_id : int = Field(
        foreign_key="interaction.id"
    )

class InteractionLinkBaseAsPrimaryKey(SQLModel):
    interaction_id : Optional[int] = Field(
        default=None, 
        foreign_key="interaction.id", 
        primary_key=True
    )

class InteractionLinkBaseAsPrimaryKeyWithRequiredID(SQLModel):
    interaction_id : int = Field(
        foreign_key="interaction.id", 
        primary_key=True
    )

T_InteractionLink_TypeVar = TypeVar(
    "T_InteractionLink_TypeVar", 
    bound=InteractionLinkBase|InteractionLinkBaseWithRequiredID|InteractionLinkBaseAsPrimaryKey|InteractionLinkBaseAsPrimaryKeyWithRequiredID
)

