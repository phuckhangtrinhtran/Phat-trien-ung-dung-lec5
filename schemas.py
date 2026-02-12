from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    is_done: bool = False

class Todo(TodoCreate):
    id: int
