from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from widgets.navigation_panel_widget import NavigationPanel
from .authorization_widget import AuthorizationWidget
from .tasks_widget import TasksWidget
from .projects_widget import ProjectsWidget
from .employees_widget import EmployeesWidget
from .create_update_project_widget import CreateUpdateProjectWidget
from .create_update_show_task_widget import CreateUpdateShowTaskWidget
from .create_update_show_employee_widget import CreateUpdateShowEmployeeWidget
from resources.colors import Color
from resources.accesses import AccessName
from models.employee_model import Employee
from models.project_model import Project
from models.task_model import Task
from controllers.employee_controller import EmployeeController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Таск-трекер")
        self.showMaximized()
        self.setStyleSheet(f"QWidget{{background: {Color.DARK_BROWN.value}}}")

        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(main_widget)

        self.current_user_email = None

        self.navigation_panel_widget = NavigationPanel()
        self.navigation_panel_widget.exit_from_account.connect(self.handle_exit_from_account)
        self.navigation_panel_widget.show_user_info.connect(self.handle_show_user_info)
        self.navigation_panel_widget.make_invisible_all_layouts()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet(f"background: {Color.WHITE.value};")

        self.authorization_widget = AuthorizationWidget()
        self.authorization_widget.authorization_successful.connect(self.handle_authorization_successful)

        self.projects_widget = ProjectsWidget()
        self.projects_widget.project_card_update.connect(self.handle_update_project)

        self.tasks_widget = TasksWidget()
        self.tasks_widget.task_card_show.connect(self.handle_show_task)
        self.tasks_widget.task_card_update.connect(self.handle_update_task)

        self.employees_widget = EmployeesWidget()
        self.employees_widget.delete_card_success.connect(self.clicked_employees_btn)
        self.employees_widget.employee_card_update.connect(self.handle_update_user)

        self.create_project_widget = CreateUpdateProjectWidget()
        self.create_project_widget.create_update_project_success.connect(self.clicked_projects_btn)

        self.create_task_widget = CreateUpdateShowTaskWidget()
        self.create_task_widget.create_update_task_succees.connect(self.clicked_tasks_btn)

        self.create_employee_widget = CreateUpdateShowEmployeeWidget()
        self.create_employee_widget.create_employee_success.connect(self.clicked_employees_btn)

        self.stacked_widget.addWidget(self.authorization_widget)
        self.stacked_widget.addWidget(self.projects_widget)
        self.stacked_widget.addWidget(self.tasks_widget)
        self.stacked_widget.addWidget(self.employees_widget)
        self.stacked_widget.addWidget(self.create_project_widget)
        self.stacked_widget.addWidget(self.create_task_widget)
        self.stacked_widget.addWidget(self.create_employee_widget)

        self.navigation_panel_widget.projects_btn.clicked.connect(self.clicked_projects_btn)
        self.navigation_panel_widget.tasks_btn.clicked.connect(self.clicked_tasks_btn)
        self.navigation_panel_widget.employees_btn.clicked.connect(self.clicked_employees_btn)
        self.navigation_panel_widget.create_project_btn.clicked.connect(self.clicked_create_project_btn)
        self.navigation_panel_widget.create_task_btn.clicked.connect(self.clicked_create_task_btn)
        self.navigation_panel_widget.create_employee_btn.clicked.connect(self.clicked_create_employee_btn)

        main_layout.addWidget(self.navigation_panel_widget)
        main_layout.addWidget(self.stacked_widget)
    
    def clicked_projects_btn(self):
        current_employee = EmployeeController.get_employee_by_email(self.current_user_email)

        self.stacked_widget.removeWidget(self.projects_widget)
        self.projects_widget.deleteLater()
        self.projects_widget = ProjectsWidget(current_employee)
        self.projects_widget.project_card_update.connect(self.handle_update_project)
        self.stacked_widget.insertWidget(1, self.projects_widget)

        self.stacked_widget.setCurrentIndex(1)

    def clicked_tasks_btn(self):
        current_employee = EmployeeController.get_employee_by_email(self.current_user_email)

        self.stacked_widget.removeWidget(self.tasks_widget)
        self.tasks_widget.deleteLater()

        self.tasks_widget = TasksWidget(current_employee)
        self.tasks_widget.task_card_show.connect(self.handle_show_task)
        self.tasks_widget.task_card_update.connect(self.handle_update_task)
        self.stacked_widget.insertWidget(2, self.tasks_widget)

        self.stacked_widget.setCurrentIndex(2)

    def clicked_employees_btn(self):
        current_employee = EmployeeController.get_employee_by_email(self.current_user_email)

        self.stacked_widget.removeWidget(self.employees_widget)
        self.employees_widget.deleteLater()

        self.employees_widget = EmployeesWidget(current_employee)
        self.employees_widget.delete_card_success.connect(self.clicked_employees_btn)
        self.employees_widget.employee_card_update.connect(self.handle_update_user)

        self.stacked_widget.insertWidget(3, self.employees_widget)

        self.stacked_widget.setCurrentIndex(3)

    def clicked_create_project_btn(self):
        self.stacked_widget.removeWidget(self.create_project_widget)
        self.create_project_widget.deleteLater()

        self.create_project_widget = CreateUpdateProjectWidget()
        self.create_project_widget.create_update_project_success.connect(self.clicked_projects_btn)
        self.stacked_widget.insertWidget(4, self.create_project_widget)

        self.stacked_widget.setCurrentIndex(4)

    def clicked_create_task_btn(self, task: Task = None, show_flag = None):
        current_employee = EmployeeController.get_employee_by_email(self.current_user_email)

        self.stacked_widget.removeWidget(self.create_task_widget)
        self.create_task_widget.deleteLater()

        self.create_task_widget = CreateUpdateShowTaskWidget(task=task, show_flag=show_flag, current_employee=current_employee)
        self.create_task_widget.create_update_task_succees.connect(self.clicked_tasks_btn)
        self.stacked_widget.insertWidget(5, self.create_task_widget)

        self.stacked_widget.setCurrentIndex(5)

    def clicked_create_employee_btn(self):
        self.stacked_widget.removeWidget(self.create_employee_widget)
        self.create_employee_widget.deleteLater()

        self.create_employee_widget = CreateUpdateShowEmployeeWidget()
        self.create_employee_widget.create_employee_success.connect(self.clicked_employees_btn)
        self.stacked_widget.insertWidget(6, self.create_employee_widget)

        self.stacked_widget.setCurrentIndex(6)
    
    def handle_authorization_successful(self, employee: Employee):
        self.navigation_panel_widget.user_fio_label.setText(f"{employee.last_name} {employee.first_name} {employee.patronymic if employee.patronymic is not None else ''}")
        self.current_user_email = employee.email

        for accees in employee.accesses:
            match accees.name:
                case AccessName.CREATING_PROJECTS.value:
                    self.navigation_panel_widget.create_project_btn.setVisible(True)
                case AccessName.SETTING_TASKS.value:
                    self.navigation_panel_widget.create_task_btn.setVisible(True)
                case AccessName.ADDING_EMPLOYEES.value:
                    self.navigation_panel_widget.create_employee_btn.setVisible(True)

        self.navigation_panel_widget.make_visible_layout(self.navigation_panel_widget.buttons_layout)
        self.navigation_panel_widget.make_visible_layout(self.navigation_panel_widget.user_info_layout)
        self.navigation_panel_widget.make_visible_layout(self.navigation_panel_widget.icon_btn_layout)

        self.clicked_tasks_btn()

    def handle_exit_from_account(self):
        self.authorization_widget.email_input.clear()
        self.authorization_widget.password_input.clear()
        self.authorization_widget.email_input.setFocus()
        self.stacked_widget.setCurrentIndex(0)

    def handle_show_user_info(self):
        current_employee = EmployeeController.get_employee_by_email(self.current_user_email)

        self.stacked_widget.removeWidget(self.create_employee_widget)
        self.create_employee_widget.deleteLater()

        self.create_employee_widget = CreateUpdateShowEmployeeWidget(current_employee, True)
        self.stacked_widget.insertWidget(6, self.create_employee_widget)

        self.stacked_widget.setCurrentIndex(6)

    def handle_update_user(self, employee: Employee):
        self.stacked_widget.removeWidget(self.create_employee_widget)
        self.create_employee_widget.deleteLater()
        self.create_employee_widget = CreateUpdateShowEmployeeWidget(employee, False)
        self.create_employee_widget.create_employee_success.connect(self.clicked_employees_btn)
        self.stacked_widget.insertWidget(6, self.create_employee_widget)

        self.stacked_widget.setCurrentIndex(6)

    def handle_update_project(self, project: Project):
        self.stacked_widget.removeWidget(self.create_project_widget)
        self.create_project_widget.deleteLater()
        self.create_project_widget = CreateUpdateProjectWidget(project)
        self.create_project_widget.create_update_project_success.connect(self.clicked_projects_btn)
        self.stacked_widget.insertWidget(4, self.create_project_widget)

        self.stacked_widget.setCurrentIndex(4)

    def handle_show_task(self, task: Task):
        self.clicked_create_task_btn(task=task, show_flag=True)

    def handle_update_task(self, task: Task):
        self.clicked_create_task_btn(task=task, show_flag=False)
