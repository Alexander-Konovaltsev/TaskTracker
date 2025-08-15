from models.database import SessionLocal
from models.task_model import Task
from models.project_model import Project
from models.status_model import Status

def apply_filters(selected_project: str, selected_status: str, only_my_tasks: bool, current_user_id: int):
    db = SessionLocal()
    try:
        query = db.query(Task)

        if selected_project != "Все":
            query = query.join(Project).filter(Project.name == selected_project)

        if selected_status != "Все":
            query = query.join(Status).filter(Status.name == selected_status)

        if only_my_tasks:
            query = query.filter(
                (Task.author_id == current_user_id) |
                (Task.executor_id == current_user_id) |
                (Task.tester_id == current_user_id)
            )

        filtered_tasks = query.order_by(Task.id.asc()).all()

        return filtered_tasks   
    except Exception as e:
        print(f"apply_filters error: {e}")
        return None
    finally:
        db.close()
