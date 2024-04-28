
from typing import Annotated
from fastapi import APIRouter, Depends
from repo import TaskRepository
from schemas import TaskAdd, Task, TaskID

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.post("")
async def add_task(
    task: Annotated[TaskAdd, Depends()]
) -> TaskID:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.find_all()
    return {"data": tasks}
