# Todo Application

A full-stack todo application with both console and web interfaces, built with Python and Next.js.

## Overview

This project consists of two phases:

### Phase I: Console Application
A simple console-based todo application that allows users to manage their tasks. It supports the following basic operations:

1. Add tasks
2. Delete tasks
3. Update tasks
4. View task list
5. Mark tasks as complete/incomplete

### Phase II: Full-Stack Web Application
A modern multi-user web application with persistent storage and authentication:

- Frontend: Next.js 16+ with App Router
- Backend: Python FastAPI
- ORM: SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT tokens

## Setup

### Phase I Setup
1. Ensure you have Python 3.13+ installed
2. Clone this repository
3. Install dependencies using UV:
   ```bash
   uv sync
   ```

### Phase II Setup
1. Ensure you have Node.js and npm installed
2. Navigate to the frontend directory:
   ```bash
   cd frontend
   npm install
   ```
3. Navigate to the backend directory:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

## Usage

### Phase I: Console Application
To run the console application:

```bash
python -m src.main
```

### Phase II: Full-Stack Application
1. Start the backend:
   ```bash
   cd backend
   python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

   Alternatively, from the project root directory:
   ```bash
   python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
   ```
2. In a new terminal, start the frontend:
   ```bash
   cd frontend
   npm run dev
   ```

## Features

### Basic Level Features
- **Add Task**: Create new todo items with title and description
- **Delete Task**: Remove tasks from the list
- **Update Task**: Modify existing task details
- **View Task List**: Display all tasks with status indicators
- **Mark as Complete**: Toggle task completion status

### Intermediate Level Features
- **Priorities & Tags/Categories**: Assign priority levels (high/medium/low) or labels (work/home)
- **Search & Filter**: Search by keyword; filter by status, priority, or date
- **Sort Tasks**: Reorder by due date, priority, or alphabetically

### Architecture
The application follows a clean architecture with separation of concerns:
#### Phase I Architecture
- **Models**: Define the data structures (Task model)
- **Repositories**: Handle data storage and retrieval (in-memory)
- **Services**: Contain business logic for task operations
- **Interfaces**: Provide user interaction (console interface)

#### Phase II Architecture
- **Frontend**: Next.js 16+ with React components
- **Backend**: FastAPI with SQLModel ORM
- **Authentication**: Better Auth with JWT token verification
- **Database**: PostgreSQL with Neon Serverless

## API Endpoints (Phase II)

### Authentication
- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login a user
- `GET /api/v1/auth/me` - Get current user info

### Tasks
- `GET /api/v1/{user_id}/tasks` - List all tasks
- `POST /api/v1/{user_id}/tasks` - Create a new task
- `GET /api/v1/{user_id}/tasks/{id}` - Get task details
- `PUT /api/v1/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/v1/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/v1/{user_id}/tasks/{id}/complete` - Toggle completion

## Project Structure

```
todo-app/
├── backend/                 # Phase II backend (FastAPI)
│   ├── main.py              # FastAPI application entry point
│   ├── core/                # Configuration, security, database
│   │   ├── config.py        # Configuration settings
│   │   ├── database.py      # Database connection and session management
│   │   └── security.py      # JWT authentication utilities
│   ├── models/              # SQLModel database models
│   ├── schemas/             # Pydantic schemas for API requests/responses
│   ├── api/                 # API routes
│   │   └── v1/              # API version 1
│   │       ├── auth.py      # Authentication endpoints
│   │       └── tasks.py     # Task-related endpoints
│   ├── services/            # Business logic
│   │   └── task_service.py  # Task operations and validation
│   └── middleware/          # Authentication middleware
│       └── auth_middleware.py # JWT token validation middleware
├── frontend/                # Phase II frontend (Next.js)
│   ├── package.json         # Frontend dependencies
│   ├── next.config.js       # Next.js configuration
│   ├── tsconfig.json        # TypeScript configuration
│   ├── tailwind.config.js   # Tailwind CSS configuration
│   ├── postcss.config.js    # PostCSS configuration
│   ├── .env                 # Environment variables
│   └── src/
│       ├── app/             # Next.js App Router pages
│       │   ├── layout.tsx   # Root layout component
│       │   ├── page.tsx     # Home page
│       │   ├── login/       # Login page
│       │   ├── signup/      # Signup page
│       │   └── dashboard/   # Dashboard page
│       ├── components/      # React components
│       │   ├── Header.tsx   # Header component
│       │   ├── TaskList.tsx # Task list component
│       │   ├── TaskItem.tsx # Task item component
│       │   └── TaskForm.tsx # Task form component
│       ├── lib/             # Utilities (auth, API client)
│       │   ├── auth.ts      # Better Auth integration
│       │   └── api.ts       # API client utilities
│       └── types/           # TypeScript type definitions
│       └── app/             # Next.js App Router pages
├── src/                     # Phase I source code
│   ├── main.py              # Console application entry point
│   ├── models/              # Data models (Task, etc.)
│   │   └── task.py          # Task data model
│   ├── repositories/        # Data access layer
│   │   └── task_repository.py # In-memory storage
│   ├── services/            # Business logic
│   │   └── task_service.py  # Task operations and validation
│   └── interfaces/          # User interface (console)
│       └── console_interface.py # Command-line interface
├── tests/                   # Test files for both phases
│   ├── test_task.py         # Tests for Task model
│   ├── test_task_repository.py # Tests for TaskRepository
│   ├── test_task_service.py # Tests for TaskService
│   ├── test_console_interface.py # Tests for ConsoleInterface
│   ├── test_integration.py  # Integration tests
│   └── test_backend_api.py  # Backend API tests
├── specs/                   # Specifications directory
│   ├── overview.md          # Project overview
│   ├── architecture.md      # Architecture specification
│   ├── features/            # Feature specifications
│   ├── api/                 # API specifications
│   ├── database/            # Database specifications
│   └── ui/                  # UI specifications
├── docker-compose.yml       # Docker configuration for local development
├── pyproject.toml           # Project dependencies and configuration
├── README.md                # This file
└── CLAUDE.md                # Claude Code instructions
```

## Development

### Phase I Testing
To run Phase I tests:

```bash
uv run pytest
```

Or run the specific test files directly:
```bash
python test_all_components.py
python test_final_validation.py
```

### Phase II Development
- Backend: Run the backend server with hot reloading using either:
  - From the project root: `python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload`
  - From the backend directory: `python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload`
- Frontend: Use `npm run dev` in the frontend directory for hot reloading

### Running Tests
For backend API tests:
```bash
python -m pytest tests/test_backend_api.py
```

## Deployment

The application can be deployed using:
- Backend: Any platform that supports Python/FastAPI (e.g., Heroku, AWS, GCP)
- Frontend: Next.js static export or Vercel

## Security

The application implements several security measures:
- JWT token authentication and authorization
- Password hashing with bcrypt
- Input validation and sanitization
- User data isolation by user ID
- Secure token handling with expiration

## License

This project is licensed under the MIT License.