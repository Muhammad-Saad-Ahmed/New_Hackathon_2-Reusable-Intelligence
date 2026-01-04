"""
FastAPI application for the Todo Application backend.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import using relative imports from the project root
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.api.v1.tasks import router as tasks_router
from backend.api.v1.auth import router as auth_router
from backend.core.config import settings
from backend.core.database import Base, engine # Import Base and engine

# Create the FastAPI app instance
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Todo Application API - Backend for the Todo Application",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(tasks_router, prefix=settings.API_V1_STR, tags=["tasks"])
app.include_router(auth_router, prefix=settings.API_V1_STR, tags=["auth"])


@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    """
    return {"message": "Todo Application API", "version": settings.APP_VERSION}


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy", "service": "Todo Application Backend"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG
    )