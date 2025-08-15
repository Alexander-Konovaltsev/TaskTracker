from models.database import SessionLocal
from models.project_model import Project

class ProjectController:
    @staticmethod
    def get_all_projects():
        db = SessionLocal()
        try:
            projects = db.query(Project).order_by(Project.id.asc()).all()
            return projects
        except Exception as e:
            print(f"get_all_projects error: {e}")
            return None
        finally:
            db.close()
    
    @staticmethod
    def create_project(project: Project):
        db = SessionLocal()
        try:
            db.add(project)
            db.commit()
            db.refresh(project)
            return project
        except Exception as e:
            print(f"create_project error: {e}")
            db.rollback()
            return None
        finally:
            db.close()

    @staticmethod
    def update_project(project_id: int, name: str, description: str | None):
        db = SessionLocal()
        try:
            project = db.query(Project).filter_by(id=project_id).first()

            if project:
                project.name = name
                project.description = description

                db.commit()
            return True
        except Exception as e:
            print(f"update_project error: {e}")
            db.rollback()
            return None
        finally:
            db.close()

    @staticmethod
    def get_project_id_by_name(project_name: str):
        db = SessionLocal()
        try:
            project = db.query(Project).filter_by(name=project_name).first()
            if project is None:
                return None
            return project.id
        except Exception as e:
            print(f"get_project_id_by_name error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def get_project_name_by_id(project_id: str):
        db = SessionLocal()
        try:
            project = db.query(Project).filter_by(id=project_id).first()
            if project is None:
                return None
            return project.name
        except Exception as e:
            print(f"get_project_name_by_id error: {e}")
            return None
        finally:
            db.close()