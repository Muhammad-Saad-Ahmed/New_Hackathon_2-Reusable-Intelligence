# Todo Application - Architecture Specification

## System Architecture Overview

The Todo application is designed as a two-phase evolution:
1. Phase I: A standalone Python console application with in-memory storage
2. Phase II: A full-stack web application with multi-user support, persistent storage, and authentication

## Phase I Architecture: Console Application

### Components
- **Main Application**: Entry point for the console application
- **Task Service**: Business logic for task operations (add, delete, update, view, mark complete)
- **Task Repository**: In-memory storage for tasks
- **Console Interface**: Command-line interface for user interaction
- **Task Model**: Data structure representing a task

### Technology Stack
- Python 3.13+
- UV for package management
- Standard Python libraries

### Data Flow
1. User inputs command via console
2. Console Interface parses command
3. Task Service processes business logic
4. Task Repository handles data operations
5. Results returned to Console Interface for display

## Phase II Architecture: Full-Stack Web Application

### Frontend Architecture (Next.js 16+)
- **App Router**: Next.js 16+ routing system
- **React Components**: UI components for task management
- **API Client**: Service layer for API communication
- **Authentication Client**: Better Auth integration
- **State Management**: Client-side state management

### Backend Architecture (FastAPI)
- **API Routes**: RESTful endpoints for task operations
- **Authentication Middleware**: JWT token verification
- **Business Logic Layer**: Task operations and validation
- **Data Access Layer**: SQLModel ORM operations
- **Database Models**: SQLModel entity definitions

### Technology Stack
- **Frontend**: Next.js 16+, React, Better Auth
- **Backend**: Python FastAPI
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT tokens

### Data Flow
1. User interacts with frontend UI
2. Frontend makes authenticated API requests
3. JWT token verified by authentication middleware
4. Business logic processes request
5. Database operations via SQLModel
6. Response returned to frontend
7. UI updates based on response

## Authentication Architecture

### JWT Token Flow
1. User logs in via Better Auth on frontend
2. Better Auth issues JWT token
3. Frontend includes JWT in Authorization header for API requests
4. FastAPI backend verifies JWT signature using shared secret
5. User identity extracted from token
6. Request validated against user permissions
7. User-specific data returned

### Security Considerations
- All API endpoints require valid JWT token
- User data is isolated by user ID
- JWT tokens have automatic expiration
- Stateless authentication mechanism

## Database Architecture

### Schema Design
- **Users Table**: Stores user information
- **Tasks Table**: Stores task information with foreign key to user
- Indexes on frequently queried fields

### Connection Management
- Neon Serverless PostgreSQL connection pooling
- SQLModel for ORM operations
- Connection security via environment variables

## API Architecture

### RESTful Design Principles
- Resource-based URLs
- Standard HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Consistent response formats
- Proper HTTP status codes

### Endpoints
- GET /api/{user_id}/tasks - List all tasks
- POST /api/{user_id}/tasks - Create a new task
- GET /api/{user_id}/tasks/{id} - Get task details
- PUT /api/{user_id}/tasks/{id} - Update a task
- DELETE /api/{user_id}/tasks/{id} - Delete a task
- PATCH /api/{user_id}/tasks/{id}/complete - Toggle completion

## Deployment Architecture

### Phase I
- Standalone Python application
- Executable via command line
- No external dependencies beyond Python environment

### Phase II
- Frontend: Next.js static site or server-side rendering
- Backend: FastAPI application server
- Database: Neon Serverless PostgreSQL
- Environment configuration via environment variables