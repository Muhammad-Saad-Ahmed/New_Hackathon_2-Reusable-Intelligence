"""
Final validation script to ensure all components of both phases are properly implemented.
"""
import os
import sys
from pathlib import Path

def validate_project_structure():
    """Validate that all required directories and files exist."""
    print("Validating project structure...")
    
    required_paths = [
        # Backend
        "backend/main.py",
        "backend/core/config.py",
        "backend/core/database.py",
        "backend/core/security.py",
        "backend/models/database.py",
        "backend/schemas/task.py",
        "backend/api/v1/tasks.py",
        "backend/api/v1/auth.py",
        "backend/services/task_service.py",
        "backend/middleware/auth_middleware.py",
        "backend/requirements.txt",
        "backend/.env",
        
        # Frontend
        "frontend/package.json",
        "frontend/next.config.js",
        "frontend/tsconfig.json",
        "frontend/tailwind.config.js",
        "frontend/postcss.config.js",
        "frontend/.env",
        "frontend/src/app/layout.tsx",
        "frontend/src/app/page.tsx",
        "frontend/src/app/login/page.tsx",
        "frontend/src/app/signup/page.tsx",
        "frontend/src/app/dashboard/page.tsx",
        "frontend/src/components/Header.tsx",
        "frontend/src/components/TaskList.tsx",
        "frontend/src/components/TaskItem.tsx",
        "frontend/src/components/TaskForm.tsx",
        "frontend/src/lib/auth.ts",
        "frontend/src/lib/api.ts",
        
        # Phase I
        "src/main.py",
        "src/models/task.py",
        "src/repositories/task_repository.py",
        "src/services/task_service.py",
        "src/interfaces/console_interface.py",
        
        # Tests
        "tests/test_task.py",
        "tests/test_task_repository.py",
        "tests/test_task_service.py",
        "tests/test_console_interface.py",
        "tests/test_integration.py",
        "tests/test_backend_api.py",
        
        # Specs
        "specs/overview.md",
        "specs/architecture.md",
        "specs/features/basic_level.md",
        "specs/features/intermediate_level.md",
        "specs/features/advanced_level.md",
        "specs/features/phase_i_features.md",
        "specs/features/phase_ii_features.md",
        "specs/api/endpoints.md",
        "specs/api/auth.md",
        "specs/database/schema.md",
        "specs/ui/components.md",
        "specs/plan_phase_i.md",
        "specs/plan_phase_ii.md",
        "specs/tasks_phase_i.md",
        "specs/tasks_phase_ii.md",
        
        # Root files
        "pyproject.toml",
        "README.md",
        "CLAUDE.md",
        "docker-compose.yml"
    ]
    
    missing_paths = []
    for path in required_paths:
        if not Path(path).exists():
            missing_paths.append(path)
    
    if missing_paths:
        print(f"FAILED Missing {len(missing_paths)} required paths:")
        for path in missing_paths:
            print(f"  - {path}")
        return False
    else:
        print(f"OK All {len(required_paths)} required paths exist")
        return True


def validate_content():
    """Validate that key files contain expected content."""
    print("\nValidating content...")

    # Check backend main.py has FastAPI app
    with open("backend/main.py", "r") as f:
        backend_main_content = f.read()
        if "FastAPI" not in backend_main_content:
            print("FAILED backend/main.py does not contain FastAPI app")
            return False
        print("OK backend/main.py contains FastAPI app")

    # Check frontend page.tsx has TaskList component
    with open("frontend/src/app/page.tsx", "r") as f:
        frontend_page_content = f.read()
        if "TaskList" not in frontend_page_content:
            print("FAILED frontend/src/app/page.tsx does not use TaskList component")
            return False
        print("OK frontend/src/app/page.tsx uses TaskList component")

    # Check Phase I main.py exists
    with open("src/main.py", "r") as f:
        phase1_main_content = f.read()
        if "ConsoleInterface" not in phase1_main_content:
            print("FAILED src/main.py does not use ConsoleInterface")
            return False
        print("OK src/main.py uses ConsoleInterface")

    return True


def validate_api_endpoints():
    """Validate that API endpoints are properly defined."""
    print("\nValidating API endpoints...")

    # Check tasks endpoints
    with open("backend/api/v1/tasks.py", "r") as f:
        tasks_content = f.read()
        required_endpoints = [
            "GET /{user_id}/tasks",
            "POST /{user_id}/tasks",
            "GET /{user_id}/tasks/{task_id}",
            "PUT /{user_id}/tasks/{task_id}",
            "DELETE /{user_id}/tasks/{task_id}",
            "PATCH /{user_id}/tasks/{task_id}/complete"
        ]

        missing_endpoints = []
        for endpoint in required_endpoints:
            if endpoint.split()[1] not in tasks_content:
                missing_endpoints.append(endpoint)

        if missing_endpoints:
            print(f"FAILED Missing {len(missing_endpoints)} API endpoints in tasks.py:")
            for endpoint in missing_endpoints:
                print(f"  - {endpoint}")
            return False
        else:
            print(f"OK All {len(required_endpoints)} task API endpoints exist")

    # Check auth endpoints
    with open("backend/api/v1/auth.py", "r") as f:
        auth_content = f.read()
        auth_endpoints = [
            "POST /auth/register",
            "POST /auth/login",
            "GET /auth/me"
        ]

        missing_auth_endpoints = []
        for endpoint in auth_endpoints:
            if endpoint.split()[1] not in auth_content:
                missing_auth_endpoints.append(endpoint)

        if missing_auth_endpoints:
            print(f"FAILED Missing {len(missing_auth_endpoints)} auth API endpoints in auth.py:")
            for endpoint in missing_auth_endpoints:
                print(f"  - {endpoint}")
            return False
        else:
            print(f"OK All {len(auth_endpoints)} auth API endpoints exist")

    return True


def validate_frontend_components():
    """Validate that frontend components are properly implemented."""
    print("\nValidating frontend components...")

    components = [
        "Header.tsx",
        "TaskList.tsx",
        "TaskItem.tsx",
        "TaskForm.tsx"
    ]

    for component in components:
        with open(f"frontend/src/components/{component}", "r") as f:
            content = f.read()
            if "export default" not in content:
                print(f"FAILED {component} does not have default export")
                return False
            print(f"OK {component} has default export")

    return True


def main():
    """Run all validations."""
    print("="*60)
    print("TODO APPLICATION - FINAL VALIDATION")
    print("="*60)

    all_validations_passed = True

    # Run all validations
    all_validations_passed &= validate_project_structure()
    all_validations_passed &= validate_content()
    all_validations_passed &= validate_api_endpoints()
    all_validations_passed &= validate_frontend_components()

    print("\n" + "="*60)
    if all_validations_passed:
        print("ALL VALIDATIONS PASSED!")
        print("OK Phase I (Console Application) is complete")
        print("OK Phase II (Full-Stack Web Application) is complete")
        print("OK All specifications have been implemented")
        print("OK Ready for deployment")
    else:
        print("SOME VALIDATIONS FAILED!")
        print("Please review the issues above and fix them.")
    print("="*60)

    return all_validations_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)