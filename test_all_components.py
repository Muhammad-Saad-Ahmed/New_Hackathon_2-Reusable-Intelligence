"""
Comprehensive test to verify all components of Phase I work together.
"""
import subprocess
from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.services.task_service import TaskService
from src.interfaces.console_interface import ConsoleInterface


def test_all_components():
    print("Testing all components of Phase I...")
    
    # Test 1: Task model
    print("\n1. Testing Task model...")
    task = Task(id="", title="Test Task", description="Test Description")
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False
    print("   OK Task model works")
    
    # Test 2: Task repository
    print("\n2. Testing Task repository...")
    repo = TaskRepository()
    repo.create(task)
    retrieved_task = repo.get_by_id(task.id)
    assert retrieved_task is not None
    assert retrieved_task.title == "Test Task"
    print("   OK Task repository works")
    
    # Test 3: Task service
    print("\n3. Testing Task service...")
    service = TaskService(repo)
    new_task = service.add_task("New Task", "New Description")
    assert new_task.title == "New Task"
    assert new_task.description == "New Description"
    
    # Test update
    updated_task = service.update_task(new_task.id, title="Updated Task")
    assert updated_task.title == "Updated Task"
    assert updated_task.description == "New Description"
    
    # Test mark complete
    completed_task = service.mark_task_complete(new_task.id)
    assert completed_task.completed is True
    print("   OK Task service works")
    
    # Test 4: Console interface
    print("\n4. Testing Console interface...")
    console_interface = ConsoleInterface()
    assert console_interface.repository is not None
    assert console_interface.service is not None
    assert console_interface.running is True
    print("   OK Console interface works")
    
    # Test 5: Integration
    print("\n5. Testing integration...")
    # Add a task
    task1 = console_interface.service.add_task("Integration Task", "Integration Description")
    assert task1 is not None
    
    # Retrieve all tasks
    all_tasks = console_interface.service.get_all_tasks()
    assert len(all_tasks) >= 1
    
    # Find our specific task
    found_task = console_interface.service.get_task(task1.id)
    assert found_task is not None
    assert found_task.title == "Integration Task"
    print("   OK Integration works")
    
    print("\nAll components test passed! OK")


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
    test_all_components()
    test_phase_ii()

if __name__ == "__main__":
    main()