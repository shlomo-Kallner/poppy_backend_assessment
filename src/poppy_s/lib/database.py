#!/bin/env python3

# from contextlib import contextmanager
from typing import Generator

from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.engine.base import Engine as BaseEngine
from sqlalchemy.future.engine import Engine as FutureEngine
# from sqlalchemy.engine.mock import MockConnection, create_mock_engine

from poppy_s.config import Configuration

class Database:
    def __init__(self) -> None:
        self._engine : BaseEngine | FutureEngine | None = None

    @property
    def engine(self) -> BaseEngine | FutureEngine | None:
        return self._engine
    
    # TODO: Add Mocking!!
    # def getMockDBEngine(self, config: Configuration, connect_args: dict = {}) -> BaseEngine | FutureEngine | MockConnection:
    #
    #   self._engine : MockConnection = create_mock_engine()
    #
    #   return self._engine

    def createDBEngine(self, config: Configuration, connect_args: dict = {}) -> BaseEngine | FutureEngine:
        
        self._engine = create_engine(
            config.database.DB_URL, 
            echo=config.app.DEBUG, 
            connect_args=connect_args
        )

        return self._engine
    

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self._engine)

    # @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        with Session(self._engine) as session:
            yield session


database = Database()