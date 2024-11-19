from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
import config 
import models 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
DATABASE_URL = f'postgresql://manager:manager1@postgres-db:5432/taskmanagerdatabase'

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.on_event("startup")
def create_tables():
    """
    This function is executed when the application starts.
    It ensures that the database tables are created using the SQLAlchemy Base metadata.
    The `checkfirst=True` parameter ensures that tables are not recreated if they already exist.
    """
    config.Base.metadata.create_all(bind=engine, checkfirst=True)

@app.get("/tasks", response_model=list[models.TaskResponse])
async def get_tasks() -> list[models.TaskResponse]:
    """
    Handles the GET request to retrieve all tasks.

    - Initializes a new database session.
    - Fetches all task records from the database using a SQLAlchemy query.
    - Returns the list of tasks from the database.
    """
    db = SessionLocal()
    try: 
        tasks = db.query(models.Task).all()
        return tasks
    finally:
        db.close()

@app.post("/tasks", response_model=models.TaskResponse)
async def post_tasks(task: models.TaskRequest) -> models.TaskResponse:
    """
    Handles the POST request to create a new task.

    - Accepts a TaskRequest model as input, containing the description of the task.
    - Initializes a new database session.
    - Creates a new Task object, adds it to the database, and commits the transaction.
    - Refreshes the Task object to include generated fields like `id` and `created_at`.
    - Returns the created task as a responses.
    """
    db = SessionLocal()
    try:
        new_task = models.Task(description=task.description)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return models.TaskResponse(
        id=new_task.id,
        description=new_task.description,
        created_at=new_task.created_at,
    )
    finally: 
        db.close()

@app.delete("/tasks/{id}", response_model=dict)
async def delete_tasks(id: int) -> dict:
    """
    Handles the DELETE request to remove a task by its ID.

    - Accepts the task ID as a path parameter.
    - Initializes a new database session.
    - Queries the database for a task with the given ID.
    - If the task exists, deletes it and commits the transaction.
    - Returns a success message as a dictionary.
    """
    db = SessionLocal()
    try:
        task = db.query(models.Task).filter(models.Task.id == id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found in DB")
        
        db.delete(task)
        db.commit()
        return {"message": f"Task '{id}' deleted successfully"}
    finally: 
        db.close()