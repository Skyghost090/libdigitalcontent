#!/usr/bin/python3
from PySide2 import QtWidgets
from ui import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
window = Window()
window.show()
app.exec_()
