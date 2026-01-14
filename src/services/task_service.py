"""
Service layer for managing Task business logic.
"""
from typing import List, Optional
from src.models.task import Task
from src.repositories.task_repository import TaskRepository


class TaskService:
    """
    Service class for managing Task business logic.
    """
    
    def __init__(self, repository: TaskRepository):
        """
        Initialize the service with a repository.
        
        Args:
            repository: The TaskRepository to use
        """
        self.repository = repository
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task.

        Args:
            title: The title of the task
            description: The description of the task (optional)

        Returns:
            The created Task object
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or just whitespace")

        # Sanitize inputs
        title = title.strip()
        if description:
            description = description.strip()

        task = Task(id="", title=title, description=description)
        return self.repository.create(task)
    
    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False otherwise
        """
        return self.repository.delete(task_id)
    
    def update_task(self, task_id: str, title: Optional[str] = None,
                    description: Optional[str] = None) -> Optional[Task]:
        """
        Update a task's details.

        Args:
            task_id: The ID of the task to update
            title: The new title (optional)
            description: The new description (optional)

        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        task = self.repository.get_by_id(task_id)
        if not task:
            return None

        # Sanitize inputs
        if title is not None:
            title = title.strip() if title.strip() else task.title  # Keep original if sanitized title is empty
        if description is not None:
            description = description.strip() if description else None

        task.update(title=title, description=description)
        return self.repository.update(task_id, task)
    
    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        return self.repository.get_by_id(task_id)
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            A list of all Task objects
        """
        return self.repository.get_all()
    
    def mark_task_complete(self, task_id: str) -> Optional[Task]:
        """
        Mark a task as complete.
        
        Args:
            task_id: The ID of the task to mark complete
            
        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        task = self.repository.get_by_id(task_id)
        if not task:
            return None
        
        task.mark_complete()
        return self.repository.update(task_id, task)
    
    def mark_task_incomplete(self, task_id: str) -> Optional[Task]:
        """
        Mark a task as incomplete.
        
        Args:
            task_id: The ID of the task to mark incomplete
            
        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        task = self.repository.get_by_id(task_id)
        if not task:
            return None
        
        task.mark_incomplete()
        return self.repository.update(task_id, task)