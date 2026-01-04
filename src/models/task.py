from dataclasses import dataclass
from typing import Optional
import uuid
from datetime import datetime


@dataclass
class Task:
    """
    Represents a todo task with properties: id, title, description, and completed status.
    """
    id: str
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        """
        Initialize default values after object creation.
        """
        if self.id is None or self.id == "":
            self.id = str(uuid.uuid4())
        
        if self.created_at is None:
            self.created_at = datetime.now()
        
        if self.updated_at is None:
            self.updated_at = datetime.now()

    def mark_complete(self):
        """
        Mark the task as complete.
        """
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self):
        """
        Mark the task as incomplete.
        """
        self.completed = False
        self.updated_at = datetime.now()

    def update(self, title: Optional[str] = None, description: Optional[str] = None):
        """
        Update the task details.
        """
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the task.
        """
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id[:8]} - {self.title}"
    
    def detailed_str(self):
        """
        Detailed string representation of the task.
        """
        status = "Completed" if self.completed else "Pending"
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description or 'No description'}\nStatus: {status}\nCreated: {self.created_at}\nUpdated: {self.updated_at}"