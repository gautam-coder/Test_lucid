from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()