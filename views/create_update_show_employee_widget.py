from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QDate
from widgets.calendar_date_edit import CalendarDateEdit
from widgets.combo_box import ComboBox
from widgets.check_box import CheckBox
from widgets.main_btn import MainBtn
from widgets.input_line_text import InputLineText
from widgets.validation_text import ValidationText
from widgets.breadcrumbs_widget import Breadcrumbs
from resources.colors import Color
import utils.validation as validation
from controllers.position_controller import PositionController
from controllers.access_controller import AccessController
from controllers.employee_controller import EmployeeController
from controllers.employee_access_controller import EmployeeAccessController
from models.employee_model import Employee
from models.employee_access_model import EmployeeAccess
from datetime import date
from utils.password_protect import hash_password
from PyQt6.QtCore import pyqtSignal

class CreateUpdateShowEmployeeWidget(QWidget):
    create_employee_success = pyqtSignal()
    def __init__(self, employee: Employee = None, show_flag: bool = None):
        super().__init__()

        self.employee = employee
        self.show_flag = show_flag

        self.setStyleSheet(f"""
        QLabel{{
            color: {Color.DARK_BROWN.value};
        }}
        """)
        main_text_font = QFont("Verdana", 16, QFont.Weight.Normal)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        breadcrumbs = Breadcrumbs(f"""Главная <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ Добавить сотрудника</span>""")

        scroll_widget = QWidget()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        main_create_employee_layout = QVBoxLayout(scroll_widget)

        create_employee_title_label = QLabel("Добавить сотрудника")
        create_employee_title_label.setFont(QFont("Verdana", 28, QFont.Weight.Normal))

        self.last_name_label = QLabel("Фамилия")
        self.last_name_label.setFont(main_text_font)

        self.last_name_input = InputLineText(False)
        self.last_name_input.setFont(main_text_font)

        self.last_name_validation_text = ValidationText()

        self.first_name_label = QLabel("Имя")
        self.first_name_label.setFont(main_text_font)

        self.first_name_input = InputLineText(False)
        self.first_name_input.setFont(main_text_font)

        self.first_name_validation_text = ValidationText()

        self.patronymic_label = QLabel("Отчество")
        self.patronymic_label.setFont(main_text_font)

        self.patronymic_input = InputLineText(False)
        self.patronymic_input.setFont(main_text_font)

        self.birth_date_label = QLabel("Дата Рождения")
        self.birth_date_label.setFont(main_text_font)

        self.birth_date_edit = CalendarDateEdit()
        self.birth_date_edit.setFont(main_text_font)
        self.birth_date_edit.setCalendarPopup(True)

        self.email_label = QLabel("Email")
        self.email_label.setFont(main_text_font)

        self.email_input = InputLineText(False)
        self.email_input.setFont(main_text_font)

        self.email_validation_text = ValidationText()

        self.password_label = QLabel("Пароль")
        self.password_label.setFont(main_text_font)

        self.password_input = InputLineText(True)
        self.password_input.setFont(main_text_font)

        self.password_validation_text = ValidationText()

        positions = PositionController.get_all_position()
        self.positions_label = QLabel("Должность")
        self.positions_label.setFont(main_text_font)

        self.positions_combo_box = ComboBox()
        self.positions_combo_box.setPlaceholderText('Выберите...')
        self.positions_combo_box.setFont(main_text_font)
        for position in positions:
            self.positions_combo_box.addItem(position.name)
        
        self.position_validation_text = ValidationText()

        self.accesses_label = QLabel("Доступы")
        self.employee_accesses_label = QLabel("У Вас нет специфичных доступов")
        self.employee_accesses_label.setFont(main_text_font)
        self.employee_accesses_label.setVisible(False)
        self.accesses_label.setFont(main_text_font)
        
        accesses = AccessController.get_all_access()
        self.check_boxes = [CheckBox(accees.name) for accees in accesses]

        create_update_employee_btn = MainBtn("Добавить", 5, 35)
        create_update_employee_btn.setFont(main_text_font)
        create_update_employee_btn.setMaximumWidth(120)
        create_update_employee_btn.clicked.connect(self.create_update_employee)
        
        main_layout.addWidget(create_employee_title_label)
        main_layout.addWidget(breadcrumbs)

        main_create_employee_layout.addWidget(self.last_name_label)
        main_create_employee_layout.addWidget(self.last_name_input)
        main_create_employee_layout.addWidget(self.last_name_validation_text)

        main_create_employee_layout.addWidget(self.first_name_label)
        main_create_employee_layout.addWidget(self.first_name_input)
        main_create_employee_layout.addWidget(self.first_name_validation_text)

        main_create_employee_layout.addWidget(self.patronymic_label)
        main_create_employee_layout.addWidget(self.patronymic_input)

        main_create_employee_layout.addWidget(self.birth_date_label)
        main_create_employee_layout.addWidget(self.birth_date_edit)

        main_create_employee_layout.addWidget(self.email_label)
        main_create_employee_layout.addWidget(self.email_input)
        main_create_employee_layout.addWidget(self.email_validation_text)

        main_create_employee_layout.addWidget(self.password_label)
        main_create_employee_layout.addWidget(self.password_input)
        main_create_employee_layout.addWidget(self.password_validation_text)

        main_create_employee_layout.addWidget(self.positions_label)
        main_create_employee_layout.addWidget(self.positions_combo_box)
        main_create_employee_layout.addWidget(self.position_validation_text)

        main_create_employee_layout.addWidget(self.accesses_label)
        main_create_employee_layout.addWidget(self.employee_accesses_label)
        for accees_check_box in self.check_boxes:
            main_create_employee_layout.addWidget(accees_check_box)

        main_create_employee_layout.addWidget(create_update_employee_btn)

        main_create_employee_layout.addStretch()

        scroll_area.setWidget(scroll_widget)

        main_layout.addWidget(scroll_area)

        if self.employee:
            breadcrumbs.breadcrumbs_text.setText(f"""Главная <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ {employee.last_name} {employee.first_name} {employee.patronymic if employee.patronymic is not None else ''}</span>""")
            create_employee_title_label.setText(f"{employee.last_name} {employee.first_name} {employee.patronymic if employee.patronymic is not None else ''}")

            self.last_name_input.setText(self.employee.last_name)
            self.first_name_input.setText(self.employee.first_name)
            self.patronymic_input.setText(self.employee.patronymic)
            birth_date = employee.birth_date
            qdate = QDate(birth_date.year, birth_date.month, birth_date.day)
            self.birth_date_edit.setDate(qdate)
            self.email_input.setText(self.employee.email)
            self.positions_combo_box.setCurrentIndex(self.employee.position_id - 1)
                      
        if self.employee and self.show_flag:
            create_update_employee_btn.setVisible(False)
            self.password_label.setVisible(False)
            self.password_input.setVisible(False)
            self.make_disable_all_widgets_in_layout(main_create_employee_layout)

            employee_accesses = EmployeeAccessController.get_employee_accesses_by_id(self.employee.id)
            if not employee_accesses:
                self.employee_accesses_label.setVisible(True)
                for check_box in self.check_boxes:
                    check_box.setVisible(False)
            else:
                for check_box in self.check_boxes:
                    if check_box.text() in [AccessController.get_access_name_by_id(access.access_id) for access in employee_accesses]:
                        check_box.setChecked(True)
                    else:
                        check_box.setVisible(False)

        if self.employee and not self.show_flag:
            breadcrumbs.breadcrumbs_text.setText(f"""Главная / Сотрудники <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ {employee.last_name} {employee.first_name} {employee.patronymic if employee.patronymic is not None else ''}</span>""")
            create_update_employee_btn.setText("Изменить")
            employee_accesses = EmployeeAccessController.get_employee_accesses_by_id(self.employee.id)
            for check_box in self.check_boxes:
                if check_box.text() in [AccessController.get_access_name_by_id(access.access_id) for access in employee_accesses]:
                    check_box.setChecked(True)

    def create_update_employee(self):
        if not self.employee:
            fields_list = [[self.last_name_label, self.last_name_input, self.last_name_validation_text],
                        [self.first_name_label, self.first_name_input, self.first_name_validation_text],
                        [self.email_label, self.email_input, self.email_validation_text],
                        [self.password_label, self.password_input, self.password_validation_text],
                        [self.positions_label, self.positions_combo_box, self.position_validation_text]]
        else:
            fields_list = [[self.last_name_label, self.last_name_input, self.last_name_validation_text],
                        [self.first_name_label, self.first_name_input, self.first_name_validation_text],
                        [self.email_label, self.email_input, self.email_validation_text],
                        [self.positions_label, self.positions_combo_box, self.position_validation_text]]
        
        if validation.empty_fields_check(fields_list) != 0:
            return
        
        if validation.emai_check(self.email_input, self.email_validation_text) is False:
            return
        
        employee_email = self.email_input.text().strip()
        if not self.employee:
            if EmployeeController.get_employee_by_email(employee_email) is not None:
                self.email_validation_text.setText("Сотрудник с данным email уже существует")
                self.email_validation_text.setVisible(True)
                return
        else:
            if self.employee.email != employee_email and EmployeeController.get_employee_by_email(employee_email) is not None:
                self.email_validation_text.setText("Сотрудник с данным email уже существует")
                self.email_validation_text.setVisible(True)
                return
        
        qdate = self.birth_date_edit.date()
        birth_date = date(qdate.year(), qdate.month(), qdate.day())
        if not self.employee:
            employee = Employee(
                last_name=self.last_name_input.text().strip(),
                first_name=self.first_name_input.text().strip(),
                patronymic=self.patronymic_input.text().strip() if not self.patronymic_input.text().isspace() and len(self.patronymic_input.text().strip()) > 0 else None,
                birth_date=birth_date,
                email=employee_email,
                password=hash_password(self.password_input.text()),
                position_id=PositionController.get_position_id_by_name(self.positions_combo_box.currentText()))
        
        
            employee = EmployeeController.create_employee(employee)

            employee_accesses = []
            for check_box_access in self.check_boxes:
                if check_box_access.isChecked():
                    employee_accesses.append(EmployeeAccess(employee_id=employee.id, access_id=AccessController.get_access_id_by_name(check_box_access.text())))

            if len(employee_accesses) > 0:
                EmployeeAccessController.create_employee_accesses(employee_accesses)
        else:
            EmployeeController.update_employee(self.employee.id,
                                               self.last_name_input.text().strip(),
                                               self.first_name_input.text().strip(),
                                               self.patronymic_input.text().strip() if not self.patronymic_input.text().isspace() and len(self.patronymic_input.text().strip()) > 0 else None,
                                               birth_date,
                                               employee_email,
                                               PositionController.get_position_id_by_name(self.positions_combo_box.currentText()),
                                               hash_password(self.password_input.text()) if len(self.password_input.text()) > 0 else None)
            
            employee_accesses_new = []
            for check_box_access in self.check_boxes:
                if check_box_access.isChecked():
                    employee_accesses_new.append(AccessController.get_access_id_by_name(check_box_access.text()))
            
            current_employee = EmployeeController.get_employee_by_email(self.employee.email)
            employee_accesses_old = [emp_acc.id for emp_acc in current_employee.accesses]

            accesses_id_for_add = []
            for new_access in employee_accesses_new:
                if new_access not in employee_accesses_old:
                    accesses_id_for_add.append(EmployeeAccess(employee_id=self.employee.id, access_id=new_access))

            accesses_id_for_del = []
            for old_access in employee_accesses_old:
                if old_access not in employee_accesses_new:
                    accesses_id_for_del.append(old_access)

            if len(accesses_id_for_add) > 0:
                EmployeeAccessController.create_employee_accesses(accesses_id_for_add)

            if len(accesses_id_for_del) > 0:
                EmployeeAccessController.delete_employee_accesses(accesses_id_for_del, self.employee.id)

        self.create_employee_success.emit()
    
    def make_disable_all_widgets_in_layout(self, layout: QLayout):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.setEnabled(False)
