"""
Tests for the TaskService.
"""
import sys
import os
import pytest

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.services.task_service import TaskService


class TestTaskService:
    """Test cases for the TaskService."""
    
    def setup_method(self):
        """Set up a fresh service for each test."""
        self.repo = TaskRepository()
        self.service = TaskService(self.repo)
    
    def test_add_task_success(self):
        """Test adding a task successfully."""
        task = self.service.add_task("Test Task", "Test Description")
        
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False
        assert self.repo.get_by_id(task.id) is not None
    
    def test_add_task_without_description(self):
        """Test adding a task without description."""
        task = self.service.add_task("Test Task")
        
        assert task.title == "Test Task"
        assert task.description is None
        assert task.completed is False
    
    def test_add_task_empty_title_error(self):
        """Test that adding a task with empty title raises an error."""
        try:
            self.service.add_task("")
            assert False, "Expected ValueError was not raised"
        except ValueError as e:
            assert "Task title cannot be empty or just whitespace" in str(e)

    def test_add_task_whitespace_only_title_error(self):
        """Test that adding a task with whitespace-only title raises an error."""
        try:
            self.service.add_task("   ")
            assert False, "Expected ValueError was not raised"
        except ValueError as e:
            assert "Task title cannot be empty or just whitespace" in str(e)
    
    def test_delete_task_success(self):
        """Test deleting an existing task."""
        task = self.service.add_task("Test Task")
        
        result = self.service.delete_task(task.id)
        
        assert result is True
        assert self.repo.get_by_id(task.id) is None
    
    def test_delete_task_not_found(self):
        """Test deleting a non-existing task."""
        result = self.service.delete_task("nonexistent")
        
        assert result is False
    
    def test_update_task_success(self):
        """Test updating an existing task."""
        task = self.service.add_task("Original Task", "Original Description")
        
        updated_task = self.service.update_task(task.id, "Updated Task", "Updated Description")
        
        assert updated_task is not None
        assert updated_task.title == "Updated Task"
        assert updated_task.description == "Updated Description"
        
        # Verify the task was actually updated in the repository
        retrieved_task = self.repo.get_by_id(task.id)
        assert retrieved_task.title == "Updated Task"
        assert retrieved_task.description == "Updated Description"
    
    def test_update_task_partial(self):
        """Test updating only some fields of a task."""
        task = self.service.add_task("Original Task", "Original Description")
        
        updated_task = self.service.update_task(task.id, title="Updated Task")
        
        assert updated_task is not None
        assert updated_task.title == "Updated Task"
        assert updated_task.description == "Original Description"
    
    def test_update_task_not_found(self):
        """Test updating a non-existing task."""
        result = self.service.update_task("nonexistent", "Updated Task")
        
        assert result is None
    
    def test_get_task_success(self):
        """Test getting an existing task."""
        task = self.service.add_task("Test Task")
        
        retrieved_task = self.service.get_task(task.id)
        
        assert retrieved_task is not None
        assert retrieved_task.id == task.id
        assert retrieved_task.title == "Test Task"
    
    def test_get_task_not_found(self):
        """Test getting a non-existing task."""
        result = self.service.get_task("nonexistent")
        
        assert result is None
    
    def test_get_all_tasks_empty(self):
        """Test getting all tasks when none exist."""
        tasks = self.service.get_all_tasks()
        
        assert len(tasks) == 0
    
    def test_get_all_tasks_with_tasks(self):
        """Test getting all tasks when some exist."""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        
        tasks = self.service.get_all_tasks()
        
        assert len(tasks) == 2
        task_ids = [task.id for task in tasks]
        assert task1.id in task_ids
        assert task2.id in task_ids
    
    def test_mark_task_complete_success(self):
        """Test marking an existing task as complete."""
        task = self.service.add_task("Test Task")
        assert task.completed is False
        
        completed_task = self.service.mark_task_complete(task.id)
        
        assert completed_task is not None
        assert completed_task.completed is True
        
        # Verify the task was actually updated in the repository
        retrieved_task = self.repo.get_by_id(task.id)
        assert retrieved_task.completed is True
    
    def test_mark_task_complete_not_found(self):
        """Test marking a non-existing task as complete."""
        result = self.service.mark_task_complete("nonexistent")
        
        assert result is None
    
    def test_mark_task_incomplete_success(self):
        """Test marking an existing task as incomplete."""
        task = self.service.add_task("Test Task")
        # First mark it complete
        self.service.mark_task_complete(task.id)
        assert task.completed is True
        
        incomplete_task = self.service.mark_task_incomplete(task.id)
        
        assert incomplete_task is not None
        assert incomplete_task.completed is False
        
        # Verify the task was actually updated in the repository
        retrieved_task = self.repo.get_by_id(task.id)
        assert retrieved_task.completed is False
    
        def test_mark_task_incomplete_not_found(self):
    
            """Test marking a non-existing task as incomplete."""
    
            result = self.service.mark_task_incomplete("nonexistent")
    
            
    
            assert result is None
    
    
    
    if __name__ == "__main__":
    
        pytest.main()
    
    