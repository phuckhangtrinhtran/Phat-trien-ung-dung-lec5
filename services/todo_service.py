from sqlalchemy.orm import Session
from repositories.todo_repository import TodoRepository
from schemas.todo import TodoCreate, TodoUpdate


class TodoService:

    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create_todo(self, db: Session, todo: TodoCreate):
        return self.repository.create(db, todo)

    def get_all_todos(
        self,
        db: Session,
        is_done,
        q,
        sort,
        limit,
        offset,
    ):
        items, total = self.repository.get_all(
            db, is_done, q, sort, limit, offset
        )

        return {
            "items": items,
            "total": total,
            "limit": limit,
            "offset": offset,
        }

    def get_todo(self, db: Session, todo_id: int):
        return self.repository.get_by_id(db, todo_id)

    def update_partial(self, db: Session, todo_id: int, data: TodoUpdate):
        return self.repository.partial_update(
            db,
            todo_id,
            data.model_dump(exclude_unset=True),
        )

    def complete_todo(self, db: Session, todo_id: int):
        return self.repository.mark_complete(db, todo_id)

    def delete_todo(self, db: Session, todo_id: int):
        return self.repository.delete(db, todo_id)