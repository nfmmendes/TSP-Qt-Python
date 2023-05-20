import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QPushButton,
                             QComboBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("My Window")

        self.startButton = QPushButton("Start", self)
        self.startButton.setGeometry(200, 200, 100, 100)
        self.startButton.clicked.connect(self.button_clicked)
        self.startButton.setEnabled(False)

        # Set the window dimensions (width, height)
        self.setGeometry(100, 100, 500, 400)

        self.modelOptionCombobox = QComboBox(self)
        self.modelOptionCombobox.setGeometry(50, 50, 200, 30)
        self.modelOptionCombobox.setPlaceholderText("Select an option")
        self.modelOptionCombobox.addItem("Subset-model")
        self.modelOptionCombobox.addItem("Lazy-constraints model")
        self.modelOptionCombobox.addItem("Flow model")
        self.modelOptionCombobox.currentIndexChanged.connect(self.combobox_selection_changed)

    def combobox_selection_changed(self, index):
        selected_text = self.modelOptionCombobox.currentText()
        print(f"Selected: {selected_text}")
        self.startButton.setEnabled(True)

    def button_clicked (self, button_clicked):
        print("Button clicked")
