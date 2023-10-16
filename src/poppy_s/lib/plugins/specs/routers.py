#!/bin/env python3

from typing import Union
from poppy_s.lib.plugins.specs import PluginSpec
from poppy_s.lib.schemas.plugins import APIRouter, RouterPluginSchema

@PluginSpec
def add_plugin_router() -> Union[APIRouter, RouterPluginSchema]: #type: ignore
    """
    add_plugin_router 

    Register additional Routes to add to the Application

    Returns
    -------
    Union[APIRouter, RouterPluginSchema]
        The Configured APIRouter or Router Definition
        to include under the "plugins" routes
    """    
    pass