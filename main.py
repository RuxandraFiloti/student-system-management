from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, \
    QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, \
    QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton

from PyQt6.QtGui import QAction
import sys 
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")  # Create a File menu
        help_menu_item = self.menuBar().addMenu("&Help")  # Create a File menu

        add_student_action = QAction("Add Student", self) # Create an action for adding a student -> subitem in the File menu
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self) # Create an action for the About dialog -> subitem in the Help menu
        help_menu_item.addAction(about_action)
        
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False) # Hide the vertical header
        self.setCentralWidget(self.table)
    
    #load data from the database and display it in the table
    def load_data(self):
        connection = sqlite3.connect("database.db")  # Connect to the database
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data))) #coordinate of the cell
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()
class InsertDialog(QDialog):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        layout = QVBoxLayout()

        #Add student name 
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Enter Student Name")
        layout.addWidget(self.student_name)

        #Add combo box
        self.course_name = QComboBox()
        courses = ["Computer Science", "Mathematics", "Physics", "Chemistry"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        #Add mobile number
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Enter Student Name")
        layout.addWidget(self.mobile)

        #Add submit button
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)
    
    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        connection = sqlite3.connect("database.db")  # Connect to the database
        cursor = connection.cursor() # for inserting data
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        student_system.load_data()


app = QApplication(sys.argv) # Create an instance of QApplication

student_system = MainWindow() # Create an instance of the AgeCalculator class

student_system.show()  # Show the window

student_system.load_data()  # Load data from the database into the table

sys.exit(app.exec()) # Start the event loop and exit when done