from typing import List
from schemas import Todo, TodoCreate
from datetime import datetime

todos: List[Todo] = []
current_id = 1

def create_todo(todo: TodoCreate) -> Todo:
    global current_id
    new_todo = Todo(
        id=current_id,
        title=todo.title,
        is_done=todo.is_done,
        created_at=datetime.utcnow()
    )
    todos.append(new_todo)
    current_id += 1
    return new_todo

def get_all_todos(
    is_done: bool | None = None,
    q: str | None = None,
    sort: str | None = None,
    limit: int = 10,
    offset: int = 0
):
    result = todos

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

def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None

def update_todo(todo_id: int, updated: TodoCreate):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = Todo(
                id=todo_id,
                title=updated.title,
                is_done=updated.is_done,
                created_at=todo.created_at  # giữ nguyên thời gian tạo
            )
            return todos[i]
    return None

def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            return todos.pop(i)
    return None
