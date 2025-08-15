from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout
from PyQt6.QtGui import QFont
from widgets.breadcrumbs_widget import Breadcrumbs
from resources.colors import Color
from controllers.employee_access_controller import EmployeeAccessController
from controllers.access_controller import AccessController
from controllers.project_controller import ProjectController
from widgets.project_card_widget import ProjectCardWidget
from models.employee_model import Employee
from models.project_model import Project
from resources.accesses import AccessName
from PyQt6.QtCore import pyqtSignal

class ProjectsWidget(QWidget):
    project_card_update = pyqtSignal(Project)
    def __init__(self, current_employee: Employee = None):
        super().__init__()

        self.setStyleSheet(f"""
        QLabel{{
            color: {Color.DARK_BROWN.value};
        }}
        """)
        main_text_font = QFont("Verdana", 16, QFont.Weight.Normal)

        main_projects_layout = QVBoxLayout(self)
        main_projects_layout.setContentsMargins(20, 20, 20, 20)

        projects_title_label = QLabel("Проекты")
        projects_title_label.setFont(QFont("Verdana", 28, QFont.Weight.Normal))

        main_projects_layout.addWidget(projects_title_label)
        main_projects_layout.addWidget(Breadcrumbs(f"""Главная <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ Проекты</span>"""))

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        scroll_widget = QWidget()

        main_cards_layout = QVBoxLayout(scroll_widget)

        projects = ProjectController.get_all_projects()

        if current_employee:
            current_employee_accesses = [AccessController.get_access_name_by_id(emp_acc.access_id) for emp_acc in EmployeeAccessController.get_employee_accesses_by_id(current_employee.id)]
            for project in projects:
                card_layout = QHBoxLayout()
                card = ProjectCardWidget(project)

                card.project_update.connect(self.handle_project_card_update)

                if AccessName.UPDATING_PROJECTS.value in current_employee_accesses:
                    card.update_btn.setVisible(True)

                card_layout.addStretch()
                card_layout.addWidget(card)
                card_layout.addStretch()

                main_cards_layout.addLayout(card_layout)
        
        main_cards_layout.addStretch()

        scroll_area.setWidget(scroll_widget)
        main_projects_layout.addWidget(scroll_area)

    def handle_project_card_update(self, project: Project):
        self.project_card_update.emit(project)
