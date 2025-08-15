from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
from resources.colors import Color

class IconBtn(QPushButton):
    def __init__(self, icon_name: str, color_hover: Color, color_pressed: Color):
        super().__init__()

        self.setIcon(QIcon(f"resources/icons/{icon_name}"))
        self.setIconSize(QSize(20, 20))
        self.setStyleSheet(f"""
        QPushButton
        {{
            border-radius: 6px;
            padding: 5px;
            background: transparent;
        }}
        QPushButton:hover
        {{
            background: {color_hover};
        }}
        QPushButton:pressed
        {{
            background: {color_pressed};
        }}
        QPushButton:focus {{
            outline: none;
        }}
        """)