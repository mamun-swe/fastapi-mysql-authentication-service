# app/schemas/response.py
from pydantic import BaseModel
from typing import Any


class ResponseModel(BaseModel):
    status: bool
    message: str
    data: Any
