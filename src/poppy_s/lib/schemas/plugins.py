#!/bin/env python3

from typing import List, Optional, Type, TypeVar

from fastapi import APIRouter, Depends, HTTPException, Query

from pydantic import BaseModel