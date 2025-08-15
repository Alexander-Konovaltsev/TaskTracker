from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class EmployeeTask(Base):
    __tablename__ = "employees_tasks"

    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="SET NULL"), primary_key=True, nullable=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="SET NULL"), primary_key=True, nullable=True)

    def __repr__(self):
        return f"<EmployeeTask(employee_id={self.employee_id}, access_id={self.task_id})>"
