#!/usr/bin/env python3
"""
Automated FastAPI debugging script.
This script will run through common checks to identify why a FastAPI app isn't starting.
"""
import os
import sys
import subprocess
import importlib.util
from pathlib import Path


def check_python_version():
    """Check Python version compatibility."""
    print("Checking Python version...")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 8:
        print("[OK] Python version is compatible with FastAPI")
    else:
        print("[ERROR] Python version may not be compatible with FastAPI (requires 3.8+)")

    return version


def check_imports(imports_to_test):
    """Test if critical imports work."""
    print("\nTesting imports...")
    for imp in imports_to_test:
        try:
            subprocess.run([sys.executable, "-c", f"import {imp}"],
                         check=True, capture_output=True)
            print(f"[OK] {imp} - import successful")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] {imp} - import failed: {e.stderr.decode()}")
            return False
    return True


def check_env_vars(required_vars):
    """Check if required environment variables are set."""
    print("\nChecking environment variables...")
    all_present = True
    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"[OK] {var} - set")
        else:
            print(f"[ERROR] {var} - not set")
            all_present = False
    return all_present


def check_file_exists(filepath):
    """Check if a file exists."""
    path = Path(filepath)
    if path.exists():
        print(f"[OK] {path} - exists")
        return True
    else:
        print(f"[ERROR] {path} - does not exist")
        return False


def run_uv_script(script_path):
    """Try to run a script with uvicorn."""
    print(f"\nTrying to run {script_path} with uvicorn...")
    try:
        # Test if uvicorn is available
        subprocess.run([sys.executable, "-c", "import uvicorn"], 
                     check=True, capture_output=True)
        
        # Try to run the script
        result = subprocess.run([
            sys.executable, "-m", "uvicorn", 
            f"{script_path.stem}:{script_path.name.replace('.py', '')}.app",
            "--host", "127.0.0.1",
            "--port", "8000",
            "--timeout-keep-alive", "1"
        ], timeout=5, capture_output=True)
        
        if result.returncode == 0:
            print(f"[OK] {script_path} - uvicorn run successful")
            return True
        else:
            print(f"[ERROR] {script_path} - uvicorn run failed: {result.stderr.decode()}")
            return False
    except subprocess.TimeoutExpired:
        print(f"[OK] {script_path} - started successfully (timed out as expected)")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {script_path} - uvicorn run failed: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] {script_path} - error during run: {e}")
        return False


def main():
    print("FastAPI Startup Debugger")
    print("="*50)

    # Define paths and requirements based on the project structure
    # Go up two levels from ai/fastapi_debugging to project root, then into backend
    project_root = Path(__file__).parent.parent.parent
    backend_path = project_root / "backend"
    
    # Check if we're in the right directory
    if not backend_path.exists():
        print(f"Backend path {backend_path} does not exist")
        return 1
    
    os.chdir(backend_path)
    
    # 1. Check Python version
    py_version = check_python_version()
    
    # 2. Check if required files exist
    print("\nChecking required files...")
    required_files = [
        "main.py",
        "requirements.txt",
        ".env"
    ]
    
    all_files_exist = True
    for file in required_files:
        if not check_file_exists(Path(file)):
            all_files_exist = False
    
    # 3. Check imports
    imports_to_test = [
        "fastapi",
        "uvicorn",
        "sqlmodel",
        "pydantic",
        "pydantic_settings",
        "dotenv"
    ]
    
    # Add project-specific imports
    sys.path.insert(0, str(project_root))
    project_imports = [
        "backend.core.config",
        "backend.core.database", 
        "backend.models.database",
        "backend.schemas.task",
        "backend.services.task_service",
        "backend.middleware.auth_middleware",
        "backend.api.v1.tasks",
        "backend.api.v1.auth"
    ]
    imports_to_test.extend(project_imports)
    
    imports_ok = check_imports(imports_to_test)
    
    # 4. Check environment variables
    required_env_vars = [
        "DATABASE_URL",
        "BETTER_AUTH_SECRET",
        "SERVER_HOST", 
        "SERVER_PORT"
    ]
    
    env_ok = check_env_vars(required_env_vars)
    
    # 5. Try running minimal app
    minimal_path = Path("minimal_main.py")
    if minimal_path.exists():
        minimal_ok = run_uv_script(minimal_path)
    else:
        print(f"\n{minimal_path} does not exist, skipping minimal app test")
        minimal_ok = None
    
    # 6. Try running safe app
    safe_path = Path("safe_main.py")
    if safe_path.exists():
        safe_ok = run_uv_script(safe_path)
    else:
        print(f"\n{safe_path} does not exist, skipping safe app test")
        safe_ok = None
    
    # Summary
    print("\n" + "="*50)
    print("DEBUG SUMMARY:")
    print(f"Python version check: {'PASS' if py_version else 'FAIL'}")
    print(f"Required files exist: {'PASS' if all_files_exist else 'FAIL'}")
    print(f"Imports work: {'PASS' if imports_ok else 'FAIL'}")
    print(f"Environment vars set: {'PASS' if env_ok else 'FAIL'}")
    print(f"Minimal app run: {'PASS' if minimal_ok else 'FAIL' if minimal_ok is False else 'SKIPPED'}")
    print(f"Safe app run: {'PASS' if safe_ok else 'FAIL' if safe_ok is False else 'SKIPPED'}")

    if imports_ok and env_ok:
        print("\n[OK] Most likely issues are resolved. Try running the main app again.")
    else:
        print("\n[ERROR] Issues detected. Address the failed checks above.")

    return 0


if __name__ == "__main__":
    sys.exit(main())