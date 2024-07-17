from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import qdarktheme
import ctypes
from ctypes import *
import os

_load_lib = ctypes.cdll.LoadLibrary("./libdigitalcontent.so")
_load_lib.getUptime.restype = ctypes.c_int
activeHours = _load_lib.getUptime()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        qdarktheme.setup_theme("auto")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u"./digitalcontenticon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(-50, 50, 600, 350))
        self.dial.valueChanged.connect(lambda: dial_value())
        self.dial.setMaximum(24)
        self.dial.setMinimum(1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(285, 15, 200, 50))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"font-size:25px")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setText("Time Limit: " + str(self.dial.value()))

        def dial_value():
            value = self.dial.value()
            self.label_2.setText("Time Limit: " + str(value))

        def buttonClick():
            os.system("pkexec python3 " + os.getcwd() + "/service.py " + str(self.dial.value()) + " $(pwd) && systemctl start libdigitalcontent.service")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 400, 80, 80))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"border-color: transparent")
        icon1 = QIcon()
        icon1.addFile(u"./check_80dp_666666_FILL0_wght700_GRAD200_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(70, 70))
        self.pushButton.setFlat(False)
        self.pushButton.clicked.connect(lambda: buttonClick())
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(15, 15, 200, 50))
        self.label_3.setStyleSheet(u"font-size: 25px")
        self.label_3.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Digital Content", None))
        #self.label_2.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Active Hours: " + str(activeHours), None))
