#!/bin/env python3


from itertools import chain

from sqlmodel import Session, select, col, and_ #, tuple_, exists, SQLModel

from poppy_s.lib.models import PrescriptionValidationErrorsBase, Prescription
from poppy_s.lib.container import globalContainer





def compile_validator_s_warnings(interactions: list[PrescriptionValidationErrorsBase], asList: bool = True, sep: str = '\n') -> list[str] | str:
    res : list[str] = [
        inter_.warning for inter_ in interactions
    ]

    return res if asList else sep.join(res)

def validate_prescription(session: Session, prescription: Prescription, loadMore: bool = False) -> list[PrescriptionValidationErrorsBase]:

    if globalContainer.plugins is None:
        raise RuntimeError("the plugins have not been loaded and stored in the globalContainer!")

    res = globalContainer.plugins.hook.validate_medications_list(
        session=session,
        prescription=prescription,
        loadMore=loadMore
    )

    tRes = list(chain.from_iterable(res))

    return tRes