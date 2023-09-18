#!/bin/env python3

from types import ModuleType
from typing import Optional
from warnings import filterwarnings
from importlib import import_module
from importlib.resources import files as importlib_files
# from importlib.abc import Traversable
from importlib.machinery import SOURCE_SUFFIXES
from re import fullmatch, IGNORECASE, escape

from pluggy import HookimplMarker, PluginManager

from poppy_s.__version__ import NAME
# from poppy_s.lib.plugins.specs import nih_data, validators


PluginImpl = HookimplMarker(NAME)

def getPlugins() -> PluginManager:
    # from poppy_s.lib.plugins.builtin import nih_data as basic_nih_data, validators as basic_validators
    from poppy_s.lib.plugins import builtin as builtin_implemtation_packages
    from poppy_s.lib.plugins import specs

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

    # pm.add_hookspecs(nih_data)
    # pm.add_hookspecs(validators)

    def recursively_load(mod_pack: ModuleType, is_plugin_spec:bool, super_pack: Optional[str] = None) -> None:

        mod_dir = importlib_files(mod_pack)

        def _load_mod(name: str) -> ModuleType:
            return import_module(
                f".{name}",
                package=''.join( 
                    [
                        f'{super_pack}.' if super_pack is not None else '',
                        f"{mod_pack.__package__}"
                    ]
                )
            )

        for mod in mod_dir.iterdir():
            if fullmatch(
                r"(\.|_{1,}).+(_{1,})",
                mod.name,
                IGNORECASE
            ) is not None:
                # skip hidden or private files/modules (example: "__pycache__")
                continue
            
            mod_mat = fullmatch( 
                # for now only plain ("source") python modules!!
                fr"(?P<name>..+)\.({'|'.join([ escape(eStr.strip('.')) for eStr in SOURCE_SUFFIXES])})", 
                mod.name,
                IGNORECASE
            )

            if mod_mat is None or mod.is_dir():
                sub_pack = _load_mod(mod.name)
                recursively_load(
                    sub_pack,
                    is_plugin_spec=is_plugin_spec,
                    super_pack=''.join(
                        [
                            f'{super_pack}.' if super_pack is not None else '',
                            mod.name
                        ]
                    )
                )

            elif (
                mod.is_file() and 
                mod_mat.start() != mod_mat.end() and
                mod_mat["name"] is not None
            ):
                # load this!
                sub_mod = _load_mod(mod_mat["name"])
                if is_plugin_spec:
                    pm.add_hookspecs(sub_mod)
                else:
                    pm.register(sub_mod)

            else:
                # not a python file! SKIP!!
                continue

    
    recursively_load(specs, is_plugin_spec=True)

    pm.load_setuptools_entrypoints(NAME)

    # pm.register(basic_nih_data)
    # pm.register(basic_validators)

    return pm