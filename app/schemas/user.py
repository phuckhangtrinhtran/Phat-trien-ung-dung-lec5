from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    email: str
    password: str = Field(..., min_length=6, max_length=72)

class UserOut(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True