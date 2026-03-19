from sqlalchemy.orm import Session
from repositories.todo_repository import TodoRepository
from schemas.todo import TodoCreate, TodoUpdate


class TodoService:

    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create_todo(self, db: Session, todo: TodoCreate, user_id: int):
        return self.repository.create_todo_repo(db, todo, user_id)

    def get_todos(
        self,
        db: Session,
        user_id: int,
        is_done=None,
        q=None,
        sort=None,
        limit=100,
        offset=0
    ):
        items, total = self.repository.get_all(
            db, user_id, is_done, q, sort, limit, offset
        )

        return {
            "items": items,
            "total": total,
            "limit": limit,
            "offset": offset,
        }

    def get_todo(self, db: Session, todo_id: int, user_id: int):
        return self.repository.get_by_id(db, todo_id, user_id)

    def update_partial(self, db: Session, todo_id: int, user_id: int, data: TodoUpdate):
        return self.repository.partial_update(
            db,
            todo_id,
            user_id,
            data.model_dump(exclude_unset=True),
        )

    def complete_todo(self, db: Session, todo_id: int, user_id: int):
        return self.repository.mark_complete(db, todo_id, user_id)

    def delete_todo(self, db: Session, todo_id: int, user_id: int):
        return self.repository.delete(db, todo_id, user_id)
    
    def get_overdue(self, db, user_id):
        return self.repository.get_overdue(db, user_id)

    def get_today(self, db, user_id):
        return self.repository.get_today(db, user_id)