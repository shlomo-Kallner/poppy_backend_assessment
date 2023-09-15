#!/bin/env python3

from fastapi import APIRouter

from poppy_s.api.v1.doctors import getRouter as getDoctorsRouter
from poppy_s.api.v1.patients import getRouter as getPatientsRouter
from poppy_s.api.v1.medications import getRouter as getMedicationsRouter
from poppy_s.api.v1.prescriptions import getRouter as getPrescriptionsRouter
from poppy_s.api.v1.plugins import getRouter as getPluginsRouter

def getRouter() -> APIRouter:

    router = APIRouter(prefix="/v1", tags=["api", "api/v1"])

    router.include_router(
        getDoctorsRouter()
    )

    router.include_router(
        getPatientsRouter()
    )

    router.include_router(
        getMedicationsRouter()
    )

    router.include_router(
        getPrescriptionsRouter()
    )

    router.include_router(
        getPluginsRouter()
    )


    return router