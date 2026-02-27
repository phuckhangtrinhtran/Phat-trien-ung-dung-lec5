from typing import Optional
from repositories.todo_repository import TodoRepository
from schemas.todo import TodoCreate

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create_todo(self, todo: TodoCreate):
        return self.repository.create(todo)

    def get_all_todos(
        self,
        is_done: Optional[bool],
        q: Optional[str],
        sort: Optional[str],
        limit: int,
        offset: int
    ):
        result = self.repository.get_all()

        # Filter
        if is_done is not None:
            result = [t for t in result if t.is_done == is_done]

        # Search
        if q:
            result = [t for t in result if q.lower() in t.title.lower()]

        total = len(result)

        # Sort
        if sort == "created_at":
            result = sorted(result, key=lambda x: x.created_at)
        elif sort == "-created_at":
            result = sorted(result, key=lambda x: x.created_at, reverse=True)

        # Pagination
        result = result[offset: offset + limit]

        return {
            "items": result,
            "total": total,
            "limit": limit,
            "offset": offset
        }

    def get_todo(self, todo_id: int):
        return self.repository.get_by_id(todo_id)

    def update_todo(self, todo_id: int, updated: TodoCreate):
        return self.repository.update(todo_id, updated)

    def delete_todo(self, todo_id: int):
        return self.repository.delete(todo_id)