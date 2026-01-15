"""
Simple test to verify backend code structure without dependencies.
"""
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./backend'))

def test_backend_structure():
    print("Testing backend code structure...")
    
    # Check if main.py exists and can be imported
    try:
        import main
        print("OK main.py exists and can be imported")
    except ImportError as e:
        print(f"FAILED main.py import error: {e}")
    except Exception as e:
        print(f"FAILED main.py error: {e}")
    
    # Check if core modules exist
    try:
        import core.config
        print("OK config module exists")
    except ImportError as e:
        print(f"FAILED config import error: {e}")
    except Exception as e:
        print(f"FAILED config error: {e}")
    
    try:
        import core.database
        print("OK database module exists")
    except ImportError as e:
        print(f"FAILED database import error: {e}")
    except Exception as e:
        print(f"FAILED database error: {e}")
    
    try:
        import core.security
        print("OK security module exists")
    except ImportError as e:
        print(f"FAILED security import error: {e}")
    except Exception as e:
        print(f"FAILED security error: {e}")
    
    # Check if models exist
    try:
        import models.database
        print("OK database models exist")
    except ImportError as e:
        print(f"FAILED database models import error: {e}")
    except Exception as e:
        print(f"FAILED database models error: {e}")
    
    # Check if schemas exist
    try:
        import schemas.task
        print("OK task schemas exist")
    except ImportError as e:
        print(f"FAILED task schemas import error: {e}")
    except Exception as e:
        print(f"FAILED task schemas error: {e}")
    
    # Check if middleware exists
    try:
        import middleware.auth_middleware
        print("OK auth middleware exists")
    except ImportError as e:
        print(f"FAILED auth middleware import error: {e}")
    except Exception as e:
        print(f"FAILED auth middleware error: {e}")
    
    # Check if services exist
    try:
        import services.task_service
        print("OK task service exists")
    except ImportError as e:
        print(f"FAILED task service import error: {e}")
    except Exception as e:
        print(f"FAILED task service error: {e}")
    
    # Check if API routes exist
    try:
        import api.v1.tasks
        print("OK tasks API exists")
    except ImportError as e:
        print(f"FAILED tasks API import error: {e}")
    except Exception as e:
        print(f"FAILED tasks API error: {e}")
    
    try:
        import api.v1.auth
        print("OK auth API exists")
    except ImportError as e:
        print(f"FAILED auth API import error: {e}")
    except Exception as e:
        print(f"FAILED auth API error: {e}")
    
    print("\nCode structure validation completed!")


if __name__ == "__main__":
    test_backend_structure()