#!/bin/env python3

from typing import Union, Literal
from pydantic import BaseSettings, Field, BaseModel
from pydantic.networks import AnyHttpUrl

from poppy_s.__version__ import NAME

class AppSettings(BaseModel):
    DEBUG: bool = False
    ALLOWED_ORIGINS: list[Union[AnyHttpUrl, Literal["*"], Literal["localhost"]]] = ["*", "localhost"]

