"""
Test script to verify PostgreSQL connection with the current configuration.
"""
import os
import sys
from sqlalchemy import text
from backend.core.config import settings
from backend.core.database import engine

def test_db_connection():
    print("Testing database connection...")
    print(f"Database URL: {settings.DATABASE_URL}")

    try:
        print("Attempting to connect to the database...")
        # Attempt to connect to the database
        with engine.connect() as connection:
            print("Connection established!")
            # Execute a simple query to test the connection
            result = connection.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
            print(f"✅ Query result: {result.fetchone()[0]}")

            # Check if we're using PostgreSQL
            if "postgresql" in settings.DATABASE_URL.lower():
                # Get PostgreSQL version
                pg_version = connection.execute(text("SELECT version();")).fetchone()[0]
                print(f"✅ Connected to PostgreSQL: {pg_version.split(',')[0] if ',' in pg_version else pg_version}")

                # Check if tables exist
                tables_result = connection.execute(text("""
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                """)).fetchall()
                table_names = [row[0] for row in tables_result]
                print(f"✅ Tables in database: {table_names}")

            elif "sqlite" in settings.DATABASE_URL.lower():
                print("✅ Using SQLite database")

        return True

    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_db_connection()