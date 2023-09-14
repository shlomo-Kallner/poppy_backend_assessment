#!/bin/env python3


from poppy_s.lib.plugins.specs import PluginSpec
from poppy_s.lib.models import Medication, InteractionCreate, PrescriptionValidationErrorsBase

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



@PluginSpec
def validate_medications_list(medications: list[Medication]) -> list[PrescriptionValidationErrorsBase]:

    """
     _summary_

    Returns
    -------
    list[PrescriptionValidationErrorsBase]
        A list of already created and databased instances of the 
        Plugin's SubClass of `PrescriptionValidationErrorsBase`
    """
    return []