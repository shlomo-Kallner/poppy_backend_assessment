#!/bin/env python3

from typing import TypeVar
from sqlmodel import SQLModel


T_SQLModel_TypeVar = TypeVar("T_SQLModel_TypeVar", bound=SQLModel, covariant=True)
