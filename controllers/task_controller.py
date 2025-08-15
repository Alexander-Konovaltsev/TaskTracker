from models.database import SessionLocal
from models.task_model import Task
from datetime import date

class TaskController:
    @staticmethod
    def create_task(task: Task):
        db = SessionLocal()
        try:
            db.add(task)
            db.commit()
            db.refresh(task)
            return task
        except Exception as e:
            print(f"create_task error: {e}")
            db.rollback()
            return None
        finally:
            db.close()

    @staticmethod
    def update_task(task_id: int, name: str, description: str, deadline_date: date, status_id: int, priority_id: int, project_id: int, executor_id: int, tester_id: int, end_date: date=None):
        db = SessionLocal()
        try:
            task = db.query(Task).filter_by(id=task_id).first()

            if task:
                task.name = name
                task.description = description
                task.deadline_date = deadline_date
                task.status_id = status_id
                task.priority_id = priority_id
                task.project_id = project_id
                task.executor_id = executor_id
                task.tester_id = tester_id
                if end_date:
                    task.end_date = end_date

                db.commit()
            return True
        except Exception as e:
            print(f"update_task error: {e}")
            db.rollback()
            return None
        finally:
            db.close()

    @staticmethod
    def get_all_tasks():
        db = SessionLocal()
        try:
            tasks = db.query(Task).order_by(Task.id.asc()).all()
            return tasks
        except Exception as e:
            print(f"get_all_tasks error: {e}")
            return None
        finally:
            db.close()
