import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("My Window")

        
        self.startButton = QPushButton("Start", self)
        self.startButton.setGeometry(200, 200, 100, 100)
        self.startButton.clicked.connect(self.button_clicked)

        # Set the window dimensions (width, height)
        self.setGeometry(100, 100, 500, 400)

    def button_clicked (self, button_clicked):
        print("Button clicked")
