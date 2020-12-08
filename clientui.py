# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(805, 603)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(18)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, -30, 201, 91))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(196, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(158, 30, 41, 20))
        self.lineEdit_2.setCursorPosition(13)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(101, 350, 231, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 350, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(100, 55, 271, 271))
        self.textBrowser_2.setObjectName("textBrowser_2")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MESSANGER"))
        self.label.setText(_translate("mainWindow", "Lookgram"))
        self.lineEdit.setPlaceholderText(_translate("mainWindow", "Jack..."))
        self.lineEdit_2.setText(_translate("mainWindow", "         имя:"))
        self.textBrowser.setPlaceholderText(_translate("mainWindow", "Введите сообщение..."))
        self.pushButton.setText(_translate("mainWindow", ">"))




app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec_()
