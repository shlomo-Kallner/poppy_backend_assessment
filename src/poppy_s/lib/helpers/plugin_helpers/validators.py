#!/bin/env python3

from sqlmodel import Session, select, col, and_ #, tuple_, exists, SQLModel

from poppy_s.lib.models import PrescriptionValidationErrorsBase
from poppy_s.lib.container import globalContainer





def compile_validator_s_warnings(interactions: list[PrescriptionValidationErrorsBase], asList: bool = True, sep: str = '\n') -> list[str] | str:
    res : list[str] = [
        inter_.warning for inter_ in interactions
    ]

    return res if asList else sep.join(res)