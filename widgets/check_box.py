from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtGui import QFont
from resources.colors import Color

class CheckBox(QCheckBox):
    def __init__(self, text: str):
        super().__init__(text)

        main_text_font = QFont("Verdana", 16, QFont.Weight.Normal)
        self.setStyleSheet(f"""
        QCheckBox {{
            color: {Color.DARK_BROWN.value};
        }}
        QCheckBox::indicator {{
                width: 16px;
                height: 16px;
        }}
        QCheckBox::indicator:checked {{
            background-color: {Color.ORANGE.value};
            border: 1px solid {Color.ORANGE.value};
            border-radius: 4px;
            image: url(resources/icons/galka_icon.png)
        }}
        QCheckBox::indicator:unchecked {{
            background-color: {Color.WHITE.value};
            border: 2px solid {Color.ORANGE.value};
            border-radius: 4px; 
        }}
        """)
        self.setFont(main_text_font)
