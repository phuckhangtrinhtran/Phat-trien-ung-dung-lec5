from typing import List
from schemas import Todo, TodoCreate

todos: List[Todo] = []
current_id = 1

def create_todo(todo: TodoCreate) -> Todo:
    global current_id
    new_todo = Todo(id=current_id, title=todo.title, is_done=todo.is_done)
    todos.append(new_todo)
    current_id += 1
    return new_todo

def get_all_todos():
    return todos

def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None

def update_todo(todo_id: int, updated: TodoCreate):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = Todo(id=todo_id, title=updated.title, is_done=updated.is_done)
            return todos[i]
    return None

def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            return todos.pop(i)
    return None
