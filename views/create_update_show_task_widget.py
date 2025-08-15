from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QDate
from widgets.breadcrumbs_widget import Breadcrumbs
from resources.colors import Color
from models.task_model import Task
from widgets.input_line_text import InputLineText
from widgets.validation_text import ValidationText
from widgets.input_area_text import InputAreaText
from widgets.main_btn import MainBtn
from widgets.calendar_date_edit import CalendarDateEdit
from widgets.combo_box import ComboBox
import utils.validation as validation
from controllers.status_controller import StatusController
from controllers.project_controller import ProjectController
from controllers.priority_controller import PriorityController
from controllers.employee_controller import EmployeeController
from controllers.task_controller import TaskController
from models.status_model import Status
from models.project_model import Project
from models.priority_model import Priority
from models.employee_model import Employee
from resources.positions import PositionName
from resources.statuses import StatusName
from datetime import date
from PyQt6.QtCore import pyqtSignal

class CreateUpdateShowTaskWidget(QWidget):
    create_update_task_succees = pyqtSignal()
    def __init__(self, task: Task = None, show_flag: bool = None, current_employee: Employee = None):
        super().__init__()

        self.task = task
        self.show_flag = show_flag
        self.current_employee = current_employee

        self.setStyleSheet(f"""
        QLabel{{
            color: {Color.DARK_BROWN.value};
        }}
        """)
        main_text_font = QFont("Verdana", 16, QFont.Weight.Normal)

        breadcrumbs = Breadcrumbs(f"""Главная <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ Создать задачу</span>""")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        create_task_title_label = QLabel("Создать задачу")
        create_task_title_label.setFont(QFont("Verdana", 28, QFont.Weight.Normal))

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        scroll_widget = QWidget()

        main_create_task_layout = QVBoxLayout(scroll_widget)

        self.name_label = QLabel("Название")
        self.name_label.setFont(main_text_font)

        self.name_input = InputLineText(False)
        self.name_input.setFont(main_text_font)

        self.name_validation_text = ValidationText()

        self.description_label = QLabel("Описание")
        self.description_label.setFont(main_text_font)

        self.description_input = InputAreaText()
        self.description_input.setFont(main_text_font)

        self.start_date_label = QLabel("Дата начала")
        self.start_date_label.setFont(main_text_font)
        self.start_date_label.setVisible(False)

        self.start_date_input = InputLineText(False)
        self.start_date_input.setFont(main_text_font)
        self.start_date_input.setVisible(False)

        self.deadline_date_label = QLabel("Дедлайн")
        self.deadline_date_edit = CalendarDateEdit()
        self.deadline_date_edit.setFont(main_text_font)
        self.deadline_date_edit.setCalendarPopup(True)
        self.deadline_date_edit.setDate(QDate.currentDate())

        self.end_date_label = QLabel("Дата завершения")
        self.end_date_label.setFont(main_text_font)
        self.end_date_label.setVisible(False)

        self.end_date_input = InputLineText(False)
        self.end_date_input.setFont(main_text_font)
        self.end_date_input.setVisible(False)

        self.status_label = QLabel("Статус")
        self.status_label.setFont(main_text_font)

        self.status_combo_box = ComboBox()
        self.status_combo_box.setFont(main_text_font)
        self.status_combo_box.setPlaceholderText('Выберите...')

        self.statuses = StatusController.get_all_statuses()
        for status in self.statuses:
            self.status_combo_box.addItem(status.name)
        self.status_combo_box.setCurrentIndex(0)

        self.status_validation_text = ValidationText()

        self.priority_label = QLabel("Приоритет")
        self.priority_label.setFont(main_text_font)

        self.priority_combo_box = ComboBox()
        self.priority_combo_box.setFont(main_text_font)
        self.priority_combo_box.setPlaceholderText('Выберите...')

        self.priorities = PriorityController.get_all_priorities()
        for priority in self.priorities:
            self.priority_combo_box.addItem(priority.name)

        self.priority_validation_text = ValidationText()

        self.project_label = QLabel("Проект")
        self.project_label.setFont(main_text_font)

        self.project_combo_box = ComboBox()
        self.project_combo_box.setFont(main_text_font)
        self.project_combo_box.setPlaceholderText('Выберите...')

        self.projects = ProjectController.get_all_projects()
        for project in self.projects:
            self.project_combo_box.addItem(project.name)

        self.project_validation_text = ValidationText()

        self.author_label = QLabel("Автор")
        self.author_label.setFont(main_text_font)
        self.author_label.setVisible(False)

        self.author_input = InputLineText(False)
        self.author_input.setFont(main_text_font)
        self.author_input.setVisible(False)

        self.executor_label = QLabel("Программист")
        self.executor_label.setFont(main_text_font)

        self.executor_combo_box = ComboBox()
        self.executor_combo_box.setFont(main_text_font)
        self.executor_combo_box.setPlaceholderText('Выберите...')

        self.programmers = EmployeeController.get_employees_by_position_name(PositionName.PROGRAMMER.value)
        self.employess_info = {}
        for employee in self.programmers:
            self.executor_combo_box.addItem(f"{employee.last_name} {employee.first_name} {employee.patronymic if employee.patronymic is not None else ''}")
            self.employess_info[employee.id] = f"{employee.last_name} {employee.first_name} {employee.patronymic if employee.patronymic is not None else ''}"

        self.executor_validation_text = ValidationText()

        self.tester_label = QLabel("Тестировщик")
        self.tester_label.setFont(main_text_font)

        self.tester_combo_box = ComboBox()
        self.tester_combo_box.setFont(main_text_font)
        self.tester_combo_box.setPlaceholderText('Выберите...')

        self.testers = EmployeeController.get_employees_by_position_name(PositionName.TESTER.value)
        for employee in self.testers:
            self.tester_combo_box.addItem(f"{employee.last_name} {employee.first_name} {employee.patronymic if employee.patronymic is not None else ''}")
            self.employess_info[employee.id] = f"{employee.last_name} {employee.first_name} {employee.patronymic if employee.patronymic is not None else ''}"

        self.tester_validation_text = ValidationText()

        self.create_update_task_btn = MainBtn("Создать", 5, 35)
        self.create_update_task_btn.setFont(main_text_font)
        self.create_update_task_btn.setMaximumWidth(120)
        self.create_update_task_btn.clicked.connect(self.create_update_task)

        main_create_task_layout.addWidget(self.name_label)
        main_create_task_layout.addWidget(self.name_input)
        main_create_task_layout.addWidget(self.name_validation_text)

        main_create_task_layout.addWidget(self.description_label)
        main_create_task_layout.addWidget(self.description_input)

        main_create_task_layout.addWidget(self.start_date_label)
        main_create_task_layout.addWidget(self.start_date_input)

        main_create_task_layout.addWidget(self.deadline_date_label)
        main_create_task_layout.addWidget(self.deadline_date_edit)

        main_create_task_layout.addWidget(self.end_date_label)
        main_create_task_layout.addWidget(self.end_date_input)

        main_create_task_layout.addWidget(self.status_label)
        main_create_task_layout.addWidget(self.status_combo_box)
        main_create_task_layout.addWidget(self.status_validation_text)

        main_create_task_layout.addWidget(self.priority_label)
        main_create_task_layout.addWidget(self.priority_combo_box)
        main_create_task_layout.addWidget(self.priority_validation_text)

        main_create_task_layout.addWidget(self.project_label)
        main_create_task_layout.addWidget(self.project_combo_box)
        main_create_task_layout.addWidget(self.project_validation_text)

        main_create_task_layout.addWidget(self.author_label)
        main_create_task_layout.addWidget(self.author_input)

        main_create_task_layout.addWidget(self.executor_label)
        main_create_task_layout.addWidget(self.executor_combo_box)
        main_create_task_layout.addWidget(self.executor_validation_text)

        main_create_task_layout.addWidget(self.tester_label)
        main_create_task_layout.addWidget(self.tester_combo_box)
        main_create_task_layout.addWidget(self.tester_validation_text)

        main_create_task_layout.addWidget(self.create_update_task_btn)

        main_create_task_layout.addStretch()

        scroll_area.setWidget(scroll_widget)

        main_layout.addWidget(create_task_title_label)
        main_layout.addWidget(breadcrumbs)
        main_layout.addWidget(scroll_area)

        if self.task:
            create_task_title_label.setText(self.task.name)
            breadcrumbs.breadcrumbs_text.setText(f"""Главная / Задачи <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ {self.task.name}</span>""")

            self.name_input.setText(self.task.name)
            self.description_input.setPlainText(self.task.description)
            
            deadline_date = self.task.deadline_date
            qdate = QDate(deadline_date.year, deadline_date.month, deadline_date.day)
            self.deadline_date_edit.setDate(qdate)

            self.status_combo_box.setCurrentIndex(self.task.status_id - 1)
            self.priority_combo_box.setCurrentIndex(self.task.priority_id - 1)
            self.project_combo_box.setCurrentIndex(self.task.project_id - 1)
            
            for idx, prog in enumerate(self.programmers):
                if prog.id == self.task.executor_id:
                    self.executor_combo_box.setCurrentIndex(idx)

            for idx, test in enumerate(self.testers):
                if test.id == self.task.tester_id:
                    self.tester_combo_box.setCurrentIndex(idx)

            self.start_date_input.setText(self.task.start_date.strftime("%d.%m.%Y"))
            self.end_date_input.setText(self.task.end_date.strftime("%d.%m.%Y") if self.task.end_date is not None else '-')
            author = EmployeeController.get_employee_by_id(self.task.author_id)
            self.author_input.setText(f"{author.last_name} {author.first_name} {author.patronymic if author.patronymic is not None else ''}")

            if not self.show_flag:
                self.create_update_task_btn.setText("Изменить")
            else:
                self.create_update_task_btn.setVisible(False)

                self.start_date_label.setVisible(True)
                self.start_date_input.setVisible(True)

                self.end_date_label.setVisible(True)
                self.end_date_input.setVisible(True)

                self.author_label.setVisible(True)
                self.author_input.setVisible(True)

                self.make_disable_all_widgets_in_layout(main_create_task_layout)

    def create_update_task(self):
        fields_list = [[self.name_label, self.name_input, self.name_validation_text],
                        [self.status_label, self.status_combo_box, self.status_validation_text],
                        [self.priority_label, self.priority_combo_box, self.priority_validation_text],
                        [self.project_label, self.project_combo_box, self.project_validation_text],
                        [self.executor_label, self.executor_combo_box, self.executor_validation_text],
                        [self.tester_label, self.tester_combo_box, self.tester_validation_text]]
        
        if validation.empty_fields_check(fields_list) != 0:
            return      

        qdate_deadline = self.deadline_date_edit.date()
        deadline_date = date(qdate_deadline.year(), qdate_deadline.month(), qdate_deadline.day())

        programmer_id = None
        tester_id = None
        for key, value in self.employess_info.items():
            if value == self.executor_combo_box.currentText():
                programmer_id = key
            if value == self.tester_combo_box.currentText():
                tester_id = key

        if not self.task:
            qdate_today = QDate.currentDate()
            start_date = date(qdate_today.year(), qdate_today.month(), qdate_today.day())
            end_date = None
            if self.status_combo_box.currentText() == StatusName.CLOSE.value:
                end_date = start_date

            task = Task(name=self.name_input.text().strip(),
                        description=self.description_input.toPlainText().strip() if not self.description_input.toPlainText().isspace() and len(self.description_input.toPlainText().strip()) > 0 else None,
                        start_date=start_date,
                        end_date=end_date,
                        deadline_date=deadline_date,
                        status_id=StatusController.get_status_id_by_name(self.status_combo_box.currentText()),
                        priority_id=PriorityController.get_priority_id_by_name(self.priority_combo_box.currentText()),
                        project_id=ProjectController.get_project_id_by_name(self.project_combo_box.currentText()),
                        author_id=self.current_employee.id,
                        executor_id=programmer_id,
                        tester_id=tester_id)

            TaskController.create_task(task)
        else:
            end_date = None
            if self.status_combo_box.currentText() == StatusName.CLOSE.value and self.task.end_date is None:
                qdate_today = QDate.currentDate()
                end_date = date(qdate_today.year(), qdate_today.month(), qdate_today.day())

            TaskController.update_task(task_id=self.task.id,
                                       name=self.name_input.text().strip(),
                                       description=self.description_input.toPlainText().strip() if not self.description_input.toPlainText().isspace() and len(self.description_input.toPlainText().strip()) > 0 else None,
                                       deadline_date=deadline_date,
                                       status_id=StatusController.get_status_id_by_name(self.status_combo_box.currentText()),
                                       priority_id=PriorityController.get_priority_id_by_name(self.priority_combo_box.currentText()),
                                       project_id=ProjectController.get_project_id_by_name(self.project_combo_box.currentText()),
                                       executor_id=programmer_id,
                                       tester_id=tester_id,
                                       end_date=end_date)

        self.create_update_task_succees.emit()

    def make_disable_all_widgets_in_layout(self, layout: QLayout):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.setEnabled(False)
