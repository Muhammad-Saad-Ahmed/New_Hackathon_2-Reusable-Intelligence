"""
Script to create a test user in the database.
"""
from sqlalchemy.orm import Session
from core.database import SessionLocal
from models.database import User
from core.security import get_password_hash
import uuid

def create_test_user():
    db: Session = SessionLocal()
    try:
        email = "test@example.com"
        password = "password"
        
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            print(f"User with email {email} already exists.")
            return

        hashed_password = get_password_hash(password)
        db_user = User(
            id=uuid.uuid4(),
            email=email,
            name="Test User",
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        print(f"Test user '{email}' created successfully.")
    except Exception as e:
        print(f"Error creating test user: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_test_user()
