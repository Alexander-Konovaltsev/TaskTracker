from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame
from resources.colors import Color
from PyQt6.QtGui import QFont
from models.employee_model import Employee
from controllers.position_controller import PositionController
from controllers.employee_controller import EmployeeController
from widgets.icon_btn import IconBtn
from PyQt6.QtCore import pyqtSignal

class EmployeeCardWidget(QFrame):
    success_delete = pyqtSignal()
    employee_update = pyqtSignal(Employee)
    def __init__(self, employee: Employee):
        super().__init__()

        self.setMinimumWidth(480)
        self.employee = employee
        self.setStyleSheet(f"""
        QFrame{{
            color: {Color.DARK_BROWN.value};
            padding: 15px;
            border: 1px solid {Color.DARK_BROWN.value};
            border-radius: 15px;
            background: {Color.GRAY.value};
            max-width: 500px;
        }}
        QLabel{{
            border: none;
            padding-bottom: 3px;
            padding-top: 0px;
        }}
        """)

        title_text_font = QFont("Verdana", 16, QFont.Weight.Bold)
        main_text_font = QFont("Verdana", 14, QFont.Weight.Bold)

        main_card_layout = QVBoxLayout(self)
        main_card_layout.setContentsMargins(0, 0, 0, 0)

        fio_layout = QHBoxLayout()
        fio_layout.setContentsMargins(0, 0, 0, 20)
        fio_label = QLabel(f"{employee.last_name} {employee.first_name} {employee.patronymic if employee.patronymic is not None else ''}")
        fio_label.setFont(title_text_font)

        birth_date_label = QLabel(f"""<span style="font-weight: normal;">Дата рождения:</span> {employee.birth_date.strftime("%d.%m.%Y")}""")
        birth_date_label.setFont(main_text_font)

        email_label = QLabel(f"""<span style="font-weight: normal;">Email:</span> {employee.email}""")
        email_label.setFont(main_text_font)

        position_label = QLabel(f"""<span style="font-weight: normal;">Должность:</span> {PositionController.get_position_name_by_id(employee.position_id)}""")
        position_label.setFont(main_text_font)

        icons_btn = QHBoxLayout()

        self.update_btn = IconBtn("update_icon_brown.png", Color.LIGHT_GRAY.value, Color.LIGHT_GRAY_DARKER.value)
        self.update_btn.clicked.connect(self.update_btn_clicked)
        self.update_btn.setVisible(False)

        self.delete_btn = IconBtn("delete_icon.png", Color.LIGHT_GRAY.value, Color.LIGHT_GRAY_DARKER.value)
        self.delete_btn.clicked.connect(self.delete_btn_clicked)
        self.delete_btn.setVisible(False)

        fio_layout.addStretch()
        fio_layout.addWidget(fio_label)
        fio_layout.addStretch()

        icons_btn.addStretch()
        icons_btn.addWidget(self.update_btn)
        icons_btn.addWidget(self.delete_btn)
        icons_btn.addStretch()

        main_card_layout.addLayout(fio_layout)
        main_card_layout.addWidget(birth_date_label)
        main_card_layout.addWidget(email_label)
        main_card_layout.addWidget(position_label)
        main_card_layout.addLayout(icons_btn)

    def update_btn_clicked(self):
        self.employee_update.emit(self.employee)
    
    def delete_btn_clicked(self):
        if EmployeeController.delete_employee(self.employee):
            self.success_delete.emit()