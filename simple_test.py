"""
Test script to verify PostgreSQL connection with the current configuration.
"""
import os
import sys
sys.stdout.flush()
print("Testing database connection...")
sys.stdout.flush()

from sqlalchemy import text
from backend.core.config import settings
from backend.core.database import engine

print(f"Database URL: {settings.DATABASE_URL}")
sys.stdout.flush()

try:
    print("Attempting to connect to the database...")
    sys.stdout.flush()
    # Attempt to connect to the database
    with engine.connect() as connection:
        print("Connection established!")
        sys.stdout.flush()
        # Execute a simple query to test the connection
        result = connection.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
        sys.stdout.flush()
        print(f"✅ Query result: {result.fetchone()[0]}")
        sys.stdout.flush()
        
        # Check if we're using PostgreSQL
        if "postgresql" in settings.DATABASE_URL.lower():
            # Get PostgreSQL version
            pg_version = connection.execute(text("SELECT version();")).fetchone()[0]
            print(f"✅ Connected to PostgreSQL: {pg_version.split(',')[0] if ',' in pg_version else pg_version}")
            sys.stdout.flush()
            
            # Check if tables exist
            tables_result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)).fetchall()
            table_names = [row[0] for row in tables_result]
            print(f"✅ Tables in database: {table_names}")
            sys.stdout.flush()
            
        elif "sqlite" in settings.DATABASE_URL.lower():
            print("✅ Using SQLite database")
            sys.stdout.flush()
            
    print("Test completed successfully!")
    sys.stdout.flush()
    
except Exception as e:
    print(f"❌ Database connection failed: {str(e)}")
    sys.stdout.flush()
    import traceback
    traceback.print_exc()