from sqlalchemy.orm import Session
from app.database.schema import TodoSchema
from app.models.TodoModal import TodoUpdate


def get_todos(db: Session):
    return db.query(TodoSchema).all()


def create_todo(db: Session, todo: TodoSchema):
    new_todo = TodoSchema(title=todo.title, completed=todo.completed)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_todo(db: Session, todo_id: int):
    return db.query(TodoSchema).filter(TodoSchema.id == todo_id).first()


def update_todo(db: Session, todo_id: int, todo_data: TodoUpdate):
    todo = db.query(TodoSchema).filter(TodoSchema.id == todo_id).first()

    if not todo:
        return None

    if todo_data.title is not None:
        todo.title = todo_data.title # type: ignore

    if todo_data.completed is not None:
        todo.completed = todo_data.completed  # type: ignore

    db.commit()
    db.refresh(todo)

    return todo


def delete_todo(db: Session, todo_id: int):
    todo = db.query(TodoSchema).filter(TodoSchema.id == todo_id).first()

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return todo
