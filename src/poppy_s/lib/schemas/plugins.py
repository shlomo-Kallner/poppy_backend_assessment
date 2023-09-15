#!/bin/env python3

from typing import List, Optional, Type, TypeVar, Callable, Sequence, Union, Any

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse

from fastapi.routing import APIRoute, generate_unique_id, Default
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