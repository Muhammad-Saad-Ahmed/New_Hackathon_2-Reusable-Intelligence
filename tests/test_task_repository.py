"""
Tests for the TaskRepository.
"""
import pytest
from src.models.task import Task
from src.repositories.task_repository import TaskRepository


class TestTaskRepository:
    """Test cases for the TaskRepository."""
    
    def setup_method(self):
        """Set up a fresh repository for each test."""
        self.repo = TaskRepository()
    
    def test_create_task(self):
        """Test creating a task in the repository."""
        task = Task(id="1", title="Test Task")
        created_task = self.repo.create(task)
        
        assert created_task.id == "1"
        assert created_task.title == "Test Task"
        assert self.repo.get_by_id("1") is not None
    
    def test_get_by_id_found(self):
        """Test retrieving an existing task by ID."""
        task = Task(id="1", title="Test Task")
        self.repo.create(task)
        
        retrieved_task = self.repo.get_by_id("1")
        
        assert retrieved_task is not None
        assert retrieved_task.id == "1"
        assert retrieved_task.title == "Test Task"
    
    def test_get_by_id_not_found(self):
        """Test retrieving a non-existing task by ID."""
        retrieved_task = self.repo.get_by_id("nonexistent")
        
        assert retrieved_task is None
    
    def test_get_all_empty(self):
        """Test getting all tasks when repository is empty."""
        tasks = self.repo.get_all()
        
        assert len(tasks) == 0
    
    def test_get_all_with_tasks(self):
        """Test getting all tasks when repository has tasks."""
        task1 = Task(id="1", title="Task 1")
        task2 = Task(id="2", title="Task 2")
        
        self.repo.create(task1)
        self.repo.create(task2)
        
        tasks = self.repo.get_all()
        
        assert len(tasks) == 2
        task_ids = [task.id for task in tasks]
        assert "1" in task_ids
        assert "2" in task_ids
    
    def test_update_existing_task(self):
        """Test updating an existing task."""
        task = Task(id="1", title="Original Task")
        self.repo.create(task)
        
        updated_task = Task(id="1", title="Updated Task", description="Updated Description")
        result = self.repo.update("1", updated_task)
        
        assert result is not None
        assert result.title == "Updated Task"
        assert result.description == "Updated Description"
        
        # Verify the task was actually updated in the repository
        retrieved_task = self.repo.get_by_id("1")
        assert retrieved_task.title == "Updated Task"
        assert retrieved_task.description == "Updated Description"
    
    def test_update_nonexistent_task(self):
        """Test updating a non-existing task."""
        updated_task = Task(id="1", title="Updated Task")
        result = self.repo.update("1", updated_task)
        
        assert result is None
    
    def test_delete_existing_task(self):
        """Test deleting an existing task."""
        task = Task(id="1", title="Test Task")
        self.repo.create(task)
        
        result = self.repo.delete("1")
        
        assert result is True
        assert self.repo.get_by_id("1") is None
    
    def test_delete_nonexistent_task(self):
        """Test deleting a non-existing task."""
        result = self.repo.delete("nonexistent")
        
        assert result is False