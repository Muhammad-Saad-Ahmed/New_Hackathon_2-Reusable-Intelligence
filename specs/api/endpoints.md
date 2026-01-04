# Todo Application - API Specification

## Overview
This document specifies the RESTful API endpoints for the Phase II Todo web application. All endpoints require authentication via JWT tokens and enforce user data isolation.

## Authentication
All API endpoints (except authentication endpoints) require a valid JWT token in the Authorization header:
```
Authorization: Bearer <jwt_token>
```

The user ID in the token must match the user ID in the URL path. Requests with mismatched user IDs will be rejected.

## Base URL
```
https://api.todoapp.com/api
```

## Common Response Format

### Success Response
```json
{
  "success": true,
  "data": { ... }
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message"
  }
}
```

## HTTP Status Codes
- `200` - Success
- `201` - Created
- `204` - No Content (for deletions)
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `422` - Unprocessable Entity
- `500` - Internal Server Error

## Endpoints

### GET /api/{user_id}/tasks
Retrieve all tasks for a specific user.

#### Path Parameters
- `user_id` (string, required): The ID of the user whose tasks to retrieve

#### Headers
- `Authorization` (string, required): Bearer token with valid JWT

#### Query Parameters
- `status` (string, optional): Filter by status ("completed", "incomplete", "all")
- `priority` (string, optional): Filter by priority ("high", "medium", "low")
- `search` (string, optional): Search term to match against title or description
- `sort` (string, optional): Sort order ("created", "due_date", "priority", "title")
- `order` (string, optional): Sort direction ("asc", "desc")

#### Response
- Status: `200`
- Body:
```json
{
  "success": true,
  "data": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "completed": "boolean",
      "priority": "string",
      "tags": ["string"],
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
}
```

#### Error Responses
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User ID in token doesn't match user_id in URL
- `404`: Not Found - User doesn't exist

---

### POST /api/{user_id}/tasks
Create a new task for a specific user.

#### Path Parameters
- `user_id` (string, required): The ID of the user creating the task

#### Headers
- `Authorization` (string, required): Bearer token with valid JWT

#### Request Body
```json
{
  "title": "string",
  "description": "string",
  "priority": "string",
  "tags": ["string"]
}
```

#### Response
- Status: `201`
- Body:
```json
{
  "success": true,
  "data": {
    "id": "string",
    "title": "string",
    "description": "string",
    "completed": false,
    "priority": "string",
    "tags": ["string"],
    "created_at": "datetime",
    "updated_at": "datetime"
  }
}
```

#### Error Responses
- `400`: Bad Request - Missing required fields or invalid data
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User ID in token doesn't match user_id in URL

---

### GET /api/{user_id}/tasks/{id}
Retrieve a specific task for a user.

#### Path Parameters
- `user_id` (string, required): The ID of the user
- `id` (string, required): The ID of the task to retrieve

#### Headers
- `Authorization` (string, required): Bearer token with valid JWT

#### Response
- Status: `200`
- Body:
```json
{
  "success": true,
  "data": {
    "id": "string",
    "title": "string",
    "description": "string",
    "completed": "boolean",
    "priority": "string",
    "tags": ["string"],
    "created_at": "datetime",
    "updated_at": "datetime"
  }
}
```

#### Error Responses
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User ID in token doesn't match user_id in URL
- `404`: Not Found - Task doesn't exist or doesn't belong to user

---

### PUT /api/{user_id}/tasks/{id}
Update a specific task for a user.

#### Path Parameters
- `user_id` (string, required): The ID of the user
- `id` (string, required): The ID of the task to update

#### Headers
- `Authorization` (string, required): Bearer token with valid JWT

#### Request Body
```json
{
  "title": "string",
  "description": "string",
  "priority": "string",
  "tags": ["string"]
}
```

#### Response
- Status: `200`
- Body:
```json
{
  "success": true,
  "data": {
    "id": "string",
    "title": "string",
    "description": "string",
    "completed": "boolean",
    "priority": "string",
    "tags": ["string"],
    "created_at": "datetime",
    "updated_at": "datetime"
  }
}
```

#### Error Responses
- `400`: Bad Request - Invalid data provided
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User ID in token doesn't match user_id in URL
- `404`: Not Found - Task doesn't exist or doesn't belong to user

---

### DELETE /api/{user_id}/tasks/{id}
Delete a specific task for a user.

#### Path Parameters
- `user_id` (string, required): The ID of the user
- `id` (string, required): The ID of the task to delete

#### Headers
- `Authorization` (string, required): Bearer token with valid JWT

#### Response
- Status: `204` (No Content)

#### Error Responses
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User ID in token doesn't match user_id in URL
- `404`: Not Found - Task doesn't exist or doesn't belong to user

---

### PATCH /api/{user_id}/tasks/{id}/complete
Toggle the completion status of a specific task for a user.

#### Path Parameters
- `user_id` (string, required): The ID of the user
- `id` (string, required): The ID of the task to update

#### Headers
- `Authorization` (string, required): Bearer token with valid JWT

#### Request Body
```json
{
  "completed": "boolean"
}
```

#### Response
- Status: `200`
- Body:
```json
{
  "success": true,
  "data": {
    "id": "string",
    "title": "string",
    "description": "string",
    "completed": "boolean",
    "priority": "string",
    "tags": ["string"],
    "created_at": "datetime",
    "updated_at": "datetime"
  }
}
```

#### Error Responses
- `400`: Bad Request - Invalid completed value provided
- `401`: Unauthorized - Invalid or missing JWT token
- `403`: Forbidden - User ID in token doesn't match user_id in URL
- `404`: Not Found - Task doesn't exist or doesn't belong to user