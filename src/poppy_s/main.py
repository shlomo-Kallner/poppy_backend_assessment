#!/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from poppy_s.__version__ import TITLE, VERSION
from poppy_s.api import getRouter

def getApp() -> FastAPI:

    app = FastAPI(
        title=TITLE,
        version=VERSION
    )

    app.include_router(
        getRouter()
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], #temporrary!
    )

    return app


app = getApp()


if __name__ == "__main__":
    from uvicorn import run