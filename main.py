from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ===== CẤP 0 =====
@app.get("/")
def read_root():
    return {"message": "Hello To-Do API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# ===== CẤP 1 =====
class TodoCreate(BaseModel):
    title: str
    is_done: bool = False

class Todo(TodoCreate):
    id: int


todos: List[Todo] = []
current_id = 1


@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    global current_id

    new_todo = Todo(
        id=current_id,
        title=todo.title,
        is_done=todo.is_done
    )
    todos.append(new_todo)
    current_id += 1
    return new_todo


@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoCreate):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = Todo(
                id=todo_id,
                title=updated_todo.title,
                is_done=updated_todo.is_done
            )
            return todos[index]
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")