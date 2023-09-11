#!/bin/env python3

from pluggy import HookCallError, HookspecMarker, HookimplMarker


PluginSpec = HookspecMarker("poppy_s")
PluginImpl = HookimplMarker("poppy_s")