#!/bin/env python3

from sqlmodel import Session, select, col #, exists, SQLModel

from poppy_s.lib.models import MedicationCreate, Medication
from poppy_s.lib.container import globalContainer
from poppy_s.lib.helpers.plugin_helpers.exception import check_if_plugins_loaded
from poppy_s.lib.helpers.plugin_helpers.utils import pmTypeHelper


def find_medication_by_name(session: Session, name: str, num: int = 100, loadMore: bool = False) -> list[Medication]:

    res : list[Medication] = []

    # first check the DB

    db_stmt = select(Medication).where(
        Medication.name == name,
        col(Medication.name).ilike(name)
    )

    db_results = session.exec(db_stmt).all()

    res.extend(db_results)

    if len(db_results) == 0 or loadMore:

        # then check the API

        check_if_plugins_loaded()

        fetch_results : list[MedicationCreate] = pmTypeHelper(
            globalContainer.plugins
        ).hook.search_medication_by_name(
            name=name, num=num
        )

        for fr in fetch_results:
            if (
                any( 
                    ( 
                        r.rxcui == fr.rxcui 
                        # and r.name == fr.name and r.description == fr.description
                        for r in res 
                    ) 
                ) or len(
                    session.exec(
                        select(Medication).where(
                            Medication.rxcui == fr.rxcui
                        )
                    ).all()
                ) > 0
            ):
                # already exists, ignore
                pass
                
            tres = Medication.from_orm(fr)
            session.add(tres)
            session.commit()
            session.refresh(tres)

            res.append(tres)

    return res
