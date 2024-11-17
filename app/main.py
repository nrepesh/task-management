from fastapi import FastAPI, HTTPException
import utils

app = FastAPI()


@app.get("/tasks", response_model=list[str])
async def get_tasks() -> list[str]:
    pass

@app.post("/tasks", response_model=utils.Task)
async def post_tasks() -> utils.Task:
    pass

@app.delete("/tasks/{id}", response_model=dict)
async def delete_tasks() -> dict:
    raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task '{deleted_task}' deleted successfully"}