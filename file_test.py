"""
Test script to verify PostgreSQL connection with the current configuration.
"""
import os
import sys
from sqlalchemy import text

# Add the project root and backend directory to the path
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./backend'))

from core.config import settings
from core.database import engine

# Write results to a file
with open("db_test_results.txt", "w", encoding="utf-8") as f:
    f.write("Testing database connection...\n")
    f.write(f"Database URL: {settings.DATABASE_URL}\n")

    try:
        f.write("Attempting to connect to the database...\n")
        # Attempt to connect to the database
        with engine.connect() as connection:
            f.write("Connection established!\n")
            # Execute a simple query to test the connection
            result = connection.execute(text("SELECT 1"))
            f.write("✅ Database connection successful!\n")
            f.write(f"✅ Query result: {result.fetchone()[0]}\n")

            # Check if we're using PostgreSQL
            if "postgresql" in settings.DATABASE_URL.lower():
                f.write("Detected PostgreSQL database\n")
                # Get PostgreSQL version
                try:
                    pg_version = connection.execute(text("SELECT version();")).fetchone()[0]
                    f.write(f"✅ Connected to PostgreSQL: {pg_version.split(',')[0] if ',' in pg_version else pg_version}\n")

                    # Check if tables exist
                    tables_result = connection.execute(text("""
                        SELECT table_name
                        FROM information_schema.tables
                        WHERE table_schema = 'public'
                    """)).fetchall()
                    table_names = [row[0] for row in tables_result]
                    f.write(f"✅ Tables in database: {table_names}\n")
                except Exception as pg_error:
                    f.write(f"⚠️ Could not get PostgreSQL version or tables: {str(pg_error)}\n")

            elif "sqlite" in settings.DATABASE_URL.lower():
                f.write("✅ Using SQLite database\n")

        f.write("Test completed successfully!\n")

    except Exception as e:
        f.write(f"❌ Database connection failed: {str(e)}\n")
        import traceback
        import io
        tb = io.StringIO()
        traceback.print_exc(file=tb)
        f.write(tb.getvalue())