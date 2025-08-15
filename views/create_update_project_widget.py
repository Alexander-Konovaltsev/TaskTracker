from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSignal
from widgets.breadcrumbs_widget import Breadcrumbs
from widgets.input_line_text import InputLineText
from widgets.validation_text import ValidationText
from widgets.input_area_text import InputAreaText
from widgets.main_btn import MainBtn
from resources.colors import Color
from models.project_model import Project
from controllers.project_controller import ProjectController
import utils.validation as validation

class CreateUpdateProjectWidget(QWidget):
    create_update_project_success = pyqtSignal()
    def __init__(self, project: Project=None):
        super().__init__()

        self.current_project = project

        self.setStyleSheet(f"""
        QLabel{{
            color: {Color.DARK_BROWN.value};
        }}
        """)
        main_text_font = QFont("Verdana", 16, QFont.Weight.Normal)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        create_project_title_label = QLabel("Создать проект")
        create_project_title_label.setFont(QFont("Verdana", 28, QFont.Weight.Normal))

        breadcrumbs = Breadcrumbs(f"""Главная <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ Создать проект</span>""")

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        scroll_widget = QWidget()

        main_create_project_layout = QVBoxLayout(scroll_widget)

        self.name_label = QLabel("Название")
        self.name_label.setFont(main_text_font)

        self.name_input = InputLineText(False)
        self.name_input.setFont(main_text_font)

        self.name_validation_text = ValidationText()

        self.description_label = QLabel("Описание")
        self.description_label.setFont(main_text_font)

        self.description_input = InputAreaText()
        self.description_input.setFont(main_text_font)

        self.create_update_project_btn = MainBtn("Создать", 5, 35)
        self.create_update_project_btn.setFont(main_text_font)
        self.create_update_project_btn.setMaximumWidth(120)
        self.create_update_project_btn.clicked.connect(self.create_update_project)

        main_create_project_layout.addWidget(self.name_label)
        main_create_project_layout.addWidget(self.name_input)
        main_create_project_layout.addWidget(self.name_validation_text)

        main_create_project_layout.addWidget(self.description_label)
        main_create_project_layout.addWidget(self.description_input)

        main_create_project_layout.addWidget(self.create_update_project_btn)

        main_create_project_layout.addStretch()

        scroll_area.setWidget(scroll_widget)

        main_layout.addWidget(create_project_title_label)
        main_layout.addWidget(breadcrumbs)
        main_layout.addWidget(scroll_area)

        if self.current_project:
            self.create_update_project_btn.setText("Изменить")
            create_project_title_label.setText(f"{self.current_project.name}")
            breadcrumbs.breadcrumbs_text.setText(f"""Главная / Проекты <span style="color: {Color.LIGHT_LIGHT_BROWN.value};">/ {self.current_project.name}</span>""")
            self.name_input.setText(self.current_project.name)
            self.description_input.setPlainText(self.current_project.description)


    def create_update_project(self):
        fields_list = [[self.name_label, self.name_input, self.name_validation_text]]

        if validation.empty_fields_check(fields_list) != 0:
            return
        
        if not self.current_project:
            project = Project(name=self.name_input.text().strip(),
                            description=self.description_input.toPlainText().strip() if not self.description_input.toPlainText().isspace() and len(self.description_input.toPlainText().strip()) > 0 else None)
            
            ProjectController.create_project(project)
        else:
            ProjectController.update_project(self.current_project.id,
                                             self.name_input.text().strip(),
                                             self.description_input.toPlainText().strip() if not self.description_input.toPlainText().isspace() and len(self.description_input.toPlainText().strip()) > 0 else None)
            
        self.create_update_project_success.emit()
