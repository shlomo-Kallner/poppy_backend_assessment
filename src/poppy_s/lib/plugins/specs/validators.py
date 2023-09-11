#!/bin/env python3


from poppy_s.lib.plugins.specs import PluginSpec
from poppy_s.lib.models import Medication
from poppy_s.lib.models import InteractionCreate

@PluginSpec
def search_medication_interactions_by_rxcui(medications: list[Medication]) -> list[InteractionCreate]:
    """
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

    return []