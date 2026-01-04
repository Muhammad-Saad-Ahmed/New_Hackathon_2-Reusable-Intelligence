# Todo Application - Database Schema Specification

## Overview
This document specifies the database schema for the Phase II Todo web application using Neon Serverless PostgreSQL and SQLModel.

## Database Configuration
- Database: Neon Serverless PostgreSQL
- ORM: SQLModel
- Connection: Environment-based configuration
- Migration: Alembic for schema management

## Tables

### Users Table
Stores user account information.

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

#### Fields
- `id`: Primary key, UUID, auto-generated
- `email`: User's email address, unique, required
- `name`: User's display name, optional
- `created_at`: Timestamp when user was created
- `updated_at`: Timestamp when user was last updated

#### Indexes
- `idx_users_email`: Index on email field for fast lookups

#### Constraints
- `users_email_key`: Email must be unique

---

### Tasks Table
Stores task information with foreign key to users.

```sql
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    priority VARCHAR(20) DEFAULT 'medium', -- 'low', 'medium', 'high'
    tags TEXT[], -- Array of text tags
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

#### Fields
- `id`: Primary key, UUID, auto-generated
- `user_id`: Foreign key to users table, required
- `title`: Task title, required
- `description`: Task description, optional
- `completed`: Completion status, boolean, defaults to false
- `priority`: Task priority, text, defaults to 'medium'
- `tags`: Array of tags for the task
- `created_at`: Timestamp when task was created
- `updated_at`: Timestamp when task was last updated

#### Indexes
- `idx_tasks_user_id`: Index on user_id for fast user-based queries
- `idx_tasks_completed`: Index on completed status for filtering
- `idx_tasks_priority`: Index on priority for sorting/filtering
- `idx_tasks_created_at`: Index on creation time for chronological queries

#### Constraints
- `fk_tasks_user_id`: Foreign key constraint to users table
- `tasks_priority_check`: Check constraint to ensure priority is 'low', 'medium', or 'high'

---

## SQLModel Definitions

### User Model
```python
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False)
    name: Optional[str] = Field(default=None)

class User(UserBase, table=True):
    __tablename__ = "users"
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship to tasks would be defined here if needed
```

### Task Model
```python
from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime
import uuid

class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = Field(default=False)
    priority: Optional[str] = Field(default="medium")  # low, medium, high
    tags: Optional[List[str]] = Field(default=[])

class Task(TaskBase, table=True):
    __tablename__ = "tasks"
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id", ondelete="CASCADE")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

## Relationships
- One user to many tasks (one-to-many)
- Tasks are deleted when their associated user is deleted (CASCADE)

## Indexing Strategy
- Primary indexes on all ID fields
- Foreign key indexes for relationship queries
- Status indexes for filtering (completed, priority)
- Timestamp indexes for chronological queries

## Security Considerations
- All data access must be filtered by user ID
- No direct cross-user data access is possible through proper query construction
- Database constraints enforce referential integrity

## Migration Strategy
- Use Alembic for database schema migrations
- Maintain backward compatibility when possible
- Test migrations on staging before applying to production