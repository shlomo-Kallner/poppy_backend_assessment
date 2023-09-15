#!/bin/env python3

from typing import List, Optional, Type, TypeVar

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select, SQLModel

from poppy_s.lib.database import database


_T_SQLModel = TypeVar("_T_SQLModel", bound=SQLModel)

def genRouter(
    prefix_singular: str,
    prefix_plural: str,
    model_name: str,
    model: Type[_T_SQLModel],
    response_model: Type[_T_SQLModel],
    response_model_full_data: Type[_T_SQLModel],
    create_model: Optional[Type[_T_SQLModel]] = None,
) -> APIRouter:

    router = APIRouter(prefix=f"/{prefix_singular}", tags=["api", "api/v1", f"api/v1/{prefix_singular}", f"{prefix_plural}"])

    @router.get("/", response_model=List[response_model])
    async def getItems(
        *, 
        session: Session = Depends(database.get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100)
    ):

        items = session.exec(select(model).offset(offset).limit(limit)).all()
        return items

    if create_model is not None:

        @router.post("/", response_model=response_model)
        async def createItem(
            *, 
            session: Session = Depends(database.get_session), 
            item: create_model # type: ignore
        ):
            db_item = model.from_orm(item)
            session.add(db_item)
            session.commit()
            session.refresh(db_item)
            return db_item


    @router.get("/{item_id}", response_model=response_model_full_data)
    async def getItem(*, session: Session = Depends(database.get_session), item_id: int):
        item = session.get(model, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"{model_name} not found")
        return item

    # @router.post("/login")
    # async def loginUser():
    #     pass

    


    return router