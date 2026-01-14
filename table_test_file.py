"""
Test script to check if tables are created in the database.
"""
import sys
import os

# Write results to a file
with open("table_test_results.txt", "w") as f:
    f.write("Testing table creation...\n")
    
    # Add the project root to the Python path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from backend.core.config import settings
    from backend.core.database import engine, Base
    from backend.models.database import User, Task

    f.write(f"Database URL: {settings.DATABASE_URL}\n")
    
    try:
        f.write("Creating tables...\n")
        
        # Create all tables
        Base.metadata.create_all(bind=engine)
        f.write("Tables created successfully!\n")
        
        # Verify tables exist by reflecting them
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        f.write(f"Tables in database: {tables}\n")
        
        # Check specifically for our tables
        if 'users' in tables:
            f.write("✅ Users table exists\n")
        else:
            f.write("❌ Users table does not exist\n")
            
        if 'tasks' in tables:
            f.write("✅ Tasks table exists\n")
        else:
            f.write("❌ Tasks table does not exist\n")
        
        f.write("Table creation test completed successfully!\n")
        
    except Exception as e:
        f.write(f"❌ Table creation failed: {str(e)}\n")
        import traceback
        import io
        tb = io.StringIO()
        traceback.print_exc(file=tb)
        f.write(tb.getvalue())