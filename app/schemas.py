from typing import List, Optional
from datetime import date
from pydantic import BaseModel, EmailStr


class TodoBase(BaseModel):
    title: str
    description: str
    is_done: bool = False

    class Config:
        orm_mode = True


class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    is_done: Optional[bool] = False

    class Config:
        orm_mode = True


class Todo(TodoBase):
    created_on: date
    updated_on: date
