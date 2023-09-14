#!/bin/env python3

from sqlmodel import Session, select, col, and_ #, tuple_, exists, SQLModel

from poppy_s.lib.models import Medication, Interaction, InteractionCreate, InteractionMedicationLink
from poppy_s.lib.container import globalContainer



def find_interactions_by_rxcui(session: Session, medications: list[Medication], loadMore: bool = False) -> list[Interaction]:
    
    res : list[Interaction] = []

    med_to_ids : dict[int, Medication] = {
        m.id : m for m in medications if m.id is not None
    }
    rxcui_to_med: dict[int, Medication] = {
        m.rxcui : m for m in medications
    }

    med_ids : list[int] = list(med_to_ids.keys())

    # function to check results..

    def check_interaction_results(tmp_result: Interaction) -> bool:
        # it needs to match at least 2 from the med_to_ids dict's keys!
        num : int = 0
        for m in tmp_result.medications:
            if m.id in med_to_ids:
                num = num + 1

        return num > 1


    def filter_interaction_results(tmp_results: list[Interaction]) -> list[Interaction]:
        fRes : list[Interaction] = [] 

        for tdres in tmp_results:
            if check_interaction_results(tdres):
                fRes.append(tdres)

        return fRes

    # check via SQLModel Relationships..

    for med in medications:
        tm_res = filter_interaction_results(med.interactions)
        res.extend(tm_res)

    db_stmt = select(Interaction).join(
        InteractionMedicationLink, 
        and_(
            col(InteractionMedicationLink.interaction_id) == Interaction.id,
            col(InteractionMedicationLink.medication_id).in_(med_ids)
        )
        # ,
        # isouter=False, full=False
    ).where(
        col(Interaction.id).not_in([ r.id for r in res ])
    )

    tdb_results : list[Interaction] = session.exec(db_stmt).all()
    
    
    db_results: list[Interaction] = filter_interaction_results(tdb_results)

    res.extend(db_results)

    if len(db_results) == 0 or loadMore:

        def filter_existing_interaction_create_results(
            interCrt: InteractionCreate,
            interactions: list[Interaction]
        ) -> bool: 

            bol1 = any( 
                ( 
                    r.warning == interCrt.warning 
                    and ( rm.rxcui for rm in r.medications ) == tuple(interCrt.rxcuis)
                    for r in interactions 
                ) 
            )

            return bol1 

        def filter_non_selected_interaction_create_results(
            interCrt: InteractionCreate,
            existing_interactions: list[Interaction]
        ) -> tuple[bool, list[Interaction]]: 

            # bol1 = filter_existing_interaction_create_results(
            #     interCrt=interCrt,
            #     interactions=existing_interactions
            # )

            # db_stmt = select(Interaction).join(InteractionMedicationLink).join(Medication).where(
            #     and_(
            #         col(Interaction.id).not_in([ei.id for ei in existing_interactions]),
            #         col(Interaction.warning) == interCrt.warning,
            #         and_(
            #             col(Interaction.id) == col(InteractionMedicationLink.interaction_id),
            #             *( 
            #                 and_(
            #                     col(InteractionMedicationLink.medication_id) == col(Medication.id),
            #                     col(Medication.rxcui) == rxcui
            #                 )
            #                 for rxcui in interCrt.rxcuis
            #             )
            #         )
            #     )
            # )

            med_db_sq = select(Medication).where(col(Medication.rxcui).in_(interCrt.rxcuis) ).subquery()

            intactMedLink_sq = select(InteractionMedicationLink).join(
                med_db_sq, InteractionMedicationLink.medication_id == med_db_sq.c.id
            ).subquery()

            db_stmt = select(Interaction).join(
                intactMedLink_sq, Interaction.id == intactMedLink_sq.c.interaction_id
            ).where(
                and_(
                    col(Interaction.id).not_in([ei.id for ei in existing_interactions]),
                    col(Interaction.warning) == interCrt.warning,
                )
            )

            filt_res = session.exec(db_stmt).all()

            sub_filt = filter_interaction_results(filt_res)

            bol1 = len(filt_res) > 0 or len(sub_filt) > 0


            return bol1, filt_res

        # then check the API

        if globalContainer.plugins is None:
            raise RuntimeError("the plugins have not been loaded and stored in the globalContainer!")

        fetch_results : list[InteractionCreate] = globalContainer.plugins.hook.search_medication_interactions_by_rxcui(
            medications=medications
        )

        for fr in fetch_results:
            bol, non_selected_interactions = filter_non_selected_interaction_create_results(fr, res)
            if (
                filter_existing_interaction_create_results(fr, res) or 
                bol
            ):
                # already exists, ignore
                pass
                
            # tres = Interaction(warning=fr.warning)
            tres = Interaction.from_orm(fr)

            session.add(tres)
            session.commit()
            session.refresh(tres)
            
            # TODO: Cache the unused RXCUIs for future requests!!
            ## for now they are stored on the Interaction Object.
            # unused_rxcui = []

            for rxcui in fr.rxcuis:
                if rxcui in rxcui_to_med:
                    tres.medications.append(rxcui_to_med[rxcui])
                # else:
                #     unused_rxcui.append(rxcui)

            if check_interaction_results(tres):
                res.append(tres)


    return res



# def compile_interactions_warnings(interactions: list[Interaction], asList: bool = True, sep: str = '\n') -> list[str] | str:
#     res : list[str] = [
#         inter_.warning for inter_ in interactions
#     ]

#     return res if asList else sep.join(res)