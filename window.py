from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QGridLayout
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        self.buttons = []  # Store buttons in a list
        self.button_layout = QGridLayout()
        self.layout.addLayout(self.button_layout)

        button_labels = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        for i, label in enumerate(button_labels):
            button = QPushButton(label)
            self.buttons.append(button)  # Add button to the list
            self.button_layout.addWidget(button, i // 4, i % 4)

    def update_display(self, text):
        """Update the display with the given text."""
        self.display.setText(text)