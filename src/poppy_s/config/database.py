#!/bin/env python3

from typing import Union, Literal
from pydantic import BaseModel, PostgresDsn
from pydantic.networks import MultiHostDsn


class SQLiteDsn(MultiHostDsn):
    allowed_schemes = {
        "sqlite",
        "sqlite+pysqlite"
    }
    host_required = False


class DatabaseSettings(BaseModel):
    DB_URL : Union[PostgresDsn, SQLiteDsn, Literal['sqlite://']] = 'sqlite://'
    # create_tables : bool = True

