from pydantic import BaseModel 
from datetime import datetime

class Task(BaseModel):
    id: int
    description: str
    created_at: datetime