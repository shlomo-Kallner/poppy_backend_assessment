#!/bin/env python3

from fastapi import APIRouter

from poppy_s.lib.models import Patient, PatientRead, PatientCreate

from poppy_s.lib.helpers.routes_helpers.helper_generator import genRouter

def getRouter() -> APIRouter:

    router = genRouter(
        "patient", "patients", "Patient",
        Patient, PatientRead, PatientRead, PatientCreate
    )
    return router