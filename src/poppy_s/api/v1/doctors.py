#!/bin/env python3

from fastapi import APIRouter

from poppy_s.lib.models import Doctor, DoctorCreate, DoctorRead

from poppy_s.api.v1.helper_generator import genRouter

def getRouter() -> APIRouter:

    router = genRouter(
        "doctor", "doctors", "Doctor",
        Doctor, DoctorRead, DoctorRead, DoctorCreate
    )

    
    return router