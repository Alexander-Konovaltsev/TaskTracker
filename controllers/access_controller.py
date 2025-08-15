from models.access_model import Access
from models.database import SessionLocal

class AccessController:
    @staticmethod
    def get_access_id_by_name(access_name: str):
        db = SessionLocal()
        try:
            access = db.query(Access).filter_by(name=access_name).first()
            if access is None:
                return None
            return access.id
        except Exception as e:
            print(f"get_access_id_by_name error: {e}")
            return None
        finally:
            db.close()
    
    @staticmethod
    def get_access_name_by_id(access_id: str):
        db = SessionLocal()
        try:
            access = db.query(Access).filter_by(id=access_id).first()
            if access is None:
                return None
            return access.name
        except Exception as e:
            print(f"get_access_name_by_id error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def get_all_access():
        db = SessionLocal()
        try:
            accesses = db.query(Access).all()
            return accesses
        except Exception as e:
            print(f"get_all_access error: {e}")
            return None
        finally:
            db.close()
            
