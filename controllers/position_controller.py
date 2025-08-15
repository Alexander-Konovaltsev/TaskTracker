from models.position_model import Position
from models.database import SessionLocal

class PositionController:
    @staticmethod
    def get_position_id_by_name(position_name: str):
        db = SessionLocal()
        try:
            position = db.query(Position).filter_by(name=position_name).first()
            if position is None:
                return None
            return position.id
        except Exception as e:
            print(f"get_position_id_by_name error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def get_position_name_by_id(position_id: str):
        db = SessionLocal()
        try:
            position = db.query(Position).filter_by(id=position_id).first()
            if position is None:
                return None
            return position.name
        except Exception as e:
            print(f"get_position_name_by_id error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def get_all_position():
        db = SessionLocal()
        try:
            positions = db.query(Position).all()
            return positions
        except Exception as e:
            print(f"get_all_position error: {e}")
            return None
        finally:
            db.close()
