from PyQt6.QtWidgets import QPlainTextEdit
from PyQt6.QtCore import Qt
from resources.colors import Color

class InputAreaText(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"""
        border: 1px solid {Color.DARK_BROWN.value};
        border-radius: 5px;
        padding: 10px;
        background: {Color.GRAY.value};
        color: {Color.DARK_BROWN.value};
        max-width: 450px;
        min-width: 200px;
        """)