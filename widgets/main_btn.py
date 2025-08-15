from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
from resources.colors import Color

class MainBtn(QPushButton):
    def __init__(self, text, border_radius: int, min_height: int, icon_name: str = None):
        super().__init__()

        if icon_name:
            self.setFont(QFont("Verdana", 12, QFont.Weight.Bold))
            self.setIcon(QIcon(f"resources/icons/{icon_name}"))
            self.setIconSize(QSize(20, 20))

        self.setText(text)
        self.setStyleSheet(f"""
        QPushButton
        {{
            text-align: center;
            min-height: {min_height}px;
            background: {Color.ORANGE.value};
            color: {Color.WHITE.value};
            border-radius: {border_radius}px;
        }}
        QPushButton:hover
        {{
            background: {Color.DARK_ORANGE.value};
        }}
        QPushButton:pressed
        {{
            background: {Color.LIGHT_ORANGE.value};
        }}
        QPushButton:focus {{
            outline: none;
        }}
        """)