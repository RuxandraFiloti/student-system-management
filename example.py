# Import the components that you need in your app
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, \
    QPushButton, QMessageBox
import sys 
from datetime import datetime

class AgeCalculator(QWidget): #QWidget creates a window
    def __init__(self): # Constructor of the AgeCalculator class -> overwriting the __init__ method
        super().__init__() # Call the constructor of the parent class -> QWidget
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout() #QGridLayout creates a grid layout

    #Create widgets
        name_label = QLabel("Name: ") #QLabel creates a label
        self.name_line_edit = QLineEdit() #QLineEdit creates textbox

        date_birth_label = QLabel("Date of Birth MM/DD/YYYY: ") #QLabel creates a label
        self.date_birth_line_edit = QLineEdit() #QLineEdit creates textbox

        calculate_button = QPushButton("Calculate Age") #QPushButton creates a button
        calculate_button.clicked.connect(self.calculate_age) # Connect the button to the calculate_age method
        self.output_label = QLabel("")


# Add widgets to the grid layout

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid) # Set the layout of the window to the grid layout (you can see the widgets in the window)
    
    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_birth_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old")



        
app = QApplication(sys.argv) # Create an instance of QApplication

age_calculator = AgeCalculator() # Create an instance of the AgeCalculator class

age_calculator.show()  # Show the window

sys.exit(app.exec()) # Start the event loop and exit when done