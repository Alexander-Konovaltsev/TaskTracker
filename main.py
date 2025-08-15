# import utils.database_init
import sys
from PyQt6.QtWidgets import QApplication
from views.main_window_view import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
