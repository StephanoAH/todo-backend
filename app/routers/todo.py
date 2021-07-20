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


@router.get("/{id}", response_model=schemas.TodoBase, status_code=status.HTTP_200_OK)
def get_specific_todo(id, db: Session = Depends(session.get_db)):
    return todo.get_one(id, db)


@router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_todo(id, ut: schemas.TodoUpdate, db: Session = Depends(session.get_db)):
    return todo.update(id, ut, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id, db: Session = Depends(session.get_db)):
    return todo.delete(id, db)
