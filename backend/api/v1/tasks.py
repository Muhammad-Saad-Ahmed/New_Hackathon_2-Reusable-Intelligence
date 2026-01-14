"""
API endpoints for managing tasks.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
import uuid

from core.database import get_db
from schemas.task import TaskCreate, TaskUpdate, Task, TaskResponse, TasksResponse, MessageResponse
from services.task_service import TaskService
from middleware.auth_middleware import JWTBearer

router = APIRouter()

@router.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate, db: Session = Depends(get_db), token_data: dict = Depends(JWTBearer())):
    user_id = uuid.UUID(token_data.get("sub"))
    task_service = TaskService(db)
    db_task = task_service.create_task(user_id, task)
    return {"success": True, "data": db_task}

@router.get("/tasks/", response_model=TasksResponse)
async def get_tasks(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    db: Session = Depends(get_db),
    token_data: dict = Depends(JWTBearer())
):
    user_id = uuid.UUID(token_data.get("sub"))
    task_service = TaskService(db)
    filters = {}
    if status:
        filters["status"] = status
    if priority:
        filters["priority"] = priority
    tasks = task_service.get_tasks(user_id, filters=filters)
    return {"success": True, "data": tasks}

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: uuid.UUID, db: Session = Depends(get_db), token_data: dict = Depends(JWTBearer())):
    user_id = uuid.UUID(token_data.get("sub"))
    task_service = TaskService(db)
    task = task_service.get_task(user_id, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"success": True, "data": task}

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: uuid.UUID, task: TaskUpdate, db: Session = Depends(get_db), token_data: dict = Depends(JWTBearer())):
    user_id = uuid.UUID(token_data.get("sub"))
    task_service = TaskService(db)
    db_task = task_service.update_task(user_id, task_id, task)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"success": True, "data": db_task}

@router.patch("/tasks/{task_id}/complete", response_model=TaskResponse)
async def update_task_completion(task_id: uuid.UUID, completed: bool, db: Session = Depends(get_db), token_data: dict = Depends(JWTBearer())):
    user_id = uuid.UUID(token_data.get("sub"))
    task_service = TaskService(db)
    task_update = TaskUpdate(completed=completed)
    db_task = task_service.update_task(user_id, task_id, task_update)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"success": True, "data": db_task}

@router.delete("/tasks/{task_id}", response_model=MessageResponse)
async def delete_task(task_id: uuid.UUID, db: Session = Depends(get_db), token_data: dict = Depends(JWTBearer())):
    user_id = uuid.UUID(token_data.get("sub"))
    task_service = TaskService(db)
    if not task_service.delete_task(user_id, task_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"success": True, "message": "Task deleted successfully"}