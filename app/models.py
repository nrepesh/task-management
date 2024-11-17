from sqlalchemy import Column, Integer, String, DateTime, func
from config import Base
from datetime import datetime
from pydantic import BaseModel

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=func.now())

class TaskResponse(BaseModel):
    id: int
    description: str
    created_at: datetime  