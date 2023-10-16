#!/bin/env python3

from typing import cast
from pluggy import PluginManager


def pmTypeHelper(pm: PluginManager|None) -> PluginManager:
    return cast(PluginManager, pm)
