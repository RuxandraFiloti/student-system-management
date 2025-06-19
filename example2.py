# Import the components that you need in your app
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, \
    QPushButton, QComboBox
import sys 
from datetime import datetime

class SpeedCalculator(QWidget): #QWidget creates a window
    def __init__(self): # Constructor of the AgeCalculator class -> overwriting the __init__ method
        super().__init__() # Call the constructor of the parent class -> QWidget
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout() #QGridLayout creates a grid layout

    #Create widgets
        distance_label = QLabel("Distance: ") #QLabel creates a label
        self.distance_line_edit = QLineEdit() #QLineEdit creates textbox

        time_label = QLabel("Time(hours): ") #QLabel creates a label
        self.time_line_edit = QLineEdit() #QLineEdit creates textbox

        self.unit_combo = QComboBox() #QComboBox creates a dropdown menu
        self.unit_combo.addItems(['Metric (km)', 'Imperial(miles)'] )

        calculate_button = QPushButton("Calculate") #QPushButton creates a button
        calculate_button.clicked.connect(self.calculate) # Connect the button to the calculate_age method
        self.output_label = QLabel("")


# Add widgets to the grid layout

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid) # Set the layout of the window to the grid layout (you can see the widgets in the window)
    
    def calculate(self):
       #Get distance and time from the input fields
       distance = float(self.distance_line_edit.text())
       time = float(self.time_line_edit.text())

       #calculate average speed

       speed = distance / time

       #check the selected unit and convert speed to the appropriate unit

       if self.unit_combo.currentText() == 'Metric (km)':
           speed =  round(speed, 2)
           unit = "km/h"

       if self.unit_combo.currentText() == 'Imperial(miles)':
           speed = round(speed * 0.621371, 2)
           unit = "mph"
         #Display the result in the output label
       self.output_label.setText(f"Average speed: {speed} {unit}")
        
app = QApplication(sys.argv) # Create an instance of QApplication

calculator = SpeedCalculator() # Create an instance of the AgeCalculator class

calculator.show()  # Show the window

sys.exit(app.exec()) # Start the event loop and exit when done