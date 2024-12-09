import sys
from PyQt6.QtWidgets import (
                             QMainWindow, 
                             QPushButton,
                             QComboBox,
                             QSpinBox, 
                             QLabel
                             )

from FlowModel import FlowModel
from SubSetModel import SubSetModel
from LazyConstraintsModel import LazyConstraintsModel
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.number_of_cities = 5

        # Set the window title
        self.setWindowTitle("My Window")
        
        # Set the window dimensions (width, height)
        self.setGeometry(100, 100, 500, 400)

        self.model_option_label = QLabel("Select model: ")
        self.model_option_label.setGeometry(30, 80, 100, 30)

        # Model selector combobox
        self.model_option_combobox = QComboBox()
        self.model_option_combobox.setGeometry(150, 80, 200, 30)
        self.model_option_combobox.setPlaceholderText("Select an option")
        self.model_option_combobox.addItem("Subset-model")
        self.model_option_combobox.addItem("Lazy-constraints model")
        self.model_option_combobox.addItem("Flow model")
        self.model_option_combobox.currentIndexChanged.connect(self.comboboxSelectionChanged)

        # City number spin box
        self.number_of_cities_selector = QSpinBox()
        self.number_of_cities_selector.setValue(self.number_of_cities)
        self.number_of_cities_selector.setGeometry(150, 50, 50, 20)
        self.number_of_cities_selector.setRange(0, 200)
        self.number_of_cities_selector.valueChanged.connect(self.updateNumberOfCities)

        self.solution_status_label = QLabel("")

        # Start button
        self.start_button = QPushButton("Start")
        self.start_button.setGeometry(200, 200, 100, 100)
        self.start_button.clicked.connect(self.buttonClicked)
        self.start_button.setEnabled(False)


        layout = self.layout()
        layout.addItem(self.model_option_combobox)
        layout.addItem(self.number_of_cities_selector)
        layout.addItem(self.start_button)
        layout.addItem(self.solution_status_label)


    # Slot that updates the number of cities after spin box change. 
    def updateNumberOfCities(self, value):
        self.number_of_cities = value

    # Slot that updates the model that should be run after combobox change.
    def comboboxSelectionChanged(self, index):
        selected_text = self.model_option_combobox.currentText()
        print(f"Selected: {selected_text}")
        self.start_button.setEnabled(True)

    # Slots that starts the optimization.
    def buttonClicked (self, button_clicked):
        selected_index = self.model_option_combobox.currentIndex()

        cities_positions = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(self.number_of_cities)]

        new_model = None
        if selected_index == 0:
            new_model = SubSetModel(cities_positions)
        elif selected_index == 1:
            new_model = LazyConstraintsModel(cities_positions)
        elif selected_index == 2:
            new_model = FlowModel(cities_positions)

        self.solution_status_label.setText(new_model.solution_status)
