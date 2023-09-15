#!/bin/env python3
from typing import cast

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session #, select

from datetime import datetime, timezone

from poppy_s.lib.database import database



def getRouter(
) -> APIRouter:

    router = APIRouter(
        prefix=f"/plugins", 
        tags=[
            "api", "api/v1", 
            "api/v1/plugin", 
            "plugins"
        ]
    )


    # TODO: Insert call to retrieve the plugin Routers here!
    # TODO: Insert loop to include the plugin Routers here!


    return router



