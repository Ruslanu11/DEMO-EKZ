from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
import sys
from client.ui.main_window_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget
from query.selects import select_user_


class TableDataHandler:
    @staticmethod
    def populate_table(table, data):
        if isinstance(table, QtWidgets.QTableWidget) and isinstance(data, list):
            table.setRowCount(len(data))
            for row, item in enumerate(data):
                for col, value in enumerate(item):
                    table_item = QtWidgets.QTableWidgetItem(str(value))
                    table.setItem(row, col, table_item)

class MainWindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def show_data_user(self):
        data = select_user_()
        TableDataHandler.populate_table(self.tableWidget, data)

app = QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
app.exec_()


