#!/bin/env python3

from typing import Union, Literal
from pydantic import BaseSettings
from pydantic.networks import AnyHttpUrl


class AppSettings(BaseSettings):
    debug: bool = False
    allow_origins: list[Union[AnyHttpUrl, Literal["*"], Literal["localhost"]]] = ["*", "localhost"]

