from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base 
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, index=True)


