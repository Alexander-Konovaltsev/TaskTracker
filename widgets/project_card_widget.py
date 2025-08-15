from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame
from resources.colors import Color
from PyQt6.QtGui import QFont
from models.project_model import Project
from widgets.icon_btn import IconBtn
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import Qt

class ProjectCardWidget(QFrame):
    project_update = pyqtSignal(Project)
    def __init__(self, project: Project):
        super().__init__()

        self.setMinimumWidth(480)
        self.project = project
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
        name_label = QLabel(self.project.name)
        name_label.setFont(title_text_font)

        name_layout.addStretch()
        name_layout.addWidget(name_label)
        name_layout.addStretch()

        description_label = QLabel(f"""<span style="font-weight: normal;">Описание:</span> {self.project.description}""")
        description_label.setFont(main_text_font)
        description_label.setWordWrap(True)
        description_label.setTextFormat(Qt.TextFormat.RichText)

        icons_btn = QHBoxLayout()

        self.update_btn = IconBtn("update_icon_brown.png", Color.LIGHT_GRAY.value, Color.LIGHT_GRAY_DARKER.value)
        self.update_btn.clicked.connect(self.clicked_update_btn)
        self.update_btn.setVisible(False)

        icons_btn.addStretch()
        icons_btn.addWidget(self.update_btn)
        icons_btn.addStretch()

        main_card_layout.addLayout(name_layout)
        main_card_layout.addWidget(description_label)
        main_card_layout.addLayout(icons_btn)

    def clicked_update_btn(self):
        self.project_update.emit(self.project)