#!/bin/env python3

# from typing import Optional, TYPE_CHECKING
# from pydantic import conint
from sqlmodel import SQLModel, Field

# from poppy_s.lib.models.base import (
#     MedicationLinkBaseAsPrimaryKey, 
#     PrescriptionLinkBaseAsPrimaryKey,
# )

# if TYPE_CHECKING:
#     from poppy_s.lib.models.prescriptions import Prescription
#     from poppy_s.lib.models.medications import Medication, MedicationBase

class PrescriptionValidationErrorsBase(SQLModel):
    warning: str = Field(
        min_length=1 #, index=True, unique=True
    )
    rxcuis: list[int]

# class PrescriptionValidationErrorsMedicationLinkBase(MedicationLinkBaseAsPrimaryKey):
#     pass

# class PrescriptionValidationErrorsPrescriptionLinkBase(PrescriptionLinkBaseAsPrimaryKey):
#     pass


