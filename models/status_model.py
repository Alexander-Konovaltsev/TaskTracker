from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    tasks = relationship("Task", back_populates="status")

    def __repr__(self):
        return f"<Status(id={self.id}, name='{self.name}')>"
    