#!/bin/env python3

from typing import Optional, Type, TypeVar, TYPE_CHECKING, Any, Sequence, Mapping, cast
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import RelationshipProperty
from sqlalchemy.orm.decl_api import DeclarativeMeta


if TYPE_CHECKING:
    from poppy_s.lib.models.prescriptions import Prescription

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

def generatePrescriptionLinkRelationship(
    *,
    containerRelashionship: bool = True,
    withSQLModelBaseClass: bool = True,
    link_model: Optional[Type[T_PrescriptionLink_TypeVar]] = None,
    back_population_field: Optional[str] = None,
    sa_relationship: Optional[RelationshipProperty] = None,
    sa_relationship_args: Optional[Sequence[Any]] = None,
    sa_relationship_kwargs: Optional[Mapping[str, Any]] = None
) -> Type[SQLModel]|Type[DeclarativeMeta]:

    if withSQLModelBaseClass and containerRelashionship:

        class PrescriptionsLinkRelationshipWithSQLModel(SQLModel):

            prescriptions : list["Prescription"] = Relationship(
                back_populates=back_population_field,
                link_model=link_model,
                sa_relationship=sa_relationship,
                sa_relationship_args=sa_relationship_args,
                sa_relationship_kwargs=sa_relationship_kwargs
            )

        return PrescriptionsLinkRelationshipWithSQLModel
    
    elif not withSQLModelBaseClass and containerRelashionship:

        class PrescriptionsLinkRelationship(DeclarativeMeta):

            prescriptions : list["Prescription"] = Relationship(
                back_populates=back_population_field,
                link_model=link_model,
                sa_relationship=sa_relationship,
                sa_relationship_args=sa_relationship_args,
                sa_relationship_kwargs=sa_relationship_kwargs
            )

        return PrescriptionsLinkRelationship
    
    elif withSQLModelBaseClass and not containerRelashionship:
        
        class PrescriptionLinkRelationshipWithSQLModel(SQLModel):

            prescription : "Prescription" = Relationship(
                back_populates=back_population_field,
                link_model=link_model,
                sa_relationship=sa_relationship,
                sa_relationship_args=sa_relationship_args,
                sa_relationship_kwargs=sa_relationship_kwargs
            )

        return PrescriptionLinkRelationshipWithSQLModel
    
    else:

        class PrescriptionLinkRelationship(DeclarativeMeta):

            prescription : "Prescription" = Relationship(
                back_populates=back_population_field,
                link_model=link_model,
                sa_relationship=sa_relationship,
                sa_relationship_args=sa_relationship_args,
                sa_relationship_kwargs=sa_relationship_kwargs
            )

        return PrescriptionLinkRelationship

SimplePrescriptionsLinkRelationship : Type[DeclarativeMeta] = cast(
    Type[DeclarativeMeta],
    generatePrescriptionLinkRelationship(withSQLModelBaseClass=False)
)
SimplePrescriptionLinkRelationship : Type[DeclarativeMeta] = cast(
    Type[DeclarativeMeta],
    generatePrescriptionLinkRelationship(
        containerRelashionship=False,
        withSQLModelBaseClass=False
    )
)
SimplePrescriptionsLinkRelationshipWithSQLModelBase : Type[SQLModel] = cast(
    Type[SQLModel],
    generatePrescriptionLinkRelationship()
)
SimplePrescriptionLinkRelationshipWithSQLModelBase : Type[SQLModel] = cast(
    Type[SQLModel],
    generatePrescriptionLinkRelationship(containerRelashionship=False)
)
