#!/bin/env python3

from typing import Generator
# from urllib.parse import quote_plus
from datetime import datetime, timezone
from warnings import warn

from requests import Session

from poppy_s.lib.plugins import PluginImpl
from poppy_s.lib.models import Medication
from poppy_s.lib.models import InteractionCreate

@PluginImpl(wrapper=True, specname="search_medication_interactions_by_rxcui")
def search_medication_interactions_by_rxcui_results_flattener_wrapper(
    medications: list[Medication]
) -> Generator[None, list[list[InteractionCreate]], list[InteractionCreate]]:
    """
        search_medication_interactions_by_rxcui_results_flattener_wrapper
        A wrapper to flatten the retunred list of Models.
        Should be called within a DB Session!

    Spec Docs:
        search_medication_interactions_by_rxcui 
        
        Given a list Medications, search for 
        Interactions of any combo of them.

        Parameters
        ----------
        medications : list[Medication]
            _description_

        Returns
        -------
        list[InteractionCreate]
            _description_
    """     

    res : list[InteractionCreate] = []

    tmp : list[list[InteractionCreate]] = yield

    for result in tmp:
        res.extend( 
            ( InteractionCreate.from_orm(rv) if not isinstance(rv, InteractionCreate) else rv for rv in result ) 
        )

    return res






#############################################
##
##          WARNING!!!!!
##
## Upcoming Changes On or About January 2, 2024:
##
## The Drug-Drug Interaction API will be discontinued on or about January 2, 2024. 
## RxNav's Interactions tab will also be removed.
##
##

@PluginImpl
def search_medication_interactions_by_rxcui(medications: list[Medication]) -> list[InteractionCreate]:
    """
    search_medication_interactions_by_rxcui 
    
    Given a list Medications, search for 
    Interactions of any combo of them.

    Uses the `findInteractionsFromList` API 
    <https://lhncbc.nlm.nih.gov/RxNav/APIs/api-Interaction.findInteractionsFromList.html>
    from the NIH Drug Interaction API 
    <https://lhncbc.nlm.nih.gov/RxNav/APIs/InteractionAPIs.html>.


    #############################################
    ##
    ##          WARNING!!!!!
    ##
    ## Upcoming Changes On or About January 2, 2024:
    ##
    ## The Drug-Drug Interaction API will be discontinued on or about January 2, 2024. 
    ## RxNav's Interactions tab will also be removed.
    ##
    #############################################


    Parameters
    ----------
    medications : list[Medication]
        _description_

    Returns
    -------
    list[InteractionCreate]
        _description_
    """    

    res : list[InteractionCreate] = []

    rxcuis_tmp = [ med.rxcui for med in medications ]

    rxcuis_nx = " ".join( [ str(ri) for ri in rxcuis_tmp ] )

    ## No need to quote it ourselves, request will do it for us!
    # rxcuis = quote_plus(rxcuis_nx) 


    now = datetime.now(timezone.utc)

    deprecation_dt = datetime(2024, 1, 2, tzinfo=timezone.utc)

    if (
        ( td := deprecation_dt - now).days > 0 
    ):
        
        if td.days > 120:
            warn(
                "The Drug-Drug Interaction API will be discontinued on or about January 2, 2024.",
                category=PendingDeprecationWarning
            )
        elif td.days > 60:
            warn(
                "The Drug-Drug Interaction API will be discontinued on or about January 2, 2024.",
                category=DeprecationWarning
            )
        else:
            warn(
                "The Drug-Drug Interaction API will be discontinued on or about January 2, 2024.",
                category=FutureWarning
            )

    else:
        raise RuntimeError("The Drug-Drug Interaction API has been Discontinued!!")


    with Session() as s:
        params = {
            "rxcuis": rxcuis_nx,
        }
        resp = s.get(
            'https://rxnav.nlm.nih.gov/REST/interaction/list.json',
            params=params
        )
        resp.raise_for_status()

        data = resp.json()

        data2 = data["fullInteractionTypeGroup"]
        
        for data3 in data2:

            data4 = data3["fullInteractionType"]

            for d5_1 in data4:
                data5 = d5_1["interactionPair"]

                for data6 in data5:

                    data7 = data6["interactionConcept"]

                    data8 = [
                        int(item["minConceptItem"]["rxcui"]) for item in data7
                    ]
                    res.append(
                        InteractionCreate(
                            warning=data6["description"],
                            rxcuis=data8
                        )
                    )

    return res