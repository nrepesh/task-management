from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base 
from datetime import datetime
from pydantic import BaseModel

Base = declarative_base()     # sqlalchemy base class

class Task(Base):
    """
    Represents the 'tasks' table in the database.

    - __tablename__: Specifies the name of the table ('tasks').
    - id: The primary key column, an auto-incrementing integer.
    - description: A column to store the task description as a string.
    - created_at: A timestamp column with a default value of the current time (using `func.now()`).
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=func.now())

class TaskResponse(BaseModel):
    """
    Formatting responses when fetching or returning task data in the api call.

    - id: The unique identifier of the task (integer).
    - description: The description of the task (string).
    - created_at: The timestamp indicating when the task was created (datetime).
    """
    id: int
    description: str
    created_at: datetime  

class TaskRequest(BaseModel):
    """
    Validating requests to create a new task in the api call.

    - description: The description of the task (string).
    """
    description: str