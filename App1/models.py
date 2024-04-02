
from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP
from sqlalchemy.sql.expression import null
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from database import engine


Base = declarative_base()
Base.metadata.create_all(bind=engine)
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    cost = Column(Integer, nullable=False)
    manufacture = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    brand = Column(Boolean, default=False)
