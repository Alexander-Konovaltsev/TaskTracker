from models.database import create_tables, delete_tables, SessionLocal
from datetime import date
from .password_protect import hash_password
from models.employee_model import Employee
from models.position_model import Position
from models.priority_model import Priority
from models.project_model import Project
from models.status_model import Status
from models.task_model import Task
from models.access_model import Access
from models.employee_access_model import EmployeeAccess
from models.employee_task_model import EmployeeTask
from controllers.access_controller import AccessController
from controllers.position_controller import PositionController
from resources.accesses import AccessName
from resources.positions import PositionName
from resources.priorities import PriorityName
from resources.statuses import StatusName

def table_init(new_records: list):
    db = SessionLocal()
    try:
        db.add_all(new_records)
        db.commit()
        for new_record in new_records:
            db.refresh(new_record)
        return new_records
    except Exception as e:
        print(f"table_init error: {e}")
        db.rollback()
        return None
    finally:
        db.close()

def create_owner():
    db = SessionLocal()
    try:
        owner = Employee(
            last_name="Овнеров",
            first_name="Овнер",
            patronymic="Овнерович",
            birth_date=date(2000, 10, 20),
            email="owner@mail.ru",
            password=hash_password("1234"),
            position_id=PositionController.get_position_id_by_name(PositionName.HEAD.value)
        )

        owner_accesses = [EmployeeAccess(employee_id=1, access_id=AccessController.get_access_id_by_name(AccessName.ADDING_EMPLOYEES.value)),
                          EmployeeAccess(employee_id=1, access_id=AccessController.get_access_id_by_name(AccessName.UPDATING_EMPLOYEES.value)),
                          EmployeeAccess(employee_id=1, access_id=AccessController.get_access_id_by_name(AccessName.DELETING_EMPLOYEES.value)),
                          EmployeeAccess(employee_id=1, access_id=AccessController.get_access_id_by_name(AccessName.SETTING_TASKS.value)),
                          EmployeeAccess(employee_id=1, access_id=AccessController.get_access_id_by_name(AccessName.UPDATING_TASKS.value)),
                          EmployeeAccess(employee_id=1, access_id=AccessController.get_access_id_by_name(AccessName.CREATING_PROJECTS.value)),
                          EmployeeAccess(employee_id=1, access_id=AccessController.get_access_id_by_name(AccessName.UPDATING_PROJECTS.value))]

        db.add(owner)
        db.commit()
        db.add_all(owner_accesses)
        db.commit()

        db.refresh(owner)
        return owner
    except Exception as e:
        print(f"create_owner error: {e}")
        db.rollback()
        return None
    finally:
        db.close
    

priorities = [Priority(name=PriorityName.LOW.value),
              Priority(name=PriorityName.MIDDLE.value),
              Priority(name=PriorityName.HIGH.value),
              Priority(name=PriorityName.CRITICAL.value),
              Priority(name=PriorityName.BLOCKER.value)]

statuses = [Status(name=StatusName.OPEN.value),
            Status(name=StatusName.IN_WORK.value),
            Status(name=StatusName.MAY_TEST.value),
            Status(name=StatusName.IN_TEST.value),
            Status(name=StatusName.ON_REVIEW.value),
            Status(name=StatusName.CLOSE.value)]

positions = [Position(name=PositionName.HEAD.value),
             Position(name=PositionName.TEAM_LEADER.value),
             Position(name=PositionName.PROGRAMMER.value),
             Position(name=PositionName.TESTER.value),
             Position(name=PositionName.TECHNICAL_SUPPORT_SPECIALIST.value),
             Position(name=PositionName.ACCOUNTANT.value),
             Position(name=PositionName.JURIST.value),
             Position(name=PositionName.PROJECT_MANAGER.value),
             Position(name=PositionName.HR_MANAGER.value)]

accesses = [Access(name=AccessName.ADDING_EMPLOYEES.value),
            Access(name=AccessName.UPDATING_EMPLOYEES.value),
            Access(name=AccessName.DELETING_EMPLOYEES.value),
            Access(name=AccessName.SETTING_TASKS.value),
            Access(name=AccessName.UPDATING_TASKS.value),
            Access(name=AccessName.CREATING_PROJECTS.value),
            Access(name=AccessName.UPDATING_PROJECTS.value)]

delete_tables()
create_tables()
table_init(priorities)
table_init(statuses)
table_init(positions)
table_init(accesses)
create_owner()
