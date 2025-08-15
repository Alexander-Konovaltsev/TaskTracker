from PyQt6.QtWidgets import QDateEdit
from resources.colors import Color

class CalendarDateEdit(QDateEdit):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"""
        color: {Color.DARK_BROWN.value};
        padding: 10px;
        border: 1px solid {Color.DARK_BROWN.value};
        border-radius: 5px;
        background: {Color.GRAY.value};
        max-width: 450px;
        """)
