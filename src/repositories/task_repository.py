"""
Repository for managing Task objects in memory.
"""
from typing import Dict, List, Optional
from src.models.task import Task


class TaskRepository:
    """
    Repository class for managing Task objects in memory.
    """
    
    def __init__(self):
        """
        Initialize the repository with an empty storage.
        """
        self._tasks: Dict[str, Task] = {}
    
    def create(self, task: Task) -> Task:
        """
        Create a new task in the repository.
        
        Args:
            task: The Task object to create
            
        Returns:
            The created Task object
        """
        self._tasks[task.id] = task
        return task
    
    def get_by_id(self, task_id: str) -> Optional[Task]:
        """
        Retrieve a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        return self._tasks.get(task_id)
    
    def get_all(self) -> List[Task]:
        """
        Retrieve all tasks in the repository.
        
        Returns:
            A list of all Task objects
        """
        return list(self._tasks.values())
    
    def update(self, task_id: str, task: Task) -> Optional[Task]:
        """
        Update an existing task in the repository.
        
        Args:
            task_id: The ID of the task to update
            task: The updated Task object
            
        Returns:
            The updated Task object if successful, None if task doesn't exist
        """
        if task_id not in self._tasks:
            return None
        
        self._tasks[task_id] = task
        return task
    
    def delete(self, task_id: str) -> bool:
        """
        Delete a task from the repository.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if it didn't exist
        """
        if task_id not in self._tasks:
            return False
        
        del self._tasks[task_id]
        return True
    
    def get_by_user(self, user_id: str) -> List[Task]:
        """
        Retrieve all tasks for a specific user.
        Note: In the console app, we're simulating user separation.
        
        Args:
            user_id: The ID of the user
            
        Returns:
            A list of Task objects for the user
        """
        # In the console app, we're not implementing multi-user functionality
        # This method is included for consistency with the web app design
        return self.get_all()