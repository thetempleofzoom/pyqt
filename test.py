import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, \
    QGridLayout, QLineEdit, QPushButton, QComboBox, QTableWidget, \
    QTableWidgetItem, QDialog, QVBoxLayout, QToolBar, QStatusBar, \
    QMessageBox

class DeleteDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("Delete Student Record")

        #index = mainwindow.table.currentRow()
        #id = mainwindow.table.item(index, 0).text()
        #tbd = mainwindow.table.item(index, 1).text()
        tbd = 'aston martin'
        reply = self.question(self, 'delete student record', f"Delete {tbd}'s record?",
                      self.StandardButton.Ok | self.StandardButton.Cancel)
        if reply == self.StandardButton.Ok:
            print('deleted')
        else:
            self.close()

        #self.setText(f"Delete {tbd}'s record?")
        #self.setStandardButtons(self.StandardButton.Ok | self.StandardButton.Cancel)


app = QApplication(sys.argv)
msg = DeleteDialog()
msg.exec()
sys.exit(app.exec())

