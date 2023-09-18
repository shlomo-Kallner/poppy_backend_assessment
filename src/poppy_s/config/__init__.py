#!/bin/env python3

from typing import Union, Literal, Type, Optional, Any
from pathlib import Path
from importlib.abc import Traversable
from pydantic import BaseSettings, BaseModel
from pydantic.typing import StrPath
from pydantic.env_settings import BaseSettings, DotenvType
from pluggy import PluginManager

from poppy_s.config.app import AppSettings
from poppy_s.config.database import DatabaseSettings
from poppy_s.__version__ import NAME

class Configuration(BaseSettings):
    app: AppSettings = AppSettings()
    database: DatabaseSettings = DatabaseSettings()

    plugins: dict[str, BaseSettings] = {}

    class Config:
        # env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = "__"
        env_prefix = f"{NAME.upper()}__"

    
    def __init__(
        self, 
        *, 
        _env_file: Optional[DotenvType] = ..., 
        _env_file_encoding: Optional[str] = None, 
        _secrets_dir: Optional[StrPath] = None, 
        **values: Any
    ) -> None:
        super().__init__(
            _env_file, 
            _env_file_encoding, 
            "__", 
            _secrets_dir, 
            **values
        )


def load_config(
    plugins: PluginManager,
    env_file_path: DotenvType = '.env'
) -> Configuration:
    config = Configuration(
        # _env_file=env_file_path
        _env_file=env_file_path
    )

    return config
