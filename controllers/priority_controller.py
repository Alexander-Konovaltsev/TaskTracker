from models.database import SessionLocal
from models.priority_model import Priority

class PriorityController:
    @staticmethod
    def get_all_priorities():
        db = SessionLocal()
        try:
            priorities = db.query(Priority).all()
            return priorities
        except Exception as e:
            print(f"get_all_priorities error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def get_priority_id_by_name(priority_name: str):
        db = SessionLocal()
        try:
            priority = db.query(Priority).filter_by(name=priority_name).first()
            if priority is None:
                return None
            return priority.id
        except Exception as e:
            print(f"get_priority_id_by_name error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def get_priority_name_by_id(priority_id: str):
        db = SessionLocal()
        try:
            priority = db.query(Priority).filter_by(id=priority_id).first()
            if priority is None:
                return None
            return priority.name
        except Exception as e:
            print(f"get_priority_name_by_id error: {e}")
            return None
        finally:
            db.close()
