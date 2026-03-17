from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from core.database import get_db
from schemas.todo import (
    TodoCreate,
    TodoResponse,
    TodoListResponse,
    TodoUpdate,
)
from repositories.todo_repository import TodoRepository
from services.todo_service import TodoService

router = APIRouter(prefix="/api/v1/todos", tags=["todos"])

repository = TodoRepository()
service = TodoService(repository)


@router.post("/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return service.create_todo(db, todo)


@router.get("/", response_model=TodoListResponse)
def get_todos(
    is_done: Optional[bool] = None,
    q: Optional[str] = None,
    sort: Optional[str] = Query(None, pattern="^-?created_at$"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return service.get_all_todos(db, is_done, q, sort, limit, offset)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = service.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.patch("/{todo_id}", response_model=TodoResponse)
def partial_update(
    todo_id: int,
    data: TodoUpdate,
    db: Session = Depends(get_db),
):
    todo = service.update_partial(db, todo_id, data)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.post("/{todo_id}/complete", response_model=TodoResponse)
def complete(todo_id: int, db: Session = Depends(get_db)):
    todo = service.complete_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo = service.delete_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}