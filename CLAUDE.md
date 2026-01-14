# Claude Code Instructions for Todo Application

## Overview

This document provides instructions for Claude when working on the Todo Application project.

## Project Structure

- `src/` - Contains all source code
  - `models/` - Data models (Task, etc.)
    - `task.py` - Task data model with id, title, description, and completion status
  - `repositories/` - Data access layer
    - `task_repository.py` - In-memory storage for tasks
  - `services/` - Business logic
    - `task_service.py` - Task operations and validation
  - `interfaces/` - User interface (console)
    - `console_interface.py` - Command-line interface for user interaction
- `tests/` - Test files
  - `test_task.py` - Tests for Task model
  - `test_task_repository.py` - Tests for TaskRepository
  - `test_task_service.py` - Tests for TaskService
  - `test_console_interface.py` - Tests for ConsoleInterface
  - `test_integration.py` - Integration tests
- `pyproject.toml` - Project dependencies and configuration

## Coding Standards

1. Follow Python PEP 8 style guidelines
2. Use meaningful variable and function names
3. Include docstrings for all classes and functions
4. Write comprehensive unit tests
5. Use type hints where appropriate

## Implementation Guidelines

1. Maintain separation of concerns between layers (models, repositories, services, interfaces)
2. Implement proper error handling throughout the application
3. Follow the specifications provided in the `/specs` directory
4. Ensure all 5 Basic Level features are implemented:
   - Add Task
   - Delete Task
   - Update Task
   - View Task List
   - Mark as Complete

## Testing

1. Write unit tests for all components
2. Ensure test coverage is above 80%
3. Test both positive and negative scenarios
4. Test edge cases and error conditions

## Security Considerations

1. Validate all user inputs
2. Handle errors gracefully without exposing internal details
3. Follow secure coding practices

## Performance Considerations

1. Optimize for readability and maintainability
2. Consider performance implications of data structures and algorithms
3. Implement efficient data access patterns

## Phase I Specifics

The Phase I console application implements:
- In-memory storage using Python data structures
- Command-line interface for user interaction
- All 5 Basic Level features as specified
- Clean separation of concerns between models, repositories, services, and interfaces