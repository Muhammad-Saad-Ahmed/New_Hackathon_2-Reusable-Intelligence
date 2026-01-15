"""
Test to verify all backend components can be imported without errors.
"""
import sys
import os

# Add the project root and backend directory to the path
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./backend'))


def test_backend_imports():
    print("Testing backend component imports...")
    
    try:
        from main import app
        print("OK FastAPI app imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import FastAPI app: {e}")
        return False

    try:
        from core.config import settings
        print("OK Configuration imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import configuration: {e}")
        return False

    try:
        from core.database import engine, SessionLocal, Base, get_db
        print("OK Database components imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import database components: {e}")
        return False

    try:
        from core.security import create_access_token, verify_token, get_password_hash, verify_password
        print("OK Security utilities imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import security utilities: {e}")
        return False

    try:
        from models.database import User, Task
        from schemas.task import UserBase, TaskBase
        print("OK Database models imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import database models: {e}")
        return False

    try:
        from schemas.task import TaskCreate, TaskUpdate, Task, UserCreate, User
        print("OK Schemas imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import schemas: {e}")
        return False

    try:
        from middleware.auth_middleware import JWTBearer
        print("OK Authentication middleware imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import authentication middleware: {e}")
        return False

    try:
        from services.task_service import TaskService
        print("OK Task service imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import task service: {e}")
        return False

    try:
        from api.v1.tasks import router as tasks_router
        print("OK Tasks API router imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import tasks API router: {e}")
        return False

    try:
        from api.v1.auth import router as auth_router
        print("OK Auth API router imported successfully")
    except Exception as e:
        print(f"FAILED Failed to import auth API router: {e}")
        return False

    print("\nOK All backend components imported successfully!")
    return True


if __name__ == "__main__":
    success = test_backend_imports()
    if success:
        print("\nBackend components validation: PASSED")
    else:
        print("\nBackend components validation: FAILED")