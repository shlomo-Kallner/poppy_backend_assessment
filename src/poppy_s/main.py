#!/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from poppy_s.__version__ import TITLE, VERSION
from poppy_s.api import getRouter
from poppy_s.lib.database import database
from poppy_s.lib.container import globalContainer
from poppy_s.config import Configuration
from poppy_s.lib.plugins import getPlugins, PluginManager

def getApp(config: Configuration, plugins: PluginManager) -> FastAPI:

    app = FastAPI(
        title=TITLE,
        version=VERSION
    )

    @app.on_event("startup")
    def on_startup():
        database.createDBEngine(config)
        database.create_db_and_tables()

    app.include_router(
        getRouter()
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.app.ALLOWED_ORIGINS,
        allow_methods=["*"]
        # ,
        # allow_credentials=True
    )

    globalContainer.config = config
    globalContainer.plugins = plugins


    return app

configuration = Configuration(
    # _env_file
)
plugins = getPlugins()
app = getApp(configuration, plugins)


if __name__ == "__main__":
    from uvicorn import run

    run(app=app)