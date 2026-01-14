"""
Authentication middleware for FastAPI.
"""
from fastapi import HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.security import decode_access_token
from typing import Optional

class JWTBearer(HTTPBearer):
    """
    A FastAPI dependency that handles JWT token authentication.
    """
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[dict]:
        credentials: Optional[HTTPAuthorizationCredentials] = await super().__call__(request)
        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication scheme.",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            token_data = decode_access_token(credentials.credentials)
            if not token_data:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired token.",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return token_data
        else:
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not authenticated.",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return None
