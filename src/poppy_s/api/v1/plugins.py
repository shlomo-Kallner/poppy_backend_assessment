#!/bin/env python3

from fastapi import APIRouter

from poppy_s.lib.container import globalContainer
from poppy_s.lib.schemas.plugins import RouterPluginSchema
from poppy_s.lib.helpers.plugin_helpers.exception import check_if_plugins_loaded
from poppy_s.lib.helpers.plugin_helpers.utils import pmTypeHelper


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


    # Insert call to retrieve the plugin Routers here!
    check_if_plugins_loaded()

    pluginRouters : list[APIRouter|RouterPluginSchema] = pmTypeHelper(
        globalContainer.plugins
    ).hook.add_plugin_router()

    # Insert loop to include the plugin Routers here!
    for sub_router in pluginRouters:
        if isinstance(sub_router, APIRouter):
            router.include_router(sub_router)
        elif isinstance(sub_router, RouterPluginSchema):
            if isinstance(sub_router.router, APIRouter):
                sub_router_router = sub_router.router
            elif (
                callable(sub_router.router) and 
                isinstance(( tmp_router := sub_router.router() ), APIRouter)
            ):
                sub_router_router = tmp_router
            else:
                continue
            router.include_router(
                sub_router_router,
                **sub_router.dict(
                    exclude={"router"},
                    exclude_none=True,
                    exclude_defaults=True,
                    exclude_unset=True
                )
            )


    return router



