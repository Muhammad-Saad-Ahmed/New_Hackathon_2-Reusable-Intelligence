# Running the Backend Application

This document explains how to properly run the backend application for the Todo Application.

## Prerequisites

Before running the backend application, ensure you have:

1. Python 3.10 or higher installed
2. The required dependencies installed via `pip install -e .` or `uv sync`
3. A `.env` file with the required environment variables (see below)

## Required Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# For SQLite (default):
DATABASE_URL=sqlite:///./todo_app.db

# For PostgreSQL (recommended for production):
# DATABASE_URL=postgresql://username:password@localhost:5432/todo_db

BETTER_AUTH_SECRET=your-super-secret-jwt-key-here
SERVER_HOST=127.0.0.1
SERVER_PORT=8000
DEBUG=true
```

## Database Configuration

The application is configured to work with both SQLite and PostgreSQL databases:

- **SQLite**: Used by default for development (file-based, no setup required)
- **PostgreSQL**: Recommended for production environments (requires PostgreSQL server setup)

To switch between databases, simply change the `DATABASE_URL` environment variable:
- For SQLite: `sqlite:///./todo_app.db`
- For PostgreSQL: `postgresql://username:password@hostname:port/database_name`

The application uses SQLAlchemy as the database abstraction layer, which ensures compatibility with both database systems.

## Database Table Creation

The application automatically creates required database tables when it starts up using SQLAlchemy's `create_all()` method. This happens in the main application file (`backend/main.py`).

For PostgreSQL, ensure that:
1. The database exists before starting the application
2. The database user has permissions to create tables
3. The connection string is properly formatted

Alternatively, you can manually create the tables by running:
```bash
cd backend
python create_db.py
```

## Running the Application

### Method 1: Using Uvicorn Directly

From the project root directory, run:

```bash
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

### Method 2: Using the Main Module

From the project root directory, run:

```bash
cd backend
python main.py
```

Note: When running `main.py` directly, ensure that the environment variables are set.

## Troubleshooting Common Issues

### Issue: "Import string 'with' must be in format '<module>:<attribute>'"
**Cause**: This error occurs when uvicorn is called with an incorrect import string.
**Solution**: Ensure you're using the correct format `module:app_instance`. For this project, use `backend.main:app`.

### Issue: Import Errors
**Cause**: Python cannot find the required modules.
**Solution**: Ensure you're running from the project root directory and that the PYTHONPATH includes the project root.

### Issue: Port Already in Use
**Cause**: Another process is using the same port.
**Solution**: Change the port in your environment variables or terminate the other process.

## Verifying the Application is Running

Once the application is running, you can verify it's working by visiting:
- Root endpoint: http://127.0.0.1:8000/
- Health check: http://127.0.0.1:8000/health
- API Documentation: http://127.0.0.1:8000/docs (if DEBUG is enabled)

## Stopping the Application

To stop the application, press `Ctrl+C` in the terminal where it's running.