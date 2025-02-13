from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from pydantic import BaseModel

app = FastAPI()

# Create tables on startup
Base.metadata.create_all(bind=engine)

# Function to create a default user

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Supabase!"}
