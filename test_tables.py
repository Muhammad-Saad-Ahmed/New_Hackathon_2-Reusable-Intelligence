"""
Test script to check if tables are created in the database.
"""
import sys
import os
sys.stdout.flush()
print("Testing table creation...")
sys.stdout.flush()

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.core.config import settings
from backend.core.database import engine, Base
from backend.models.database import User, Task

print(f"Database URL: {settings.DATABASE_URL}")
sys.stdout.flush()

try:
    print("Creating tables...")
    sys.stdout.flush()
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
    sys.stdout.flush()
    
    # Verify tables exist by reflecting them
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    print(f"Tables in database: {tables}")
    sys.stdout.flush()
    
    # Check specifically for our tables
    if 'users' in tables:
        print("✅ Users table exists")
    else:
        print("❌ Users table does not exist")
        
    if 'tasks' in tables:
        print("✅ Tasks table exists")
    else:
        print("❌ Tasks table does not exist")
    
    print("Table creation test completed successfully!")
    sys.stdout.flush()
    
except Exception as e:
    print(f"❌ Table creation failed: {str(e)}")
    sys.stdout.flush()
    import traceback
    traceback.print_exc()