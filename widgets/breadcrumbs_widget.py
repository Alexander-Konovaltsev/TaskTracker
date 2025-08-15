from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtGui import QFont
from resources.colors import Color

class Breadcrumbs(QWidget):
    def __init__(self, text: str):
        super().__init__()

        breadcrumbs_layout = QHBoxLayout(self)
        breadcrumbs_layout.setContentsMargins(0, 0, 0, 0)

        self.breadcrumbs_text = QLabel(text)
        self.breadcrumbs_text.setFont(QFont("Verdana", 12, QFont.Weight.Normal))

        breadcrumbs_layout.addWidget(self.breadcrumbs_text)

        self.setStyleSheet(f"""
        QWidget{{
            background: {Color.LIGHT_GRAY.value};
            color: {Color.BROWN.value};
            padding: 10px;
            border-radius: 5px;
        }}
        """)
