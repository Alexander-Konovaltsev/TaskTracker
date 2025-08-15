from models.database import SessionLocal
from models.employee_access_model import EmployeeAccess

class EmployeeAccessController:
    @staticmethod
    def create_employee_accesses(employee_accesses: list[EmployeeAccess]):
        db = SessionLocal()
        try:
            db.add_all(employee_accesses)
            db.commit()
            for employee_access in employee_accesses:
                db.refresh(employee_access)
            return employee_accesses
        except Exception as e:
            print(f"create_employee_accesses error: {e}")
            db.rollback()
            return None
        finally:
            db.close()

    @staticmethod
    def delete_employee_accesses(accesses_id_to_delete: list[int], employee_id: int):
        db = SessionLocal()
        try:
            accesses_to_delete = []

            for id in accesses_id_to_delete:
                accesses_to_delete.append(db.query(EmployeeAccess).filter_by(employee_id=employee_id, access_id=id).first())

            for access in accesses_to_delete:
                db.delete(access)

            db.commit()
            return True
        except Exception as e:
            print(f"delete_employee_accesses error: {e}")
            db.rollback()
            return False
        finally:
            db.close()

    @staticmethod
    def get_employee_accesses_by_id(employee_id: int):
        db = SessionLocal()
        try:
            employee_accesses = db.query(EmployeeAccess).filter_by(employee_id=employee_id).all()
            return employee_accesses
        except Exception as e:
            print(f"get_employee_accesses_by_id error: {e}")
            return None
        finally:
            db.close()
