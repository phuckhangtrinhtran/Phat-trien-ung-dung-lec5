from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from datetime import datetime
from typing import Optional, List


class TodoBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = None
    is_done: bool = False
    due_date: Optional[datetime] = None  
    tags: Optional[List[str]] = [] 


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_done: Optional[bool] = None
    due_date: Optional[datetime] = None
    tags: Optional[List[str]] = None


class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TodoListResponse(BaseModel):
    items: List[TodoResponse]
    total: int
    limit: int
    offset: int