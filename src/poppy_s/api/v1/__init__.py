#!/bin/env python3

from fastapi import APIRouter


def getRouter() -> APIRouter:

    router = APIRouter(prefix="/v1", tags=["api", "api/v1"])


    return router