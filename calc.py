from PyQt6.QtWidgets import QMainWindow, QGraphicsBlurEffect, QApplication, QDialog, QLabel, QPushButton, QVBoxLayout

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle("Calculator")
