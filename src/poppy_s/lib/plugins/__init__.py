#!/bin/env python3


from warnings import filterwarnings

from pluggy import HookimplMarker, PluginManager

from poppy_s.__version__ import NAME
from poppy_s.lib.plugins.specs import nih_data, validators


PluginImpl = HookimplMarker(NAME)

def getPlugins() -> PluginManager:
    from poppy_s.lib.plugins.builtin import nih_data as basic_nih_data, validators as basic_validators

    filterwarnings(
        action="always", 
        message=r".*",
        category=DeprecationWarning
    )

    filterwarnings(
        action="always", 
        message=r".*",
        category=PendingDeprecationWarning
    )

    filterwarnings(
        action="always", 
        message=r".*",
        category=FutureWarning
    )
    
    pm = PluginManager(NAME)

    # TODO: Add tracing and hook call monitoring!!

    pm.add_hookspecs(nih_data)
    pm.add_hookspecs(validators)

    pm.load_setuptools_entrypoints(NAME)

    pm.register(basic_nih_data)
    pm.register(basic_validators)

    return pm