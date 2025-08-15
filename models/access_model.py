from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Access(Base):
    __tablename__ = "accesses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    employees = relationship("Employee", secondary="employees_accesses", back_populates="accesses")

    def __repr__(self):
        return f"<Access(id={self.id}, name='{self.name}')>"
    