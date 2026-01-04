# Todo Application - Project Overview

## Project Description
A comprehensive todo application that evolves from a simple in-memory console application (Phase I) to a full-stack web application with multi-user support and persistent storage (Phase II). The application follows spec-driven development principles using Claude Code and Spec-Kit Plus.

## Project Phases

### Phase I: Todo In-Memory Python Console App
- Build a command-line todo application that stores tasks in memory
- Implement all 5 Basic Level features (Add, Delete, Update, View, Mark Complete)
- Use spec-driven development with Claude Code and Spec-Kit Plus
- Follow clean code principles and proper Python project structure

### Phase II: Todo Full-Stack Web Application
- Transform the console app into a modern multi-user web application with persistent storage
- Implement all 5 Basic Level features as a web application
- Create RESTful API endpoints
- Build responsive frontend interface
- Store data in Neon Serverless PostgreSQL database
- Authentication with Better Auth using JWT tokens

## Feature Progression

### Basic Level (Core Essentials)
1. Add Task - Create new todo items
2. Delete Task - Remove tasks from the list
3. Update Task - Modify existing task details
4. View Task List - Display all tasks
5. Mark as Complete - Toggle task completion status

### Intermediate Level (Organization & Usability)
1. Priorities & Tags/Categories - Assign levels (high/medium/low) or labels (work/home)
2. Search & Filter - Search by keyword; filter by status, priority, or date
3. Sort Tasks - Reorder by due date, priority, or alphabetically

### Advanced Level (Intelligent Features)
1. Recurring Tasks - Auto-reschedule repeating tasks (e.g., "weekly meeting")
2. Due Dates & Time Reminders - Set deadlines with date/time pickers; browser notifications

## Technology Stack

### Phase I
- UV
- Python 3.13+
- Claude Code
- Spec-Kit Plus

### Phase II
- Frontend: Next.js 16+ (App Router)
- Backend: Python FastAPI
- ORM: SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth
- Spec-Driven: Claude Code + Spec-Kit Plus

## Deliverables
1. GitHub repository with:
   - Constitution file
   - Specs history folder containing all specification files
   - /src folder with Python source code
   - README.md with setup instructions
   - CLAUDE.md with Claude Code instructions
2. Working console application demonstrating core features
3. Full-stack web application with multi-user support and authentication