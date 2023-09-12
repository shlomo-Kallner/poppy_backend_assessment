#!/bin/env python3


from poppy_s.lib.plugins.specs import PluginSpec
from poppy_s.lib.models import MedicationCreate

@PluginSpec
def search_medication_by_name(name: str, num: int) -> list[MedicationCreate]:
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
    return []