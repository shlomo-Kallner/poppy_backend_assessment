#!/bin/env python3

from typing import Optional, Type, TypeVar, TYPE_CHECKING, Sequence, Any, Mapping, cast
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import RelationshipProperty
from sqlalchemy.orm.decl_api import DeclarativeMeta

from poppy_s.lib.models.base.base import T_SQLModel_TypeVar


if TYPE_CHECKING:
    from poppy_s.lib.models.interactions import Interaction



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

# def generateInteractionLinkRelationship(
#     *,
#     containerRelashionship: bool = True,
#     withSQLModelBaseClass: bool = True,
#     link_model: Optional[Type[T_InteractionLink_TypeVar]] = None,
#     back_population_field: Optional[str] = None,
#     sa_relationship: Optional[RelationshipProperty] = None,
#     sa_relationship_args: Optional[Sequence[Any]] = None,
#     sa_relationship_kwargs: Optional[Mapping[str, Any]] = None
# ) -> Type[SQLModel]|Type[DeclarativeMeta]:

#     if withSQLModelBaseClass and containerRelashionship:

#         class InteractionsLinkRelationshipWithSQLModel(SQLModel):

#             interactions : list["Interaction"] = Relationship(
#                 back_populates=back_population_field,
#                 link_model=link_model,
#                 sa_relationship=sa_relationship,
#                 sa_relationship_args=sa_relationship_args,
#                 sa_relationship_kwargs=sa_relationship_kwargs
#             )

#         return InteractionsLinkRelationshipWithSQLModel

#     elif not withSQLModelBaseClass and containerRelashionship:

#         class InteractionsLinkRelationshipWithoutSQLModel(DeclarativeMeta):

#             interactions : list["Interaction"] = Relationship(
#                 back_populates=back_population_field,
#                 link_model=link_model,
#                 sa_relationship=sa_relationship,
#                 sa_relationship_args=sa_relationship_args,
#                 sa_relationship_kwargs=sa_relationship_kwargs
#             )

#         return InteractionsLinkRelationshipWithoutSQLModel

#     elif withSQLModelBaseClass and not containerRelashionship:

#         class InteractionLinkRelationshipWithSQLModel(SQLModel):

#             interaction : "Interaction" = Relationship(
#                 back_populates=back_population_field,
#                 link_model=link_model,
#                 sa_relationship=sa_relationship,
#                 sa_relationship_args=sa_relationship_args,
#                 sa_relationship_kwargs=sa_relationship_kwargs
#             )

#         return InteractionLinkRelationshipWithSQLModel
    
#     else:

#         class InteractionLinkRelationshipWithoutSQLModel(DeclarativeMeta):

#             interaction : "Interaction" = Relationship(
#                 back_populates=back_population_field,
#                 link_model=link_model,
#                 sa_relationship=sa_relationship,
#                 sa_relationship_args=sa_relationship_args,
#                 sa_relationship_kwargs=sa_relationship_kwargs
#             )

#         return InteractionLinkRelationshipWithoutSQLModel



# SimpleInteractionsLinkRelationship : Type[DeclarativeMeta] = cast(
#     Type[DeclarativeMeta],
#     generateInteractionLinkRelationship(
#         withSQLModelBaseClass=False
#     )
# )
# SimpleInteractionLinkRelationship : Type[DeclarativeMeta] = cast(
#     Type[DeclarativeMeta],
#     generateInteractionLinkRelationship(
#         containerRelashionship=False,
#         withSQLModelBaseClass=False
#     )
# )
# SimpleInteractionsLinkRelationshipWithSQLModelBase : Type[SQLModel] = cast(
#     Type[SQLModel],
#     generateInteractionLinkRelationship()
# )
# SimpleInteractionLinkRelationshipWithSQLModelBase : Type[SQLModel] = cast(
#     Type[SQLModel],
#     generateInteractionLinkRelationship(containerRelashionship=False)
# )








