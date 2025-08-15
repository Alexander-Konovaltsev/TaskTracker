from PyQt6.QtWidgets import QLineEdit
from resources.colors import Color

class InputLineText(QLineEdit):
    def __init__(self, is_secure: bool):
        super().__init__()

        self.setStyleSheet(f"""
        QLineEdit{{
            color: {Color.DARK_BROWN.value};
            padding: 10px;
            border: 1px solid {Color.DARK_BROWN.value};
            border-radius: 5px;
            background: {Color.GRAY.value};
            max-width: 450px;
            min-width: 200px;
        }}
        """)
        self.setEchoMode(QLineEdit.EchoMode.Password if is_secure else QLineEdit.EchoMode.Normal)
