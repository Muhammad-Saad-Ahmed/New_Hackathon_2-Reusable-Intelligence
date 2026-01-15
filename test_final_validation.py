"""
Final validation tests for the Todo Application.
"""
import subprocess
from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.services.task_service import TaskService
from src.interfaces.console_interface import ConsoleInterface


def test_all_basic_level_features():
    """Test all 5 Basic Level features as specified."""
    # Initialize components
    repo = TaskRepository()
    service = TaskService(repo)
    
    # 1. Add Task
    print("Testing: Add Task")
    task = service.add_task("Test Task for Validation", "This is a validation task")
    assert task is not None
    assert task.title == "Test Task for Validation"
    assert task.description == "This is a validation task"
    print("OK Add Task feature works")

    # 2. View Task List
    print("\nTesting: View Task List")
    all_tasks = service.get_all_tasks()
    assert len(all_tasks) >= 1
    task_found = False
    for t in all_tasks:
        if t.id == task.id:
            task_found = True
            break
    assert task_found
    print("OK View Task List feature works")

    # 3. Update Task
    print("\nTesting: Update Task")
    updated_task = service.update_task(task.id, "Updated Test Task", "Updated description")
    assert updated_task is not None
    assert updated_task.title == "Updated Test Task"
    assert updated_task.description == "Updated description"
    print("OK Update Task feature works")

    # 4. Mark as Complete
    print("\nTesting: Mark as Complete")
    completed_task = service.mark_task_complete(task.id)
    assert completed_task is not None
    assert completed_task.completed is True
    print("OK Mark as Complete feature works")

    # 5. Delete Task
    print("\nTesting: Delete Task")
    delete_result = service.delete_task(task.id)
    assert delete_result is True
    deleted_task = service.get_task(task.id)
    assert deleted_task is None
    print("OK Delete Task feature works")

    print("\nAll 5 Basic Level features validated successfully!")


def test_error_handling():
    """Test proper error handling throughout the application."""
    repo = TaskRepository()
    service = TaskService(repo)
    
    print("\nTesting error handling...")
    
    # Test adding task with empty title
    try:
        service.add_task("")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("OK Proper error handling for empty task title")

    # Test operations on non-existent task
    result = service.get_task("nonexistent")
    assert result is None
    print("OK Proper handling for non-existent task retrieval")

    result = service.update_task("nonexistent", "New Title")
    assert result is None
    print("OK Proper handling for non-existent task update")

    result = service.delete_task("nonexistent")
    assert result is False
    print("OK Proper handling for non-existent task deletion")

    result = service.mark_task_complete("nonexistent")
    assert result is None
    print("OK Proper handling for non-existent task completion")

    result = service.mark_task_incomplete("nonexistent")
    assert result is None
    print("OK Proper handling for non-existent task incomplete")


def test_data_integrity():
    """Test that data integrity is maintained."""
    repo = TaskRepository()
    service = TaskService(repo)
    
    print("\nTesting data integrity...")
    
    # Add a task
    original_task = service.add_task("Integrity Test", "Testing data integrity")
    original_id = original_task.id
    
    # Retrieve it
    retrieved_task = service.get_task(original_id)
    assert retrieved_task.id == original_id
    assert retrieved_task.title == "Integrity Test"
    assert retrieved_task.description == "Testing data integrity"
    print("OK Data integrity maintained for create/retrieve")

    # Update it
    updated_task = service.update_task(original_id, "Updated Integrity Test", "Updated description")
    assert updated_task.id == original_id  # ID should remain the same
    assert updated_task.title == "Updated Integrity Test"
    print("OK Data integrity maintained for update")

    # Mark complete/incomplete
    completed_task = service.mark_task_complete(original_id)
    assert completed_task.id == original_id
    assert completed_task.completed is True

    incomplete_task = service.mark_task_incomplete(original_id)
    assert incomplete_task.id == original_id
    assert incomplete_task.completed is False
    print("OK Data integrity maintained for status changes")


def test_application_flow():
    """Test the overall application flow."""
    print("\nTesting application flow...")
    
    # Create the console interface (which creates all components)
    interface = ConsoleInterface()
    
    # Verify all components are properly initialized
    assert interface.repository is not None
    assert interface.service is not None
    assert interface.running is True
    print("OK Console interface properly initialized")

    # Test that services are connected
    assert interface.service.repository == interface.repository
    print("OK Service and repository properly connected")

    # Test a complete workflow
    task = interface.service.add_task("Workflow Test", "Testing complete workflow")
    assert task is not None

    all_tasks = interface.service.get_all_tasks()
    assert len(all_tasks) >= 1

    found_task = interface.service.get_task(task.id)
    assert found_task is not None

    interface.service.delete_task(task.id)
    deleted_task = interface.service.get_task(task.id)
    assert deleted_task is None

    print("OK Complete workflow functions properly")


def test_phase_ii():
    """Run the validation script for Phase II."""
    print("\nTesting Phase II...")
    try:
        result = subprocess.run(["python", "validate_implementation.py"], capture_output=True, text=True, check=True)
        print(result.stdout)
        print("   OK Phase II validation script passed")
    except subprocess.CalledProcessError as e:
        print("   FAILED Phase II validation script failed")
        print(e.stderr)
        raise e

def main():
    print("Running final validation tests...")
    
    test_all_basic_level_features()
    test_error_handling()
    test_data_integrity()
    test_application_flow()
    
    print("\n" + "="*50)
    print("ALL VALIDATION TESTS PASSED! OK")
    print("Phase I implementation is complete and working correctly.")
    print("All 5 Basic Level features are implemented:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. View Task List")
    print("5. Mark as Complete")
    print("="*50)

    test_phase_ii()

if __name__ == "__main__":
    main()