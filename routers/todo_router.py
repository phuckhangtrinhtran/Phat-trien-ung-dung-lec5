from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from dependencies.auth import get_current_user
from typing import Optional
from core.database import get_db
from schemas.todo import TodoCreate, TodoResponse, TodoUpdate, TodoListResponse
from repositories.todo_repository import TodoRepository
from services.todo_service import TodoService

router = APIRouter(prefix="/api/v1/todos", tags=["todos"])

repository = TodoRepository()
service = TodoService(repository)

@router.get("/overdue", response_model=list[TodoResponse])
def overdue_todos(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return service.get_overdue(db, user.id)

@router.get("/today", response_model=list[TodoResponse])
def today_todos(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return service.get_today(db, user.id)

@router.post("/", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return service.create_todo(db, todo, user.id)


@router.get("/", response_model=TodoListResponse)
def read_todos(
    is_done: Optional[bool] = Query(None),
    q: Optional[str] = Query(None),
    sort: Optional[str] = Query(None),
    limit: int = Query(100),
    offset: int = Query(0),

    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return service.get_todos(
        db,
        user.id,
        is_done,
        q,
        sort,
        limit,
        offset
    )


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    todo = service.get_todo(db, todo_id, user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.patch("/{todo_id}", response_model=TodoResponse)
def partial_update(
    todo_id: int,
    data: TodoUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    todo = service.update_partial(db, todo_id, user.id, data)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.post("/{todo_id}/complete", response_model=TodoResponse)
def complete(
    todo_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    todo = service.complete_todo(db, todo_id, user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.delete("/{todo_id}")
def delete(
    todo_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    todo = service.delete_todo(db, todo_id, user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}

