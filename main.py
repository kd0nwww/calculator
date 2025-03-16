import sys
from PyQt6.QtWidgets import QApplication
from calc import Calculator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Calculator()
    MainWindow.show()
    sys.exit(app.exec())