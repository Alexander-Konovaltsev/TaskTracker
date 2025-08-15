from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout
from PyQt6.QtGui import QFont
from widgets.breadcrumbs_widget import Breadcrumbs
from resources.colors import Color
from controllers.employee_controller import EmployeeController
from controllers.employee_access_controller import EmployeeAccessController
from controllers.access_controller import AccessController
from widgets.employee_card_widget import EmployeeCardWidget
from models.employee_model import Employee
from resources.accesses import AccessName
from PyQt6.QtCore import pyqtSignal

class EmployeesWidget(QWidget):
    delete_card_success = pyqtSignal()
    employee_card_update = pyqtSignal(Employee)
    def __init__(self, current_employee: Employee = None):
        super().__init__()

        self.setStyleSheet(f"""
        QLabel{{
            color: {Color.DARK_BROWN.value};
        }}
        """)
        main_text_font = QFont("Verdana", 16, QFont.Weight.Normal)

        main_employees_layout = QVBoxLayout(self)
        main_employees_layout.setContentsMargins(20, 20, 20, 20)

        employees_title_label = QLabel("Сотрудники")
        employees_title_label.setFont(QFont("Verdana", 28, QFont.Weight.Normal))

        main_employees_layout.addWidget(employees_title_label)
        main_employees_layout.addWidget(Breadcrumbs(f"""Главная <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ Сотрудники</span>"""))

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        scroll_widget = QWidget()

        main_cards_layout = QVBoxLayout(scroll_widget)

        employees = EmployeeController.get_all_employess()


        if current_employee:
            current_employee_accesses = [AccessController.get_access_name_by_id(emp_acc.access_id) for emp_acc in EmployeeAccessController.get_employee_accesses_by_id(current_employee.id)]
            for employee in employees:
                if employee.id != current_employee.id and employee.email != "owner@mail.ru":
                    card_layout = QHBoxLayout()
                    card = EmployeeCardWidget(employee)

                    card.success_delete.connect(lambda: self.delete_card_success.emit())
                    card.employee_update.connect(self.handle_employee_card_update)

                    if AccessName.UPDATING_EMPLOYEES.value in current_employee_accesses:
                        card.update_btn.setVisible(True)

                    if AccessName.DELETING_EMPLOYEES.value in current_employee_accesses:
                        card.delete_btn.setVisible(True)

                    card_layout.addStretch()
                    card_layout.addWidget(card)
                    card_layout.addStretch()

                    main_cards_layout.addLayout(card_layout)
        
        main_cards_layout.addStretch()

        scroll_area.setWidget(scroll_widget)
        main_employees_layout.addWidget(scroll_area)

    def handle_employee_card_update(self, employee: Employee):
        self.employee_card_update.emit(employee)
