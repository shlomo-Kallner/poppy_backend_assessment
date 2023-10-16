#!/bin/env python3


from itertools import chain

from sqlmodel import Session, select, col, and_ #, tuple_, exists, SQLModel

from poppy_s.lib.models import PrescriptionValidationErrorsBase, Prescription
from poppy_s.lib.container import globalContainer
from poppy_s.lib.helpers.plugin_helpers.exception import check_if_plugins_loaded
from poppy_s.lib.helpers.plugin_helpers.utils import pmTypeHelper




def compile_validator_s_warnings(interactions: list[PrescriptionValidationErrorsBase], asList: bool = True, sep: str = '\n') -> list[str] | str:
    res : list[str] = [
        inter_.warning for inter_ in interactions
    ]

    return res if asList else sep.join(res)

def validate_prescription(session: Session, prescription: Prescription, loadMore: bool = False) -> list[PrescriptionValidationErrorsBase]:

    check_if_plugins_loaded()

    res = pmTypeHelper(
        globalContainer.plugins
    ).hook.validate_medications_list(
        session=session,
        prescription=prescription,
        loadMore=loadMore
    )

    tRes = list(chain.from_iterable(res))

    return tRes