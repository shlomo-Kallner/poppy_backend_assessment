#!/bin/env python3

from typing import Optional, Type, TypeVar, TYPE_CHECKING, Sequence, Any, Mapping, cast
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import RelationshipProperty
from sqlalchemy.orm.decl_api import DeclarativeMeta

from poppy_s.lib.models.base.base import T_SQLModel_TypeVar


if TYPE_CHECKING:
    from poppy_s.lib.models.medications import Medication

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

def generateMedicationLinkRelationship(
    *,
    containerRelashionship: bool = True,
    withSQLModelBaseClass: bool = True,
    link_model: Optional[Type[T_MedicationLink_TypeVar]] = None,
    back_population_field: Optional[str] = None,
    sa_relationship: Optional[RelationshipProperty] = None,
    sa_relationship_args: Optional[Sequence[Any]] = None,
    sa_relationship_kwargs: Optional[Mapping[str, Any]] = None
) -> Type[SQLModel]|Type[DeclarativeMeta]:

    if withSQLModelBaseClass and containerRelashionship:

        class MedicationListLinkRelationshipWithSQLModel(SQLModel):

            medications : list["Medication"] = Relationship(
                back_populates=back_population_field,
                link_model=link_model,
                sa_relationship=sa_relationship,
                sa_relationship_args=sa_relationship_args,
                sa_relationship_kwargs=sa_relationship_kwargs
            )

        return MedicationListLinkRelationshipWithSQLModel

    elif not withSQLModelBaseClass and containerRelashionship:

        class MedicationListLinkRelationshipWithoutSQLModel(DeclarativeMeta):

            medications : list["Medication"] = Relationship(
                back_populates=back_population_field,
                link_model=link_model,
                sa_relationship=sa_relationship,
                sa_relationship_args=sa_relationship_args,
                sa_relationship_kwargs=sa_relationship_kwargs
            )

        return MedicationListLinkRelationshipWithoutSQLModel

    elif withSQLModelBaseClass and not containerRelashionship:

        class MedicationLinkRelationshipWithSQLModel(SQLModel):

            medication : "Medication" = Relationship(
                back_populates=back_population_field,
                link_model=link_model,
                sa_relationship=sa_relationship,
                sa_relationship_args=sa_relationship_args,
                sa_relationship_kwargs=sa_relationship_kwargs
            )

        return MedicationLinkRelationshipWithSQLModel
    
    else:

        class MedicationLinkRelationshipWithoutSQLModel(DeclarativeMeta):

            medication : "Medication" = Relationship(
                back_populates=back_population_field,
                link_model=link_model,
                sa_relationship=sa_relationship,
                sa_relationship_args=sa_relationship_args,
                sa_relationship_kwargs=sa_relationship_kwargs
            )

        return MedicationLinkRelationshipWithoutSQLModel



SimpleMedicationsLinkRelationship : Type[DeclarativeMeta] = cast(
    Type[DeclarativeMeta],
    generateMedicationLinkRelationship(
        withSQLModelBaseClass=False
    )
)
SimpleMedicationLinkRelationship : Type[DeclarativeMeta] = cast(
    Type[DeclarativeMeta],
    generateMedicationLinkRelationship(
        containerRelashionship=False,
        withSQLModelBaseClass=False
    )
)
SimpleMedicationsLinkRelationshipWithSQLModelBase : Type[SQLModel] = cast(
    Type[SQLModel],
    generateMedicationLinkRelationship()
)
SimpleMedicationLinkRelationshipWithSQLModelBase : Type[SQLModel] = cast(
    Type[SQLModel],
    generateMedicationLinkRelationship(containerRelashionship=False)
)