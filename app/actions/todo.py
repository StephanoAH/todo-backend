from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from .. import schemas, models


def create(t: schemas.TodoBase, db: Session):
    new_todo = models.Todo(title=t.title, description=t.description, is_done=t.is_done)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_all(db: Session):
    todos = db.query(models.Todo).all()
    if not todos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No todo")
    return todos


def get_one(id, db: Session):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo {id} doesn't exist"
        )
    return todo
