from fastapi import FastAPI
from fastapi import HTTPException
from schemas import TodoCreate, Todo, TodoListResponse
import crud
from typing import Optional
from fastapi import Query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello To-Do API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    return crud.create_todo(todo)


@app.get("/todos", response_model=TodoListResponse)
def get_todos(
    is_done: Optional[bool] = None,
    q: Optional[str] = None,
    sort: Optional[str] = Query(None, regex="^-?created_at$"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    return crud.get_all_todos(
        is_done=is_done,
        q=q,
        sort=sort,
        limit=limit,
        offset=offset
    )

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = crud.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoCreate):
    todo = crud.update_todo(todo_id, updated_todo)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    todo = crud.delete_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}