#!/bin/env python3

from pluggy import HookspecMarker
from poppy_s.__version__ import NAME

PluginSpec = HookspecMarker(NAME)
