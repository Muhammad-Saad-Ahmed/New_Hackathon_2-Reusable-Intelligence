"""
Integration tests for the Todo Application.
"""
from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.services.task_service import TaskService
from src.interfaces.console_interface import ConsoleInterface


class TestIntegration:
    """Integration tests for the Todo Application."""
    
    def setup_method(self):
        """Set up fresh components for each test."""
        self.repo = TaskRepository()
        self.service = TaskService(self.repo)
        self.interface = ConsoleInterface()
    
    def test_full_task_lifecycle(self):
        """Test the complete lifecycle of a task through all layers."""
        # Add a task through the service
        task = self.service.add_task("Integration Test Task", "Integration Test Description")
        
        # Verify it was created
        assert task is not None
        assert task.title == "Integration Test Task"
        assert task.description == "Integration Test Description"
        assert task.completed is False
        
        # Retrieve the task through the service
        retrieved_task = self.service.get_task(task.id)
        assert retrieved_task is not None
        assert retrieved_task.id == task.id
        
        # Update the task through the service
        updated_task = self.service.update_task(task.id, "Updated Integration Test Task")
        assert updated_task is not None
        assert updated_task.title == "Updated Integration Test Task"
        
        # Mark the task as complete through the service
        completed_task = self.service.mark_task_complete(task.id)
        assert completed_task is not None
        assert completed_task.completed is True
        
        # Mark the task as incomplete through the service
        incomplete_task = self.service.mark_task_incomplete(task.id)
        assert incomplete_task is not None
        assert incomplete_task.completed is False
        
        # Delete the task through the service
        delete_result = self.service.delete_task(task.id)
        assert delete_result is True
        
        # Verify the task is gone
        deleted_task = self.service.get_task(task.id)
        assert deleted_task is None
    
    def test_get_all_tasks(self):
        """Test retrieving all tasks through the service."""
        # Add multiple tasks
        task1 = self.service.add_task("Task 1", "Description 1")
        task2 = self.service.add_task("Task 2", "Description 2")
        task3 = self.service.add_task("Task 3", "Description 3")
        
        # Retrieve all tasks
        all_tasks = self.service.get_all_tasks()
        
        # Verify all tasks are returned
        assert len(all_tasks) == 3
        task_ids = [task.id for task in all_tasks]
        assert task1.id in task_ids
        assert task2.id in task_ids
        assert task3.id in task_ids
    
    def test_repository_service_consistency(self):
        """Test that repository and service are consistent."""
        # Add a task directly to repository
        task = Task(id="test_id", title="Direct Repository Task")
        self.repo.create(task)
        
        # Retrieve through service
        retrieved_task = self.service.get_task("test_id")
        assert retrieved_task is not None
        assert retrieved_task.title == "Direct Repository Task"
        
        # Update through service
        updated_task = self.service.update_task("test_id", "Updated Through Service")
        assert updated_task is not None
        assert updated_task.title == "Updated Through Service"
        
        # Verify update is reflected in repository
        repo_task = self.repo.get_by_id("test_id")
        assert repo_task.title == "Updated Through Service"
    
    def test_console_interface_components_connected(self):
        """Test that all components in ConsoleInterface are properly connected."""
        # Verify that the interface has all required components
        assert self.interface.repository is not None
        assert self.interface.service is not None
        assert self.interface.service.repository == self.interface.repository
        
        # Add a task through the interface's service
        task = self.interface.service.add_task("Interface Test Task")
        assert task is not None
        
        # Verify it's accessible through the interface's repository
        retrieved_task = self.interface.repository.get_by_id(task.id)
        assert retrieved_task is not None
        assert retrieved_task.title == "Interface Test Task"
    
    def test_error_handling_consistency(self):
        """Test that errors are handled consistently across layers."""
        # Try to retrieve a non-existent task from service
        result = self.service.get_task("nonexistent")
        assert result is None
        
        # Try to update a non-existent task
        result = self.service.update_task("nonexistent", "New Title")
        assert result is None
        
        # Try to delete a non-existent task
        result = self.service.delete_task("nonexistent")
        assert result is False
        
        # Try to mark a non-existent task as complete
        result = self.service.mark_task_complete("nonexistent")
        assert result is None
        
        # Try to mark a non-existent task as incomplete
        result = self.service.mark_task_incomplete("nonexistent")
        assert result is None