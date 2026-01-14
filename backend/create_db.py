"""
Script to create database tables defined in the SQLAlchemy models.
"""
from core.database import Base, engine
from models.database import User, Task # Import models to ensure they are registered with Base

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully.")
