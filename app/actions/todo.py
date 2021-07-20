from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from starlette.responses import Response
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


def update(id, ut: schemas.TodoUpdate, db: Session):
    update_todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not update_todo.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {id} can't be modified"
        )
    update_todo.update(ut.dict(exclude_unset=True))
    db.commit()
    return "Updated"


def delete(id, db: Session):
    delete_todo = db.query(models.Todo).filter(models.Todo.id == id)
    if not delete_todo.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {id} can't be modified"
        )
    delete_todo.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
