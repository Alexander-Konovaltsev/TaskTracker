from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    employees = relationship("Employee", back_populates="position")

    def __repr__(self):
        return f"<Position(id={self.id}, name='{self.name}')>"
    