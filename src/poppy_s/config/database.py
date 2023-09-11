#!/bin/env python3

from typing import Union, Literal
from sqlmodel import SQLModel, Field, create_engine
from pydantic import BaseSettings, PostgresDsn
from pydantic.networks import MultiHostDsn


class SQLiteDsn(MultiHostDsn):
    allowed_schemes = {
        "sqlite",
        "sqlite+pysqlite"
    }
    host_required = False


class DatabaseSettings(BaseSettings):
    db : Union[PostgresDsn, SQLiteDsn, Literal['sqlite://']] = 'sqlite://' # noqa
    create_tables : bool = True

