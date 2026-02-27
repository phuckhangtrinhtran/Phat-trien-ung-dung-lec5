from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from schemas.todo import Todo, TodoCreate, TodoListResponse
from repositories.todo_repository import TodoRepository
from services.todo_service import TodoService

router = APIRouter(prefix="/api/v1/todos", tags=["todos"])

repository = TodoRepository()
service = TodoService(repository)

@router.post("/", response_model=Todo)
def create_todo(todo: TodoCreate):
    return service.create_todo(todo)


@router.get("/", response_model=TodoListResponse)
def get_todos(
    is_done: Optional[bool] = None,
    q: Optional[str] = None,
    sort: Optional[str] = Query(None, pattern="^-?created_at$"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    return service.get_all_todos(is_done, q, sort, limit, offset)


@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = service.get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoCreate):
    todo = service.update_todo(todo_id, updated_todo)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    todo = service.delete_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}