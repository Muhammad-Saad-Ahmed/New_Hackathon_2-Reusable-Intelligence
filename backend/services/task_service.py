"""
Service layer for handling task-related operations.
"""
from sqlalchemy.orm import Session
from models.database import Task as TaskModel
from schemas.task import TaskCreate, TaskUpdate
import uuid

class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def get_tasks(self, user_id: uuid.UUID, skip: int = 0, limit: int = 100, filters: dict = None):
        query = self.db.query(TaskModel).filter(TaskModel.user_id == user_id)
        if filters:
            if "status" in filters:
                query = query.filter(TaskModel.completed == (filters["status"] == "completed"))
            if "priority" in filters:
                query = query.filter(TaskModel.priority == filters["priority"])
        return query.offset(skip).limit(limit).all()

    def get_task(self, user_id: uuid.UUID, task_id: uuid.UUID):
        return self.db.query(TaskModel).filter(
            TaskModel.user_id == user_id, TaskModel.id == task_id
        ).first()

    def create_task(self, user_id: uuid.UUID, task: TaskCreate):
        db_task = TaskModel(**task.model_dump(), user_id=user_id)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def update_task(self, user_id: uuid.UUID, task_id: uuid.UUID, task: TaskUpdate):
        db_task = self.get_task(user_id, task_id)
        if db_task:
            for key, value in task.model_dump(exclude_unset=True).items():
                setattr(db_task, key, value)
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    def delete_task(self, user_id: uuid.UUID, task_id: uuid.UUID):
        db_task = self.get_task(user_id, task_id)
        if db_task:
            self.db.delete(db_task)
            self.db.commit()
            return True
        return False
