#!/bin/env python3

from sqlmodel import Session, select, col #, SQLModel

from poppy_s.lib.models import MedicationCreate, Medication
from poppy_s.lib.container import globalContainer


def find_medication_by_name(name: str, session: Session, loadMore: bool = False) -> list[Medication]:

    res : list[Medication] = []

    # first check the DB

    db_stmt = select(Medication).where(
        Medication.name == name,
        col(Medication.name).ilike(name)
    )

    db_results = session.exec(db_stmt).all()

    if len(db_results) == 0 or loadMore:

        if globalContainer.plugins is not None:
            fetch_results = globalContainer.plugins.hook.search_medication_by_name(
                name=name
            )



    return res
