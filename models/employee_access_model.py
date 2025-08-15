from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class EmployeeAccess(Base):
    __tablename__ = "employees_accesses"

    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="SET NULL"), primary_key=True, nullable=True)
    access_id = Column(Integer, ForeignKey("accesses.id", ondelete="SET NULL"), primary_key=True, nullable=True)

    def __repr__(self):
        return f"<EmployeeAccess(employee_id={self.employee_id}, access_id={self.access_id})>"
