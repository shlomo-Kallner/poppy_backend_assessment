#!/bin/env python3

from typing import Union, Literal
from pydantic import BaseSettings, BaseModel

from poppy_s.config.app import AppSettings
from poppy_s.config.database import DatabaseSettings
from poppy_s.__version__ import NAME

class Configuration(BaseSettings):
    app: AppSettings = AppSettings()
    database: DatabaseSettings = DatabaseSettings()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = "__"
        env_prefix = f"{NAME.upper()}"
