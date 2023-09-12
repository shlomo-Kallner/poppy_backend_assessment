#!/bin/env python3

from fastapi import APIRouter

from poppy_s.lib.models import Medication, MedicationRead

from poppy_s.api.v1.helper_generator import genRouter

def getRouter() -> APIRouter:

    router = genRouter(
        "medication", "medications", "Medication",
        Medication, MedicationRead, MedicationRead, None
    )
    return router