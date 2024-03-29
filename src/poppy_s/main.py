#!/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from os import getcwd
from pathlib import Path

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
    plugins=plugins,
    env_file_path=Path(getcwd(), '.env')
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
        """
        main 
        The "inner", "actual" CLI Main Function, wrapped in a Typer Command.

        Parameters
        ----------
        debug : bool, optional
            If to debug the project, 
            enables use of 'debugpy' to connect to VSCode, 
            by default False
        reload : bool, optional
            Whether to enable "uvicorn" 
            to reload on file changes, 
            by default False
        server_host : str, optional
            The Host IP Address for "uvicorn", 
            by default "127.0.0.1"
        debug_host : str, optional
            The Host IP Address for "debugpy", 
            by default "127.0.0.1"
        server_port : int, optional
            The Host IP Port for "uvicorn", 
            by default 8080
        debug_port : int, optional
            The Host IP Port for "debugpy", 
            by default 5678
        workers : int, optional
            The number of Worker Processes "uvicorn" should use, 
            by default 1
        debug_log_dir : Optional[Path], optional
            An Optional Directory Path for "debugpy" 
            to write log files into, if a Path or str is given, 
            by default None
        """        
        _server_host = IPvAnyAddress.validate(server_host)
        _debug_host = IPvAnyAddress.validate(debug_host)

        if debug:
            if (
                debug_log_dir is not None and 
                (_log_dir := Path(debug_log_dir).resolve() ).exists() and
                _log_dir.is_dir()
            ):
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