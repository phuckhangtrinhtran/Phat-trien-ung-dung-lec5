from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class TodoCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Title must be between 3 and 100 characters"
    )
    is_done: bool = False


class Todo(TodoCreate):
    id: int
    created_at: datetime

class TodoListResponse(BaseModel):
    items: List[Todo]
    total: int
    limit: int
    offset: int