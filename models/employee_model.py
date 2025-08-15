from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    patronymic = Column(String(50), nullable=True)
    birth_date = Column(Date, nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password = Column(String(200), nullable=False)
    send_on_email = Column(Boolean, nullable=False, default=False)
    position_id = Column(Integer, ForeignKey("positions.id", ondelete="SET NULL"), nullable=True)

    position = relationship("Position", back_populates="employees")
    author_tasks = relationship("Task", back_populates="author", foreign_keys="[Task.author_id]")
    executor_tasks = relationship("Task", back_populates="executor", foreign_keys="[Task.executor_id]")
    tester_tasks = relationship("Task", back_populates="tester", foreign_keys="[Task.tester_id]")
    accesses = relationship("Access", secondary="employees_accesses", back_populates="employees")
    tasks = relationship("Task", secondary="employees_tasks", back_populates="employees")

    def __repr__(self):
        return f"<Employee(id={self.id}, email='{self.email}')>"
