#!/bin/env python3

from pluggy import HookimplMarker, PluginManager

from poppy_s.__version__ import NAME
from poppy_s.lib.plugins.specs import nih_data, validators


PluginImpl = HookimplMarker(NAME)

def getPlugins() -> PluginManager:
    pm = PluginManager(NAME)

    # TODO: Add tracing and hook call monitoring!!

    pm.add_hookspecs(nih_data)
    pm.add_hookspecs(validators)

    pm.load_setuptools_entrypoints(NAME)

    return pm