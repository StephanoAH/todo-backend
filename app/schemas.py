from typing import List, Optional
from datetime import date
from pydantic import BaseModel, EmailStr


class TodoBase(BaseModel):
    title: str
    description: str
    is_done: bool = False


class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    is_done: Optional[bool]
    created_on: Optional[date]
    updated_on: Optional[date]


class Todo(TodoBase):
    created_on: date
    updated_on: date
