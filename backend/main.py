from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
import config 
import models 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins for production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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
async def post_tasks(task: models.TaskRequest) -> models.TaskResponse:
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