"""
Console interface for the Todo Application.
"""
from src.services.task_service import TaskService
from src.repositories.task_repository import TaskRepository
from src.models.task import Task
from typing import List
import sys


class ConsoleInterface:
    """
    Console interface for user interaction with the Todo Application.
    """
    
    def __init__(self):
        """
        Initialize the console interface with services.
        """
        self.repository = TaskRepository()
        self.service = TaskService(self.repository)
        self.running = True
    
    def display_menu(self):
        """
        Display the main menu options.
        """
        print("\n" + "="*40)
        print("TODO APPLICATION")
        print("="*40)
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. View Task Details")
        print("8. Exit")
        print("="*40)
    
    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.
        
        Returns:
            The user's choice as a string
        """
        try:
            choice = input("Enter your choice (1-8): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nExiting application...")
            return "8"
    
    def handle_add_task(self):
        """
        Handle adding a new task.
        """
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Error: Task title cannot be empty or just whitespace.")
            return

        description = input("Enter task description (optional): ").strip()
        if not description:
            description = None

        try:
            task = self.service.add_task(title, description)
            print(f"Task added successfully! ID: {task.id[:8]}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_list_tasks(self):
        """
        Handle listing all tasks.
        """
        print("\n--- Task List ---")
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            print("No tasks found.")
            return
        
        for task in tasks:
            print(f"  {task}")
    
    def handle_update_task(self):
        """
        Handle updating an existing task.
        """
        print("\n--- Update Task ---")
        task_id = input("Enter task ID to update: ").strip()
        
        task = self.service.get_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        
        print(f"Current task: {task.detailed_str()}")
        
        new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
        if not new_title:
            new_title = None
        
        new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()
        if not new_description:
            new_description = None
        
        updated_task = self.service.update_task(task_id, new_title, new_description)
        if updated_task:
            print("Task updated successfully!")
        else:
            print("Failed to update task.")
    
    def handle_delete_task(self):
        """
        Handle deleting a task.
        """
        print("\n--- Delete Task ---")
        task_id = input("Enter task ID to delete: ").strip()
        
        success = self.service.delete_task(task_id)
        if success:
            print("Task deleted successfully!")
        else:
            print(f"Task with ID {task_id} not found.")
    
    def handle_mark_complete(self):
        """
        Handle marking a task as complete.
        """
        print("\n--- Mark Task Complete ---")
        task_id = input("Enter task ID to mark complete: ").strip()
        
        task = self.service.mark_task_complete(task_id)
        if task:
            print("Task marked as complete!")
        else:
            print(f"Task with ID {task_id} not found.")
    
    def handle_mark_incomplete(self):
        """
        Handle marking a task as incomplete.
        """
        print("\n--- Mark Task Incomplete ---")
        task_id = input("Enter task ID to mark incomplete: ").strip()
        
        task = self.service.mark_task_incomplete(task_id)
        if task:
            print("Task marked as incomplete!")
        else:
            print(f"Task with ID {task_id} not found.")
    
    def handle_view_task(self):
        """
        Handle viewing detailed task information.
        """
        print("\n--- View Task Details ---")
        task_id = input("Enter task ID to view: ").strip()
        
        task = self.service.get_task(task_id)
        if task:
            print("\nTask Details:")
            print(task.detailed_str())
        else:
            print(f"Task with ID {task_id} not found.")
    
    def handle_exit(self):
        """
        Handle exiting the application.
        """
        print("Thank you for using the Todo Application!")
        self.running = False
    
    def run(self):
        """
        Run the console interface.
        """
        print("Welcome to the Todo Application!")
        
        while self.running:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == "1":
                self.handle_add_task()
            elif choice == "2":
                self.handle_list_tasks()
            elif choice == "3":
                self.handle_update_task()
            elif choice == "4":
                self.handle_delete_task()
            elif choice == "5":
                self.handle_mark_complete()
            elif choice == "6":
                self.handle_mark_incomplete()
            elif choice == "7":
                self.handle_view_task()
            elif choice == "8":
                self.handle_exit()
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")