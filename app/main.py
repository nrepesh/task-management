from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
import config 
import models 

engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()


@app.on_event("startup")
def create_tables():
    config.Base.metadata.create_all(bind=engine, checkfirst=True)

@app.get("/tasks", response_model=list[models.TaskResponse])
async def get_tasks() -> list[models.TaskResponse]:
    db = SessionLocal()
    try: 
        tasks = db.query(models.Task).all()
        return tasks
    finally:
        db.close()

@app.post("/tasks", response_model=models.TaskResponse)
async def post_tasks(description: str) -> models.TaskResponse:
    db = SessionLocal()
    try:
        new_task = models.Task(description=description)
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
async def delete_tasks(task_id: int) -> dict:
    db = SessionLocal()
    try:
        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found in DB")
        
        db.delete(task)
        db.commit()
        return {"message": f"Task '{task_id}' deleted successfully"}
    finally: 
        db.close()