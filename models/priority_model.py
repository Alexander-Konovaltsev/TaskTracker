from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Priority(Base):
    __tablename__ = "priorities"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    tasks = relationship("Task", back_populates="priority")

    def __repr__(self):
        return f"<Priority(id={self.id}, name='{self.name}')>"
    