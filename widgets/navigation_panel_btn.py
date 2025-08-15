from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
from resources.colors import Color

class NavigationPanelBtn(QPushButton):
    def __init__(self, icon_name: str, text: str):
        super().__init__()

        self.setText(text)
        self.setFont(QFont("Verdana", 12, QFont.Weight.Bold))
        self.setIcon(QIcon(f"resources/icons/{icon_name}"))
        self.setIconSize(QSize(20, 20))
        self.setStyleSheet(f"""
        QPushButton
        {{
            text-align: left;
            padding-left: 20px;
            min-height: 40px;
            color: {Color.WHITE.value};
        }}
        QPushButton:hover
        {{
            background: {Color.BROWN.value};
        }}
        QPushButton:pressed
        {{
            background: {Color.LIGHT_BROWN.value};
        }}
        QPushButton:focus {{
            outline: none;
        }}
        """)
