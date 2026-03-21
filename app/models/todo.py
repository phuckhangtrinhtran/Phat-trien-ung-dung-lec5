from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy import JSON 


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    is_done = Column(Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("users.id"))  # ✅ FIX
    owner = relationship("User")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    due_date = Column(DateTime, nullable=True) 
    tags = Column(JSON, default=[])

    deleted_at = Column(DateTime(timezone=True), nullable=True, default=None)