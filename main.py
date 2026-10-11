from itertools import count

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API", version="1.0.0")

_task_ids = count(1)
_tasks: list[dict[str, object]] = []


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="", max_length=1000)


class Task(TaskCreate):
    id: int


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/tasks",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task_data: TaskCreate) -> Task:
    task = Task(id=next(_task_ids), **task_data.model_dump())
    _tasks.append(task.model_dump())
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return [Task(**task) for task in _tasks]
