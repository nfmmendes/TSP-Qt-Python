import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QPushButton,
                             QComboBox,
                             QSpinBox, 
                             )

from SubSetModel import SubSetModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.numberOfCities = 5

        # Set the window title
        self.setWindowTitle("My Window")
        
        # Set the window dimensions (width, height)
        self.setGeometry(100, 100, 500, 400)

        # Start button
        self.startButton = QPushButton("Start", self)
        self.startButton.setGeometry(200, 200, 100, 100)
        self.startButton.clicked.connect(self.button_clicked)
        self.startButton.setEnabled(False)

        # Model selector combobox
        self.modelOptionCombobox = QComboBox(self)
        self.modelOptionCombobox.setGeometry(50, 50, 200, 30)
        self.modelOptionCombobox.setPlaceholderText("Select an option")
        self.modelOptionCombobox.addItem("Subset-model")
        self.modelOptionCombobox.addItem("Lazy-constraints model")
        self.modelOptionCombobox.addItem("Flow model")
        self.modelOptionCombobox.currentIndexChanged.connect(self.combobox_selection_changed)

        # City number spin box
        self.numberOfCitiesSelector = QSpinBox(self)
        self.numberOfCitiesSelector.setValue(self.numberOfCities)
        self.numberOfCitiesSelector.setGeometry(300, 50, 50, 20)
        self.numberOfCitiesSelector.setRange(0, 200)
        self.numberOfCitiesSelector.valueChanged.connect(self.updateNumberOfCities)

    def updateNumberOfCities(self, value):
        self.numberOfCities = value

    def combobox_selection_changed(self, index):
        selected_text = self.modelOptionCombobox.currentText()
        print(f"Selected: {selected_text}")
        self.startButton.setEnabled(True)

    def button_clicked (self, button_clicked):
        newModel = SubSetModel(self.numberOfCities)
