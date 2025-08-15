from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame
from resources.colors import Color
from PyQt6.QtGui import QFont
from models.task_model import Task
from widgets.icon_btn import IconBtn
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import Qt
from controllers.status_controller import StatusController
from controllers.priority_controller import PriorityController
from controllers.project_controller import ProjectController
from controllers.employee_controller import EmployeeController

class TaskCardWidget(QFrame):
    task_show = pyqtSignal(Task)
    task_update = pyqtSignal(Task)
    def __init__(self, task: Task):
        super().__init__()

        self.setMinimumWidth(480)
        self.task = task
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

        name_layout = QHBoxLayout()
        name_layout.setContentsMargins(0, 0, 0, 20)
        name_label = QLabel(self.task.name)
        name_label.setMinimumWidth(400)
        name_label.setWordWrap(True)
        name_label.setTextFormat(Qt.TextFormat.RichText)
        name_label.setFont(title_text_font)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        name_layout.addWidget(name_label)

        start_date_label = QLabel(f"""<span style="font-weight: normal;">Дата начала:</span> {task.start_date.strftime("%d.%m.%Y")}""")
        start_date_label.setFont(main_text_font)

        deadline_date_label = QLabel(f"""<span style="font-weight: normal;">Дедлайн:</span> {task.deadline_date.strftime("%d.%m.%Y")}""")
        deadline_date_label.setFont(main_text_font)

        end_date_label = QLabel(f"""<span style="font-weight: normal;">Дата завершения:</span> {task.end_date.strftime("%d.%m.%Y") if task.end_date is not None else '-'}""")
        end_date_label.setFont(main_text_font)

        status_label = QLabel(f"""<span style="font-weight: normal;">Статус:</span> {StatusController.get_status_name_by_id(task.status_id)}""")
        status_label.setFont(main_text_font)

        priority_label = QLabel(f"""<span style="font-weight: normal;">Приоритет:</span> {PriorityController.get_priority_name_by_id(task.priority_id)}""")
        priority_label.setFont(main_text_font)

        project_label = QLabel(f"""<span style="font-weight: normal;">Проект:</span> {ProjectController.get_project_name_by_id(task.project_id)}""")
        project_label.setFont(main_text_font)

        author_employee = EmployeeController.get_employee_by_id(task.author_id)
        if author_employee:
            author_label = QLabel(f"""<span style="font-weight: normal;">Автор:</span> {author_employee.last_name} {author_employee.first_name} {author_employee.patronymic if author_employee.patronymic is not None else ''}""")
        else:
            author_label = QLabel(f"""<span style="font-weight: normal;">Автор:</span> -""")
        author_label.setFont(main_text_font)

        programmer_employee = EmployeeController.get_employee_by_id(task.executor_id)
        if programmer_employee:
            programmer_label = QLabel(f"""<span style="font-weight: normal;">Программист:</span> {programmer_employee.last_name} {programmer_employee.first_name} {programmer_employee.patronymic if programmer_employee.patronymic is not None else ''}""")
        else:
            programmer_label = QLabel(f"""<span style="font-weight: normal;">Программист:</span> -""")
        programmer_label.setFont(main_text_font)

        tester_employee = EmployeeController.get_employee_by_id(task.tester_id)
        if tester_employee:
            tester_label = QLabel(f"""<span style="font-weight: normal;">Тестировщик:</span> {tester_employee.last_name} {tester_employee.first_name} {tester_employee.patronymic if tester_employee.patronymic is not None else ''}""")
        else:
            tester_label = QLabel(f"""<span style="font-weight: normal;">Тестировщик:</span> -""")
        tester_label.setFont(main_text_font)

        icons_btn = QHBoxLayout()

        self.show_btn = IconBtn("show_icon_brown.png", Color.LIGHT_GRAY.value, Color.LIGHT_GRAY_DARKER.value)
        self.show_btn.clicked.connect(self.clicked_show_btn)

        self.update_btn = IconBtn("update_icon_brown.png", Color.LIGHT_GRAY.value, Color.LIGHT_GRAY_DARKER.value)
        self.update_btn.clicked.connect(self.clicked_update_btn)
        self.update_btn.setVisible(False)

        icons_btn.addStretch()
        icons_btn.addWidget(self.show_btn)
        icons_btn.addWidget(self.update_btn)
        icons_btn.addStretch()

        main_card_layout.addLayout(name_layout)
        main_card_layout.addWidget(start_date_label)
        main_card_layout.addWidget(deadline_date_label)
        main_card_layout.addWidget(end_date_label)
        main_card_layout.addWidget(status_label)
        main_card_layout.addWidget(priority_label)
        main_card_layout.addWidget(project_label)
        main_card_layout.addWidget(author_label)
        main_card_layout.addWidget(programmer_label)
        main_card_layout.addWidget(tester_label)
        main_card_layout.addLayout(icons_btn)

    def clicked_show_btn(self):
        self.task_show.emit(self.task)
    
    def clicked_update_btn(self):
        self.task_update.emit(self.task)