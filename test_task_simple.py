"""
Simple test script for the Task model.
"""
from datetime import datetime
from src.models.task import Task


def test_task():
    print("Testing Task model...")
    
    # Test 1: Create a task with required fields
    print("\n1. Testing task creation with required fields...")
    task = Task(id="1", title="Test Task")
    
    assert task.id == "1"
    assert task.title == "Test Task"
    assert task.description is None
    assert task.completed is False
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)
    print("   OK Task creation with required fields works")
    
    # Test 2: Create a task with all fields
    print("\n2. Testing task creation with all fields...")
    task2 = Task(
        id="2", 
        title="Test Task 2", 
        description="Test Description", 
        completed=False
    )
    
    assert task2.id == "2"
    assert task2.title == "Test Task 2"
    assert task2.description == "Test Description"
    assert task2.completed is False
    print("   OK Task creation with all fields works")
    
    # Test 3: Test UUID generation when no ID provided
    print("\n3. Testing UUID generation when no ID provided...")
    task3 = Task(id="", title="Test Task 3")
    
    assert task3.id != ""
    assert len(task3.id) == 36  # UUID4 length
    print("   OK UUID generation works")
    
    # Test 4: Test marking complete
    print("\n4. Testing mark complete...")
    task4 = Task(id="4", title="Test Task 4")
    task4.mark_complete()
    
    assert task4.completed is True
    print("   OK Mark complete works")
    
    # Test 5: Test marking incomplete
    print("\n5. Testing mark incomplete...")
    task5 = Task(id="5", title="Test Task 5", completed=True)
    task5.mark_incomplete()
    
    assert task5.completed is False
    print("   OK Mark incomplete works")
    
    # Test 6: Test updating task
    print("\n6. Testing update task...")
    task6 = Task(id="6", title="Test Task 6", description="Old Description")
    task6.update(title="New Title", description="New Description")
    
    assert task6.title == "New Title"
    assert task6.description == "New Description"
    print("   OK Update task works")
    
    # Test 7: Test updating task partially
    print("\n7. Testing update task partially...")
    task7 = Task(id="7", title="Test Task 7", description="Old Description")
    task7.update(title="New Title")
    
    assert task7.title == "New Title"
    assert task7.description == "Old Description"
    print("   OK Update task partially works")
    
    # Test 8: Test string representation
    print("\n8. Testing string representation...")
    task8 = Task(id="8", title="Test Task 8", completed=False)
    str_repr = str(task8)
    
    assert "O" in str_repr  # Incomplete marker
    assert "Test Task 8" in str_repr
    print(f"   OK String representation: {str_repr}")
    
    # Test 9: Test completed string representation
    print("\n9. Testing completed string representation...")
    task9 = Task(id="9", title="Test Task 9", completed=True)
    str_repr = str(task9)
    
    assert "X" in str_repr  # Complete marker
    assert "Test Task 9" in str_repr
    print(f"   OK Completed string representation: {str_repr}")
    
    # Test 10: Test detailed string representation
    print("\n10. Testing detailed string representation...")
    task10 = Task(id="10", title="Test Task 10", description="Test Description", completed=True)
    detailed_str = task10.detailed_str()
    
    assert "ID: 10" in detailed_str
    assert "Title: Test Task 10" in detailed_str
    assert "Description: Test Description" in detailed_str
    assert "Status: Completed" in detailed_str
    print("   OK Detailed string representation works")
    
    print("\nAll tests passed! OK")


if __name__ == "__main__":
    test_task()