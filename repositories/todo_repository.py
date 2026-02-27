from typing import List, Optional
from datetime import datetime
from schemas.todo import Todo, TodoCreate

class TodoRepository:
    def __init__(self):
        self.todos: List[Todo] = []
        self.current_id = 1

    def create(self, todo: TodoCreate) -> Todo:
        new_todo = Todo(
            id=self.current_id,
            title=todo.title,
            is_done=todo.is_done,
            created_at=datetime.utcnow()
        )
        self.todos.append(new_todo)
        self.current_id += 1
        return new_todo

    def get_all(self) -> List[Todo]:
        return self.todos

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update(self, todo_id: int, updated: TodoCreate) -> Optional[Todo]:
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                self.todos[i] = Todo(
                    id=todo_id,
                    title=updated.title,
                    is_done=updated.is_done,
                    created_at=todo.created_at
                )
                return self.todos[i]
        return None

    def delete(self, todo_id: int) -> Optional[Todo]:
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                return self.todos.pop(i)
        return None