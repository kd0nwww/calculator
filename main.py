import sys
from PyQt6.QtWidgets import QApplication
from calc import Calculator
from window import Window
from controller import CalculatorController
from PyQt6.QtCore import QFile, QTextStream

if __name__ == "__main__":
    app = QApplication(sys.argv)

    file = QFile("C:\Coding\Python\OOP\calculator\style.css")
    if file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
        stream = QTextStream(file)
        app.setStyleSheet(stream.readAll())
    else:
        print("Failed to load stylesheet")

    model = Calculator() 
    view = Window() 
    controller = CalculatorController(model, view) 

    view.show()

    sys.exit(app.exec())