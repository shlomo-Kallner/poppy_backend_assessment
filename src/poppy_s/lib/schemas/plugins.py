#!/bin/env python3

from typing import List, Optional, Type, Callable, Sequence, Union, Any, Dict
from enum import Enum
from inspect import signature, Signature, Parameter

from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from fastapi.params import Depends
from fastapi.routing import APIRoute
from fastapi.datastructures import Default
from fastapi.utils import generate_unique_id
from starlette.routing import BaseRoute
from pydantic import BaseModel


class RouterPluginSchema(BaseModel):
    router: APIRouter | Callable[...,APIRouter]
    prefix: str = ""
    tags: Optional[List[Union[str, Enum]]] = None
    dependencies: Optional[Sequence[Depends]] = None
    default_response_class: Type[Response] = Default(JSONResponse)
    responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None
    callbacks: Optional[List[BaseRoute]] = None
    deprecated: Optional[bool] = None
    include_in_schema: bool = True
    generate_unique_id_function: Callable[[APIRoute], str] = Default(
        generate_unique_id
    )