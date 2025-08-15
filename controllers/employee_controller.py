from models.employee_model import Employee
from models.database import SessionLocal
from sqlalchemy.orm import joinedload
from sqlalchemy import asc
from datetime import date
from models.position_model import Position

class EmployeeController:
    @staticmethod
    def get_employee_by_email(employee_email: str):
        db = SessionLocal()
        try:
            employee = db.query(Employee).options(joinedload(Employee.accesses)).filter_by(email=employee_email).first()
            return employee
        except Exception as e:
            print(f"get_employee_by_email error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def get_employee_by_id(employee_id: str):
        db = SessionLocal()
        try:
            employee = db.query(Employee).filter_by(id=employee_id).first()
            return employee
        except Exception as e:
            print(f"get_employee_by_id error: {e}")
            return None
        finally:
            db.close()
        
    @staticmethod
    def create_employee(employee: Employee):
        db = SessionLocal()
        try:
            db.add(employee)
            db.commit()
            db.refresh(employee)
            return employee
        except Exception as e:
            print(f"create_employee error: {e}")
            db.rollback()
            return None
        finally:
            db.close()

    @staticmethod
    def get_all_employess():
        db = SessionLocal()
        try:
            employess = db.query(Employee).order_by(Employee.id.asc()).all()
            return employess
        except Exception as e:
            print(f"get_all_employess error: {e}")
            return None
        finally:
            db.close()

    @staticmethod
    def delete_employee(employee: Employee):
        db = SessionLocal()
        try:
            if employee:
                db.delete(employee)
                db.commit()
            return True
        except Exception as e:
            print(f"delete_employee error: {e}")
            db.rollback()
            return None
        finally:
            db.close()

    @staticmethod
    def update_employee(employee_id: int, last_name: str, first_name: str, patronymic: str, birth_date: date, email: str, position_id: int, password: str = None):
        db = SessionLocal()
        try:
            employee = db.query(Employee).filter_by(id=employee_id).first()

            if employee:
                employee.last_name = last_name
                employee.first_name = first_name
                employee.patronymic = patronymic
                employee.birth_date = birth_date
                employee.email = email
                employee.position_id = position_id
                if password:
                    employee.password = password

                db.commit()
            return True
        except Exception as e:
            print(f"update_employee error: {e}")
            db.rollback()
            return None
        finally:
            db.close()

    @staticmethod
    def get_employees_by_position_name(position_name: str):
        db = SessionLocal()
        try:
            employees = db.query(Employee).join(Position).filter(Position.name == position_name).all()
            return employees
        except Exception as e:
            print(f"get_employees_by_position_name error: {e}")
            return None
        finally:
            db.close()