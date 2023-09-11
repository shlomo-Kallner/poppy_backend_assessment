#!/bin/env python3


from poppy_s.lib.plugins import PluginImpl
from poppy_s.lib.models import MedicationCreate
from typing import Generator
from requests import Session


@PluginImpl(wrapper=True, specname="search_medication_by_name")
def search_medication_by_name_base_wrapper(name: str) -> Generator[None, list[list[MedicationCreate]], list[MedicationCreate]]:
    """
        search_medication_by_name_base_wrapper
        A wrapper to flatten the retunred list of Models.
        Should be called within a DB Session!

    Spec Docs:
        search_medication_by_name 
        
        Given a Medication's name search for it's details.
        Can return more than one if either many use the name or 
        if the function was given a partial name.

        Parameters
        ----------
        name : str
            the Medication's name

        Returns
        -------
        list[Medication]
            the List of Medication Details
    """    

    res : list[MedicationCreate] = []

    tmp : list[list[MedicationCreate]] = yield

    for result in tmp:
        res.extend(result)

    return res

@PluginImpl
def search_medication_by_name(name: str) -> list[MedicationCreate]:
    """
        search_medication_by_name 
        
        Given a Medication's name search for it's details.
        Can return more than one if either many use the name or 
        if the function was given a partial name.

        Parameters
        ----------
        name : str
            the Medication's name

        Returns
        -------
        list[MedicationCreate]
            the List of Medication Details
    """    
    res : list[MedicationCreate] = []
    with Session() as s:
        params = {
            "terms": name,
            # "df": "DISPLAY_NAME,DISPLAY_NAME_SYNONYM",
            "df": "DISPLAY_NAME_SYNONYM",
            # "ef": "STRENGTHS_AND_FORMS,RXCUIS,SXDG_RXCUI"
            "ef": "STRENGTHS_AND_FORMS,RXCUIS"
        }
        resp = s.get(
            'https://clinicaltables.nlm.nih.gov/api/rxterms/v3/search',
            params=params
        )
        resp.raise_for_status()

        rj = resp.json()

        extras = { k: [(k, v1) for v1 in v] for k, v in rj[2].items() }

        ex_zipped = tuple(zip(*extras.values()))

        for name, display, extra in zip(
            rj[1], rj[3], ex_zipped, 
        ):
            print(f"{name=}\n{display=}\n{extra=}\n\n")
            
            nMed = 


            pass

    return res