from fastapi import APIRouter, Depends, status
from .. import schemas
from ..db import session
from ..actions import todo
from sqlalchemy.orm import Session

router = APIRouter(tags=["Todos"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(t: schemas.TodoBase, db: Session = Depends(session.get_db)):
    return todo.create(t, db)


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_todos(db: Session = Depends(session.get_db)):
    return todo.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_specific_todo(id, db: Session = Depends(session.get_db)):
    return todo.get_one(id, db)
