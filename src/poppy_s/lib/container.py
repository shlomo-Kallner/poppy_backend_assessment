#!/bin/env python3

# from contextlib import contextmanager
# from typing import Generator
from pluggy import PluginManager
from fastapi import FastAPI



from poppy_s.config import Configuration

class GeneralCOntainer:
    def __init__(self) -> None:
        self._config : Configuration | None = None
        self._plugins : PluginManager | None = None
        self._app : FastAPI | None = None


    @property
    def config(self) -> Configuration | None:
        return self._config

    @config.setter
    def config(self, config : Configuration | None):
        self._config = config


    @property
    def plugins(self) -> PluginManager | None:
        return self._plugins

    @plugins.setter
    def plugins(self, plugins : PluginManager | None):
        self._plugins = plugins


    @property
    def app(self) -> FastAPI | None:
        return self._app

    @app.setter
    def app(self, app : FastAPI | None):
        self._app = app


globalContainer = GeneralCOntainer()