from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from resources.colors import Color

class ValidationText(QLabel):
    def __init__(self, text: str = ""):
        super().__init__()

        self.setStyleSheet(f"""
        color: {Color.RED.value};
        font-size: 12px;
        padding: 0px;
        """)
        self.setText(text)
        self.setVisible(False)
