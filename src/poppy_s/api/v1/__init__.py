#!/bin/env python3

from fastapi import APIRouter

from poppy_s.api.v1.doctors import getRouter as getDoctorsRouter
from poppy_s.api.v1.patients import getRouter as getPatientsRouter

def getRouter() -> APIRouter:

    router = APIRouter(prefix="/v1", tags=["api", "api/v1"])

    router.include_router(
        getDoctorsRouter()
    )

    router.include_router(
        getPatientsRouter()
    )


    return router