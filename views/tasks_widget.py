from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QComboBox, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFont
from widgets.breadcrumbs_widget import Breadcrumbs
from resources.colors import Color
from controllers.employee_access_controller import EmployeeAccessController
from controllers.access_controller import AccessController
from controllers.task_controller import TaskController
from controllers.project_controller import ProjectController
from controllers.status_controller import StatusController
from models.task_model import Task
from widgets.task_card_widget import TaskCardWidget
from widgets.check_box import CheckBox
from widgets.main_btn import MainBtn
from models.employee_model import Employee
from resources.accesses import AccessName
from PyQt6.QtCore import pyqtSignal
from controllers.filter_controller import apply_filters

class TasksWidget(QWidget):
    task_card_update = pyqtSignal(Task)
    task_card_show = pyqtSignal(Task)
    def __init__(self, current_employee: Employee = None):
        super().__init__()
        
        self.current_employee = current_employee

        self.setStyleSheet(f"""
        QLabel{{
            color: {Color.DARK_BROWN.value};
        }}
        QComboBox{{
            color: {Color.DARK_BROWN.value};
            padding: 10px;
            border: 1px solid {Color.DARK_BROWN.value};
            border-radius: 5px;
            background: {Color.LIGHT_GRAY_DARKER.value};
            max-width: 450px;
        }}
        """)

        main_text_font = QFont("Verdana", 16, QFont.Weight.Normal)

        main_tasks_layout = QVBoxLayout(self)
        main_tasks_layout.setContentsMargins(20, 20, 20, 20)

        tasks_title_label = QLabel("Задачи")
        tasks_title_label.setFont(QFont("Verdana", 28, QFont.Weight.Normal))

        main_tasks_layout.addWidget(tasks_title_label)
        main_tasks_layout.addWidget(Breadcrumbs(f"""Главная <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ Задачи</span>"""))

        filters_layout = QHBoxLayout()

        projects_filter_label = QLabel("Проекты")
        projects_filter_label.setFont(main_text_font)

        combo_box_width = 230
        space_between_filters = 20

        self.projects_filter_combo_box = QComboBox()
        self.projects_filter_combo_box.setFont(main_text_font)
        self.projects_filter_combo_box.setMinimumWidth(combo_box_width)
        self.projects_filter_combo_box.addItem("Все")
        self.projects_filter_combo_box.setCurrentIndex(0)

        self.projects = ProjectController.get_all_projects()
        for project in self.projects:
            self.projects_filter_combo_box.addItem(project.name)

        statuses_filter_label = QLabel("Статусы")
        statuses_filter_label.setFont(main_text_font)

        self.statuses_filter_combo_box = QComboBox()
        self.statuses_filter_combo_box.setFont(main_text_font)
        self.statuses_filter_combo_box.setMinimumWidth(combo_box_width)
        self.statuses_filter_combo_box.addItem("Все")
        self.statuses_filter_combo_box.setCurrentIndex(0)

        self.statuses = StatusController.get_all_statuses()
        for status in self.statuses:
            self.statuses_filter_combo_box.addItem(status.name)

        self.my_tasks_filter_check_box = CheckBox("Только мои задачи")

        self.apply_filters_btn = MainBtn("Применить", 5, 35)
        self.apply_filters_btn.setFont(main_text_font)
        self.apply_filters_btn.setMinimumWidth(130)
        self.apply_filters_btn.clicked.connect(self.clicked_apply_filters_btn)

        filters_layout.addWidget(projects_filter_label)
        filters_layout.addWidget(self.projects_filter_combo_box)
        filters_layout.addItem(QSpacerItem(space_between_filters, 1))
        filters_layout.addWidget(statuses_filter_label)
        filters_layout.addWidget(self.statuses_filter_combo_box)
        filters_layout.addItem(QSpacerItem(space_between_filters, 1))
        filters_layout.addWidget(self.my_tasks_filter_check_box)
        filters_layout.addStretch()
        filters_layout.addWidget(self.apply_filters_btn)

        main_tasks_layout.addLayout(filters_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        scroll_widget = QWidget()

        self.main_cards_layout = QVBoxLayout(scroll_widget)

        tasks = TaskController.get_all_tasks()

        self.draw_cards(tasks)

        # if current_employee:
        #     current_employee_accesses = [AccessController.get_access_name_by_id(emp_acc.access_id) for emp_acc in EmployeeAccessController.get_employee_accesses_by_id(current_employee.id)]
        #     for task in tasks:
        #         card_layout = QHBoxLayout()
        #         card = TaskCardWidget(task)

        #         card.task_update.connect(self.handle_task_card_update)
        #         card.task_show.connect(self.handle_task_card_show)

        #         if AccessName.UPDATING_TASKS.value in current_employee_accesses:
        #             card.update_btn.setVisible(True)

        #         card_layout.addStretch()
        #         card_layout.addWidget(card)
        #         card_layout.addStretch()

        #         self.main_cards_layout.addLayout(card_layout)
        
        self.main_cards_layout.addStretch()

        scroll_area.setWidget(scroll_widget)
        main_tasks_layout.addWidget(scroll_area)

    def handle_task_card_update(self, task: Task):
        self.task_card_update.emit(task)

    def handle_task_card_show(self, task: Task):
        self.task_card_show.emit(task)

    def draw_cards(self, tasks: list[Task]):
        for i in reversed(range(self.main_cards_layout.count())):
            item = self.main_cards_layout.itemAt(i)
            if item.widget():
                widget = item.widget()
                widget.deleteLater()
            elif item.layout():
                layout = item.layout()
                for j in reversed(range(layout.count())):
                    widget = layout.itemAt(j).widget()
                    if widget:
                        widget.deleteLater()
            self.main_cards_layout.removeItem(item)

        if self.current_employee:
            current_employee_accesses = [AccessController.get_access_name_by_id(emp_acc.access_id) for emp_acc in EmployeeAccessController.get_employee_accesses_by_id(self.current_employee.id)]
            for task in tasks:
                card_layout = QHBoxLayout()
                card = TaskCardWidget(task)

                card.task_update.connect(self.handle_task_card_update)
                card.task_show.connect(self.handle_task_card_show)

                if AccessName.UPDATING_TASKS.value in current_employee_accesses:
                    card.update_btn.setVisible(True)

                card_layout.addStretch()
                card_layout.addWidget(card)
                card_layout.addStretch()

                self.main_cards_layout.addLayout(card_layout)
    
    def clicked_apply_filters_btn(self):
        filters_tasks = apply_filters(self.projects_filter_combo_box.currentText(),
                                      self.statuses_filter_combo_box.currentText(),
                                      self.my_tasks_filter_check_box.isChecked(),
                                      self.current_employee.id)
        
        self.draw_cards(filters_tasks)
        