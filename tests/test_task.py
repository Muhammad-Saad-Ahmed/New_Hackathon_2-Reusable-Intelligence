"""
Tests for the Task model.
"""
import pytest
from datetime import datetime
from src.models.task import Task


class TestTask:
    """Test cases for the Task model."""
    
    def test_task_creation_with_required_fields(self):
        """Test creating a task with required fields."""
        task = Task(id="1", title="Test Task")
        
        assert task.id == "1"
        assert task.title == "Test Task"
        assert task.description is None
        assert task.completed is False
        assert isinstance(task.created_at, datetime)
        assert isinstance(task.updated_at, datetime)
    
    def test_task_creation_with_all_fields(self):
        """Test creating a task with all fields."""
        task = Task(
            id="1", 
            title="Test Task", 
            description="Test Description", 
            completed=False
        )
        
        assert task.id == "1"
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False
    
    def test_task_creation_with_uuid_generation(self):
        """Test that a UUID is generated when no ID is provided."""
        task = Task(id="", title="Test Task")
        
        assert task.id != ""
        assert len(task.id) == 36  # UUID4 length
    
    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = Task(id="1", title="Test Task")
        
        task.mark_complete()
        
        assert task.completed is True
    
    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task = Task(id="1", title="Test Task", completed=True)
        
        task.mark_incomplete()
        
        assert task.completed is False
    
    def test_update_task(self):
        """Test updating task details."""
        task = Task(id="1", title="Test Task", description="Old Description")
        
        task.update(title="New Title", description="New Description")
        
        assert task.title == "New Title"
        assert task.description == "New Description"
    
    def test_update_task_partial(self):
        """Test updating only some task details."""
        task = Task(id="1", title="Test Task", description="Old Description")
        
        task.update(title="New Title")
        
        assert task.title == "New Title"
        assert task.description == "Old Description"
    
    def test_str_representation(self):
        """Test string representation of the task."""
        task = Task(id="1", title="Test Task", completed=False)
        
        str_repr = str(task)
        
        assert "O" in str_repr  # Incomplete marker
        assert "Test Task" in str_repr
    
    def test_completed_str_representation(self):
        """Test string representation of a completed task."""
        task = Task(id="1", title="Test Task", completed=True)
        
        str_repr = str(task)
        
        assert "X" in str_repr  # Complete marker
        assert "Test Task" in str_repr
    
    def test_detailed_str_representation(self):
        """Test detailed string representation of the task."""
        task = Task(id="1", title="Test Task", description="Test Description", completed=True)
        
        detailed_str = task.detailed_str()
        
        assert "ID: 1" in detailed_str
        assert "Title: Test Task" in detailed_str
        assert "Description: Test Description" in detailed_str
        assert "Status: Completed" in detailed_str