#!/bin/env python3

from fastapi import APIRouter


def getRouter() -> APIRouter:

    router = APIRouter(prefix="/user", tags=["api", "api/v1", "api/v1/user", "users"])

    @router.get("/")
    async def getUsers():
        pass



    @router.post("/")
    async def creatUser():
        pass

    @router.get("/{user_id}")
    async def getUser(user_id: int):
        pass


    return router