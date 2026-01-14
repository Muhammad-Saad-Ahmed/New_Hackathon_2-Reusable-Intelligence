# FastAPI Startup Issues Debugging Guide

## Root Cause Checklist for FastAPI Startup Issues

### 1. Import-Time Errors
- Circular imports between modules
- Missing dependencies not installed
- Incorrect import paths
- Syntax errors in imported modules

### 2. Configuration Issues
- Missing .env file or environment variables
- Incorrect DATABASE_URL format
- Missing required environment variables
- Invalid configuration values

### 3. Database Connection Problems
- Database server not running
- Incorrect database credentials
- Database URL format issues
- SSL connection problems

### 4. Port Binding Issues
- Port already in use
- Insufficient permissions to bind to port
- Firewall blocking the port

### 5. Dependency Loading Issues
- Version conflicts between packages
- Missing optional dependencies
- Incompatible Python version

### 6. Middleware/Router Initialization Problems
- Incorrect middleware configuration
- Router import errors
- Circular dependencies in middleware

### 7. Windows-Specific Issues
- Path separator issues (forward slash vs backslash)
- File permission problems
- Long path names causing issues

## Safe FastAPI Application Template

```python
"""
Safe FastAPI application template with proper error handling.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv  # Make sure to install python-dotenv
import logging
import sys
import os

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add the project root to the Python path to resolve imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

try:
    # Import after setting up path to avoid import-time errors
    # Add your imports here after verifying they work individually
    # from your_module import your_router
    # from your_core_module import settings
    pass
except ImportError as e:
    logger.error(f"Failed to import required modules: {e}")
    sys.exit(1)
except Exception as e:
    logger.error(f"Unexpected error during imports: {e}")
    sys.exit(1)


# Create the FastAPI app instance
try:
    app = FastAPI(
        title="Your App Title",
        version="1.0.0",
        description="Your App Description",
        openapi_url="/api/v1/openapi.json",
        # Disable docs in production for security
        docs_url="/docs" if os.getenv("DEBUG", "False").lower() == "true" else None,
        redoc_url="/redoc" if os.getenv("DEBUG", "False").lower() == "true" else None,
    )
    logger.info("FastAPI app created successfully")
except Exception as e:
    logger.error(f"Failed to create FastAPI app: {e}")
    sys.exit(1)


# Add CORS middleware - this should be added after app creation
try:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost", "http://localhost:3000"],  # Configure as needed
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    logger.info("CORS middleware added successfully")
except Exception as e:
    logger.error(f"Failed to add CORS middleware: {e}")
    sys.exit(1)


# Include API routers - this should be done after app creation and middleware setup
try:
    # app.include_router(your_router, prefix="/api/v1", tags=["your_tag"])
    logger.info("API routers included successfully")
except Exception as e:
    logger.error(f"Failed to include API routers: {e}")
    sys.exit(1)


@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    """
    return {"message": "Your App", "version": "1.0.0"}


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy", "service": "Your Service"}


if __name__ == "__main__":
    import uvicorn
    
    # Use 127.0.0.1 instead of 0.0.0.0 for Windows compatibility
    host = os.getenv("SERVER_HOST", "127.0.0.1")
    port = int(os.getenv("SERVER_PORT", 8000))
    reload = os.getenv("DEBUG", "False").lower() == "true"
    
    logger.info(f"Starting server on {host}:{port}, reload={reload}")
    
    try:
        uvicorn.run(
            "main:app",  # Use module:app format
            host=host,
            port=port,
            reload=reload,
            # Additional options for Windows compatibility
            workers=1,  # Use single worker for development
        )
    except Exception as e:
        logger.error(f"Failed to start uvicorn server: {e}")
        sys.exit(1)
```

## Debug Commands to Isolate the Issue

### 1. Test Python imports
```bash
cd /path/to/your/project
python -c "from your_core_module import settings; print('Config import successful')"
python -c "from your_database_module import get_db; print('Database import successful')"
# Add more import tests as needed
```

### 2. Test minimal app
```bash
python minimal_main.py
```

### 3. Run with uvicorn directly
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### 4. Check environment variables
```bash
python -c "import os; print('ENV_VAR:', os.getenv('YOUR_ENV_VAR'))"
```

### 5. Check Python version compatibility
```bash
python --version
pip list | grep -i "fastapi\|sqlmodel\|pydantic"
```

## Critical Mistakes That Cause "Connection Refused"

1. **Port binding issues**: The application is not actually starting on the expected port
2. **Import errors**: Syntax errors or missing dependencies preventing the app from initializing
3. **Database connection failures**: App crashes during startup when trying to connect to the database
4. **Configuration errors**: Missing or invalid environment variables causing crashes
5. **Middleware/router initialization errors**: Problems during app setup phase

## Where NOT to Initialize Components

- **Don't initialize database connections at import time** - do it during app startup or as a dependency
- **Don't create JWT tokens at import time** - create them during authentication requests
- **Don't perform network calls at import time** - these should happen during request processing
- **Don't load large data structures at import time** - these should be loaded on-demand or cached appropriately

## Recommended Python Version

For FastAPI projects, Python 3.8+ is recommended. Python 3.13 is very new and may have compatibility issues with some dependencies. If experiencing issues, consider using Python 3.11 or 3.12.

## Windows-Specific Considerations

1. Use `127.0.0.1` instead of `0.0.0.0` when possible for Windows compatibility
2. Ensure file paths use the correct separator or use `os.path.join()` or `pathlib`
3. Check that your antivirus software isn't blocking the port
4. Consider running the command prompt as administrator if there are permission issues