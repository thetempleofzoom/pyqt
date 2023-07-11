from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, \
    QGridLayout, QLineEdit, QPushButton, QComboBox, QTableWidget, \
    QTableWidgetItem, QDialog, QVBoxLayout
from PyQt6.QtGui import QAction
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management Portal")
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")
        edit_menu = self.menuBar().addMenu("&Edit")

        #add menu item
        add_student = QAction("Add Student", self)
        #when add_student chosen
        add_student.triggered.connect(self.insert)
        about = QAction("About", self)
        #??
        about.setMenuRole(QAction.MenuRole.NoRole)
        search_student = QAction("Search for Student", self)
        search_student.triggered.connect(self.search)

        file_menu.addAction(add_student)
        help_menu.addAction(about)
        edit_menu.addAction(search_student)



        #add student table to main window. add 'self' to be able to connect to other
        #functions in class
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile" ))
        #remove column numbers
        self.table.verticalHeader().setVisible(False)

        #specify central widget for window
        self.setCentralWidget(self.table)
        
    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        #always puts cursor at 0 to avoid dups
        self.table.setRowCount(0)
        for index, row_data in enumerate(result):
            self.table.insertRow(index)
            for column, data in enumerate(row_data):
                self.table.setItem(index, column, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        #call insertdialog class
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        #call searchdialog class
        dialog = SearchDialog()
        dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert New Student Data")
        #gd practice for dialog window
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("name")
        layout.addWidget(self.student_name)

        self.student_class = QComboBox()
        classes = ["Biology", "Math", "Literature", "English", "Physics"]
        self.student_class.addItems(classes)
        layout.addWidget(self.student_class)

        self.student_mobile = QLineEdit()
        self.student_mobile.setPlaceholderText("mobile")
        layout.addWidget(self.student_mobile)

        submit = QPushButton("Submit")
        submit.clicked.connect(self.add_student)
        layout.addWidget(submit)

        self.setLayout(layout)

    def add_student(self):
        #import variable values
        name = self.student_name.text()
        course = self.student_class.currentText()
        mobile = int(self.student_mobile.text())
        #add entry into sql database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?,?,?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        #refresh table
        mainwindow.load_data()
        

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student Database")
        #gd practice for dialog window
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.search_student = QLineEdit()
        self.search_student.setPlaceholderText("search by name")
        layout.addWidget(self.search_student)

        submit = QPushButton("Search")
        submit.clicked.connect(self.find_student)
        layout.addWidget(submit)

        self.setLayout(layout)
    def find_student(self):
        #erase any highlighted items
        mainwindow.table.setCurrentItem(None)
        #no need to call up database. search in table itself. alternate code with SQL
        #query in test.py

        hits = mainwindow.table.findItems(self.search_student.text(), Qt.MatchFlag.MatchContains)
        if hits:
            for hit in hits:
                hit.setSelected(True)


app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
mainwindow.load_data()
#insert = InsertDialog()
#insert.show()
sys.exit(app.exec())
