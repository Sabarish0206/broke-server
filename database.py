from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use the Supabase connection pooler link
DATABASE_URL = "postgresql://postgres.votdiebhkolbdayyprfd:Broke%40123@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()