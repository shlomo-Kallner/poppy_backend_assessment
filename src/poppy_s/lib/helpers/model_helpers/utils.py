#!/bin/env python3

from typing import Type, TypeVar, Sequence
from collections.abc import Sequence as SequenceABC
from sqlmodel import SQLModel
from itertools import chain

_T_SQLModel = TypeVar("_T_SQLModel", bound=SQLModel)


def flatten_model_list(models: Sequence[SQLModel] | Sequence[Sequence[_T_SQLModel]], model_type: Type[_T_SQLModel]) -> list[_T_SQLModel]:

    res : list[_T_SQLModel] = []

    for result in models:
        if isinstance(result, model_type):
            res.append(result)
        else:
            for rv in result:
                if isinstance(rv, model_type):
                    res.append(rv)
                elif not isinstance(rv, (list, tuple, set, SequenceABC)):
                    nrv = model_type.from_orm(rv)
                    res.append(nrv)
                else:
                    # flaten!!!
                    for nrv in chain.from_iterable(rv):
                        if isinstance(nrv, model_type):
                            res.append(nrv)
                        elif not isinstance(nrv, (list, tuple, set)):
                            nnrv = model_type.from_orm(nrv)
                            res.append(nnrv)
                        else:
                            # recurse!!!
                            res.extend(
                                flatten_model_list(
                                    models=nrv, # type: ignore
                                    model_type=model_type
                                )
                            )

    return res