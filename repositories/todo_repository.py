from sqlalchemy.orm import Session
from models.todo import Todo
from typing import Optional
from datetime import datetime, timedelta


class TodoRepository:

    def create_todo_repo(self, db: Session, todo, user_id: int):
        new_todo = Todo(**todo.dict(), owner_id=user_id)
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return new_todo

    def get_by_id(self, db: Session, todo_id: int, user_id: int):
        return db.query(Todo).filter(
            Todo.id == todo_id,
            Todo.owner_id == user_id
        ).first()

    def get_all(
        self,
        db: Session,
        user_id: int,
        is_done: Optional[bool],
        q: Optional[str],
        sort: Optional[str],
        limit: int,
        offset: int,
    ):
        query = db.query(Todo).filter(Todo.owner_id == user_id)

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

    def partial_update(self, db: Session, todo_id: int, user_id: int, data: dict):
        todo = self.get_by_id(db, todo_id, user_id)
        if not todo:
            return None

        for key, value in data.items():
            setattr(todo, key, value)

        db.commit()
        db.refresh(todo)
        return todo

    def mark_complete(self, db: Session, todo_id: int, user_id: int):
        todo = self.get_by_id(db, todo_id, user_id)
        if not todo:
            return None

        todo.is_done = True
        db.commit()
        db.refresh(todo)
        return todo

    def delete(self, db: Session, todo_id: int, user_id: int):
        todo = self.get_by_id(db, todo_id, user_id)
        if not todo:
            return None

        db.delete(todo)
        db.commit()
        return todo
    
    def get_overdue(self, db, user_id):
        return db.query(Todo).filter(
            Todo.owner_id == user_id,
            Todo.is_done == False,
            Todo.due_date < datetime.utcnow()
        ).all()

    def get_today(self, db, user_id):
        now = datetime.now()
        today_start = now.replace(hour=0, minute=0, second=0)
        today_end = today_start + timedelta(days=1)

        return db.query(Todo).filter(
            Todo.owner_id == user_id,
            Todo.is_done == False,
            Todo.due_date >= today_start,
            Todo.due_date < today_end
        ).all()