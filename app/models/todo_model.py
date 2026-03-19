from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    text = Column(String, nullable=False)
    completed = Column(Boolean, default=False)