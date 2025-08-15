from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    deadline_date = Column(Date, nullable=True)
    status_id = Column(Integer, ForeignKey("statuses.id", ondelete="SET NULL"), nullable=True)
    priority_id = Column(Integer, ForeignKey("priorities.id", ondelete="SET NULL"), nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="SET NULL"), nullable=True)
    author_id = Column(Integer, ForeignKey("employees.id", ondelete="SET NULL"), nullable=True)
    executor_id = Column(Integer, ForeignKey("employees.id", ondelete="SET NULL"), nullable=True)
    tester_id = Column(Integer, ForeignKey("employees.id", ondelete="SET NULL"), nullable=True)

    status = relationship("Status", back_populates="tasks")
    priority = relationship("Priority", back_populates="tasks")
    project = relationship("Project", back_populates="tasks")
    author = relationship("Employee", foreign_keys=[author_id], back_populates="author_tasks")
    executor = relationship("Employee", foreign_keys=[executor_id], back_populates="executor_tasks")
    tester = relationship("Employee", foreign_keys=[tester_id], back_populates="tester_tasks")
    employees = relationship("Employee", secondary="employees_tasks", back_populates="tasks")


    def __repr__(self):
        return f"<Task(id={self.id}, name='{self.name}', start_date='{self.start_date}', deadline_date='{self.deadline_date}')>"
