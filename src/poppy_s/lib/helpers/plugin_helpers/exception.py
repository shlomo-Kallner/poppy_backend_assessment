#!/bin/env python3

from typing_extensions import Never
from pluggy import PluginManager
from poppy_s.lib.container import globalContainer


def throw_plugins_not_loaded() -> Never:
    raise RuntimeError("the plugins have not been loaded and stored in the globalContainer!")

def check_if_plugins_loaded() -> None | Never:
    """
    check_if_plugins_loaded 
    
    Check if the plugins are Loaded, is not, 
    Raise a RuntimeError

    Returns
    -------
    None | Never
        _description_
    """    
    if globalContainer.plugins is None or not isinstance(globalContainer.plugins, PluginManager):
        throw_plugins_not_loaded()
    return 