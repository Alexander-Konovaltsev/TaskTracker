from models.database import SessionLocal
from models.status_model import Status

class StatusController:
    @staticmethod
    def get_all_statuses():
        db = SessionLocal()
        try:
            statuses = db.query(Status).all()
            return statuses
        except Exception as e:
            print(f"get_all_statuses error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def get_status_id_by_name(status_name: str):
        db = SessionLocal()
        try:
            status = db.query(Status).filter_by(name=status_name).first()
            if status is None:
                return None
            return status.id
        except Exception as e:
            print(f"get_status_id_by_name error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def get_status_name_by_id(status_id: str):
        db = SessionLocal()
        try:
            status = db.query(Status).filter_by(id=status_id).first()
            if status is None:
                return None
            return status.name
        except Exception as e:
            print(f"get_status_name_by_id error: {e}")
            return None
        finally:
            db.close()
