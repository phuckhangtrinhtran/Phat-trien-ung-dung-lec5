from sqlalchemy.orm import Session
from models.todo import Todo
from schemas.todo import TodoCreate
from typing import Optional


class TodoRepository:

    def create(self, db: Session, todo: TodoCreate):
        db_todo = Todo(**todo.model_dump())
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    def get_by_id(self, db: Session, todo_id: int):
        return db.query(Todo).filter(Todo.id == todo_id).first()

    def get_all(
        self,
        db: Session,
        is_done: Optional[bool],
        q: Optional[str],
        sort: Optional[str],
        limit: int,
        offset: int,
    ):
        query = db.query(Todo)

        if is_done is not None:
            query = query.filter(Todo.is_done == is_done)

        if q:
            query = query.filter(Todo.title.ilike(f"%{q}%"))

        total = query.count()

        if sort == "created_at":
            query = query.order_by(Todo.created_at)
        elif sort == "-created_at":
            query = query.order_by(Todo.created_at.desc())

        items = query.offset(offset).limit(limit).all()

        return items, total

    def partial_update(self, db: Session, todo_id: int, data: dict):
        todo = self.get_by_id(db, todo_id)
        if not todo:
            return None

        for key, value in data.items():
            setattr(todo, key, value)

        db.commit()
        db.refresh(todo)
        return todo

    def mark_complete(self, db: Session, todo_id: int):
        todo = self.get_by_id(db, todo_id)
        if not todo:
            return None

        todo.is_done = True
        db.commit()
        db.refresh(todo)
        return todo

    def delete(self, db: Session, todo_id: int):
        todo = self.get_by_id(db, todo_id)
        if not todo:
            return None

        db.delete(todo)
        db.commit()
        return todo