# Todo Application - Authentication API Specification

## Overview
This document specifies the authentication endpoints for the Todo web application using Better Auth with JWT tokens.

## Authentication Flow
1. User logs in via Better Auth on the frontend
2. Better Auth issues JWT token
3. Frontend includes JWT in Authorization header for API requests
4. FastAPI backend verifies JWT signature using shared secret
5. User identity extracted from token
6. Request validated against user permissions
7. User-specific data returned

## JWT Configuration
- Algorithm: RS256 or HS256
- Expiration: 7 days (configurable)
- Claims: sub (user ID), email, name, iat (issued at), exp (expiration)

## Environment Variables
- `BETTER_AUTH_SECRET`: Shared secret for JWT signing/verification
- `BETTER_AUTH_URL`: Base URL for Better Auth service

## Better Auth Integration

### Frontend Configuration
- Enable JWT plugin in Better Auth client
- Configure shared secret to match backend
- Include JWT token in all API request headers

### Backend Configuration
- Verify JWT tokens using the same secret
- Extract user information from token claims
- Validate that user ID in token matches user ID in URL

## Token Validation Middleware

### FastAPI Middleware
```python
# Pseudocode for JWT validation middleware
async def jwt_validation_middleware(request, call_next):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    token = auth_header[7:]  # Remove "Bearer " prefix
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        # Add user_id to request state for use in endpoints
        request.state.user_id = user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    response = await call_next(request)
    return response
```

## Security Considerations
- All API endpoints (except auth) require valid JWT token
- User ID in token must match user ID in URL path
- Tokens expire automatically after configured time
- Stateless authentication mechanism
- No shared database session between frontend and backend