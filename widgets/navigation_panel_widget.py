from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLayout
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import pyqtSignal
from resources.colors import Color
from .navigation_panel_btn import NavigationPanelBtn
from .main_btn import MainBtn
from .icon_btn import IconBtn

class NavigationPanel(QWidget):
    exit_from_account = pyqtSignal()
    show_user_info = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setFixedWidth(280)

        navigation_panel_layout = QVBoxLayout(self)
        navigation_panel_layout.setContentsMargins(0, 20, 0, 0)

        logo_layout = QHBoxLayout()

        icon_label = QLabel()
        icon_pixmap = QPixmap("resources/icons/task_icon.png").scaled(45, 45)
        icon_label.setPixmap(icon_pixmap)

        logo_text_label = QLabel("ТАСК\nТРЕКЕР")
        logo_text_font = QFont("Verdana", 18, QFont.Weight.Bold)
        logo_text_label.setFont(logo_text_font)
        logo_text_label.setStyleSheet(f"color: {Color.WHITE.value}")

        logo_layout.addStretch()
        logo_layout.addWidget(icon_label)
        logo_layout.addWidget(logo_text_label)
        logo_layout.addStretch()

        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setContentsMargins(0, 55, 0, 0)

        self.projects_btn = NavigationPanelBtn("project_icon.png", "  Проекты")
        self.tasks_btn = NavigationPanelBtn("task_second_icon.png", "  Задачи")
        self.employees_btn = NavigationPanelBtn("employee_icon.png", "  Сотрудники")

        self.create_buttons_layout = QVBoxLayout()
        self.create_buttons_layout.setContentsMargins(12, 20, 12, 0)
        
        border_radius_create_btn = 17
        min_height_create_btn = 35
        icon_name_create_btn = "plus_icon.png"

        self.create_project_btn = MainBtn("Создать проект", border_radius_create_btn, min_height_create_btn, icon_name_create_btn)
        self.create_task_btn = MainBtn("Создать задачу", border_radius_create_btn, min_height_create_btn, icon_name_create_btn)
        self.create_employee_btn = MainBtn("Добавить сотрудника", border_radius_create_btn, min_height_create_btn, icon_name_create_btn)

        self.user_info_layout = QHBoxLayout()
        self.user_info_layout.setContentsMargins(5, 20, 5, 0)

        avatar_label = QLabel()
        avatar_pixmap = QPixmap("resources/icons/avatar_icon.png").scaled(30, 30)
        avatar_label.setPixmap(avatar_pixmap)

        self.user_fio_label = QLabel("Фамилия Имя Отчество")
        self.user_fio_label.setStyleSheet("text-align: center;")
        user_fio_font = QFont("Verdana", 10, QFont.Weight.Bold)
        self.user_fio_label.setFont(user_fio_font)
        self.user_fio_label.setStyleSheet(f"color: {Color.WHITE.value}")

        self.icon_btn_layout = QHBoxLayout()
        self.icon_btn_layout.setContentsMargins(0, 0, 0, 12)

        self.show_user_btn = IconBtn("show_icon.png", Color.DARK_ORANGE.value, Color.LIGHT_ORANGE.value)
        self.show_user_btn.clicked.connect(lambda: self.show_user_info.emit())

        self.exit_btn = IconBtn("exit_icon.png", Color.DARK_ORANGE.value, Color.LIGHT_ORANGE.value)
        self.exit_btn.clicked.connect(self.exit_from_user_account)

        self.buttons_layout.addWidget(self.projects_btn)
        self.buttons_layout.addWidget(self.tasks_btn)
        self.buttons_layout.addWidget(self.employees_btn)

        self.create_buttons_layout.addWidget(self.create_project_btn)
        self.create_buttons_layout.addWidget(self.create_task_btn)
        self.create_buttons_layout.addWidget(self.create_employee_btn)

        self.user_info_layout.addStretch()
        self.user_info_layout.addWidget(avatar_label)
        self.user_info_layout.addWidget(self.user_fio_label)
        self.user_info_layout.addStretch()

        self.icon_btn_layout.addStretch()
        self.icon_btn_layout.addWidget(self.show_user_btn)
        self.icon_btn_layout.addWidget(self.exit_btn)
        self.icon_btn_layout.addStretch()

        navigation_panel_layout.addLayout(logo_layout)
        navigation_panel_layout.addLayout(self.buttons_layout)
        navigation_panel_layout.addLayout(self.create_buttons_layout)
        navigation_panel_layout.addStretch()
        navigation_panel_layout.addLayout(self.user_info_layout)
        navigation_panel_layout.addLayout(self.icon_btn_layout)
    
    def exit_from_user_account(self):
        self.make_invisible_all_layouts()
        self.exit_from_account.emit()
    
    def make_invisible_all_layouts(self):
        layouts = [self.buttons_layout, 
                   self.create_buttons_layout, 
                   self.user_info_layout, 
                   self.icon_btn_layout]
        for layout in layouts:
            self.make_invisible_layout(layout)
    
    def make_invisible_layout(self, layout: QLayout):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.setVisible(False)

    def make_visible_layout(self, layout: QLayout):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.setVisible(True)
