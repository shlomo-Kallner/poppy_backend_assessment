#!/bin/env python3

from sqlmodel import Session, select, col, and_ #, tuple_, exists, SQLModel

from poppy_s.lib.models import Medication, Interaction, InteractionCreate, InteractionMedicationLink
from poppy_s.lib.container import globalContainer



def find_interactions_by_rxcui(session: Session, medications: list[Medication], loadMore: bool = False) -> list[Interaction]:
    
    res : list[Interaction] = []

    med_to_ids : dict[int, Medication] = {
        m.id : m for m in medications if m.id is not None
    }

    med_ids : list[int] = list(med_to_ids.keys())

    # function to check results..
    def filter_results(tmp_results: list[Interaction]) -> list[Interaction]:
        fRes : list[Interaction] = [] 

        for tdres in tmp_results:
            # it needs to match at least 2 from the med_to_ids dict's keys!
            num : int = 0
            for m in tdres.medications:
                if m.id in med_to_ids:
                    num = num + 1

            if num > 1:
                fRes.append(tdres)

        return fRes

    for med in medications:
        tm_res = filter_results(med.interactions)
        res.extend(tm_res)

    db_stmt = select(Interaction).join(InteractionMedicationLink, isouter=False, full=False).where(
        and_(
            col(InteractionMedicationLink.medication_id).in_(med_ids),
            col(InteractionMedicationLink.interaction_id) == Interaction.id
        )
    )

    tdb_results : list[Interaction] = session.exec(db_stmt).all()
    
    
    db_results: list[Interaction] = filter_results(tdb_results)

    res.extend(db_results)

    if len(db_results) == 0 or loadMore:

        # then check the API

        if globalContainer.plugins is None:
            raise RuntimeError("the plugins have not been loaded and stored in the globalContainer!")

        fetch_results : list[InteractionCreate] = globalContainer.plugins.hook.search_medication_interactions_by_rxcui(
            medications=medications
        )

        for fr in fetch_results:
            if (
                any( 
                    ( 
                        r.warning == fr.warning 
                        and ( rm.rxcui for rm in r.medications ) == tuple(fr.rxcuis)
                        for r in res 
                    ) 
                ) or len(
                    session.exec(
                        select(Interaction).join(InteractionMedicationLink).join(Medication).where(
                            and_(
                                col(Interaction.warning) == fr.warning,
                                col(Interaction.id) == col(InteractionMedicationLink.interaction_id)
                                *( 
                                    and_(
                                        col(InteractionMedicationLink.medication_id) == col(Medication.id),
                                        col(Medication.rxcui) == rxcui
                                    )
                                    for rxcui in fr.rxcuis
                                )
                            )
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



def compile_interactions_warnings(interactions: list[Interaction], asList: bool = True, sep: str = '\n') -> list[str] | str:
    res : list[str] = [
        inter_.warning for inter_ in interactions
    ]

    return res if asList else sep.join(res)