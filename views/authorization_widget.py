from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSignal
from widgets.breadcrumbs_widget import Breadcrumbs
from widgets.input_line_text import InputLineText
from widgets.validation_text import ValidationText
from widgets.main_btn import MainBtn
from resources.colors import Color
from controllers.employee_controller import EmployeeController
import utils.validation as validation
from utils.password_protect import check_password
from models.employee_model import Employee

class AuthorizationWidget(QWidget):
    authorization_successful = pyqtSignal(Employee)
    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"""
        QLabel{{
            color: {Color.DARK_BROWN.value};
        }}
        """)
        main_text_font = QFont("Verdana", 16, QFont.Weight.Normal)

        main_autorization_layout = QVBoxLayout(self)
        main_autorization_layout.setContentsMargins(20, 20, 20, 20)

        authorization_title_label = QLabel("Вход")
        authorization_title_label.setFont(QFont("Verdana", 28, QFont.Weight.Normal))

        self.email_label = QLabel("Email")
        self.email_label.setFont(main_text_font)

        self.email_input = InputLineText(False)
        self.email_input.setFont(main_text_font)
        self.email_input.setText("owner@mail.ru")

        self.email_validation_text = ValidationText()

        self.password_label = QLabel("Пароль")
        self.password_label.setFont(main_text_font)

        self.password_input = InputLineText(True)
        self.password_input.setFont(main_text_font)
        self.password_input.setText("1234")

        self.password_validation_text = ValidationText()

        login_btn = MainBtn("Войти", 5, 35)
        login_btn.setFont(main_text_font)
        login_btn.setMaximumWidth(90)
        login_btn.clicked.connect(self.user_login)

        main_autorization_layout.addWidget(authorization_title_label)
        main_autorization_layout.addWidget(Breadcrumbs(f"""Главная <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ Вход</span>"""))
        main_autorization_layout.addWidget(self.email_label)
        main_autorization_layout.addWidget(self.email_input)
        main_autorization_layout.addWidget(self.email_validation_text)
        main_autorization_layout.addWidget(self.password_label)
        main_autorization_layout.addWidget(self.password_input)
        main_autorization_layout.addWidget(self.password_validation_text)
        main_autorization_layout.addWidget(login_btn)
        main_autorization_layout.addStretch()

    def user_login(self):
        fields_list = [[self.email_label, self.email_input, self.email_validation_text],
                       [self.password_label, self.password_input, self.password_validation_text]]
        if validation.empty_fields_check(fields_list) != 0:
            return
        
        if validation.emai_check(self.email_input, self.email_validation_text) is False:
            return
        
        email = self.email_input.text().strip()
        password = self.password_input.text()

        employee = EmployeeController.get_employee_by_email(email)
        if employee and check_password(password, employee.password):
            self.authorization_successful.emit(employee)
        else:
            self.password_validation_text.setText("Неверный email или пароль")
            self.password_validation_text.setVisible(True)
        