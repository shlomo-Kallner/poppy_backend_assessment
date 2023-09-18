#!/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from poppy_s.__version__ import TITLE, VERSION
from poppy_s.api import getRouter
from poppy_s.lib.database import database
from poppy_s.lib.container import globalContainer
from poppy_s.config import Configuration, load_config
from poppy_s.lib.plugins import getPlugins, PluginManager

def getApp(config: Configuration, plugins: PluginManager) -> FastAPI:

    globalContainer.config = config
    globalContainer.plugins = plugins

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
    globalContainer.app = app


    return app

plugins = getPlugins()
configuration : Configuration = load_config(
    plugins=plugins
    # _env_file
)
app = getApp(configuration, plugins)


def run_main():
    from uvicorn import run
    from typer import Typer, Option, secho
    import debugpy
    from pathlib import Path
    from os import PathLike
    from pydantic.networks import IPvAnyAddress
    from typing import Optional
    # from ipaddress import IPv4Address

    typer_app = Typer(
        name="poppy_s Dev Server",

    )

    @typer_app.command()
    def main(
        debug : bool = False,
        reload : bool = False,
        server_host : str = "127.0.0.1",
        debug_host: str = "127.0.0.1",
        server_port : int = 8080,
        debug_port : int = 5678,
        workers: int = 1,
        debug_log_dir : Optional[Path] = Option(
            None,
            dir_okay=True, 
            file_okay=False
        )
    ):

        _server_host = IPvAnyAddress.validate(server_host)
        _debug_host = IPvAnyAddress.validate(debug_host)

        if debug:
            if debug_log_dir is not None and (_log_dir := Path(debug_log_dir).resolve() ).exists():
                debugpy.log_to(str(_log_dir))
            debugpy.listen((str(_debug_host), debug_port))
            secho("Awaiting Debugger Connection..", blink=True, fg="red")
            debugpy.wait_for_client()

        run(
            app="poppy_s.main:app",
            reload=reload,
            host=str(_server_host),
            port=server_port,
            workers=workers
        )

    typer_app()

if __name__ == "__main__":
    run_main()