# Todo Application

This is a full-featured todo application with user authentication, built with a FastAPI backend and a Next.js frontend.

## Features

- User registration and login
- Create, read, update, and delete tasks
- Filter tasks by status and priority
- User-specific tasks

## Tech Stack

- **Backend:** FastAPI, PostgreSQL, SQLAlchemy
- **Frontend:** Next.js, React, Tailwind CSS

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 14+
- Docker (optional, for PostgreSQL)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. **Backend Setup:**
-Navigate to the backend directory:
 ```bash
cd backend
 ```
-Install the dependencies:
```bash
pip install -r requirements.txt
```
-Create a .env file and add the required environment variables (see backend/RUNNING_BACKEND.md).
-Run the backend server:
```bash
uvicorn main:app --reload
```
3. **Frontend Setup:**
-Navigate to the frontend directory:
```bash
cd frontend
```
-Install the dependencies:
```bash
npm install
```
-Run the frontend server:
```bash
npm run dev
```
Now you can access the application at http://localhost:3000.
