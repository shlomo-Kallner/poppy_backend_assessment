#!/bin/env python3

from fastapi import APIRouter


def getRouter() -> APIRouter:
    
    from poppy_s.api.v1 import getRouter as getRouterV1

    router = APIRouter(prefix="/api", tags=["api"])

    router.include_router(
        getRouterV1()
    )


    return router