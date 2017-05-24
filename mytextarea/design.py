# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(918, 618)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 36, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 88, 541))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Butt1 = QtGui.QPushButton(self.layoutWidget)
        self.Butt1.setObjectName(_fromUtf8("Butt1"))
        self.verticalLayout.addWidget(self.Butt1)
        self.Butt2 = QtGui.QPushButton(self.layoutWidget)
        self.Butt2.setObjectName(_fromUtf8("Butt2"))
        self.verticalLayout.addWidget(self.Butt2)
        self.Butt3 = QtGui.QPushButton(self.layoutWidget)
        self.Butt3.setObjectName(_fromUtf8("Butt3"))
        self.verticalLayout.addWidget(self.Butt3)
        self.Butt4 = QtGui.QPushButton(self.layoutWidget)
        self.Butt4.setObjectName(_fromUtf8("Butt4"))
        self.verticalLayout.addWidget(self.Butt4)
        self.Butt5 = QtGui.QPushButton(self.layoutWidget)
        self.Butt5.setObjectName(_fromUtf8("Butt5"))
        self.verticalLayout.addWidget(self.Butt5)
        self.Butt6 = QtGui.QPushButton(self.layoutWidget)
        self.Butt6.setObjectName(_fromUtf8("Butt6"))
        self.verticalLayout.addWidget(self.Butt6)
        self.Butt7 = QtGui.QPushButton(self.layoutWidget)
        self.Butt7.setObjectName(_fromUtf8("Butt7"))
        self.verticalLayout.addWidget(self.Butt7)
        self.Butt8 = QtGui.QPushButton(self.layoutWidget)
        self.Butt8.setObjectName(_fromUtf8("Butt8"))
        self.verticalLayout.addWidget(self.Butt8)
        self.Butt9 = QtGui.QPushButton(self.layoutWidget)
        self.Butt9.setObjectName(_fromUtf8("Butt9"))
        self.verticalLayout.addWidget(self.Butt9)
        self.Butt10 = QtGui.QPushButton(self.layoutWidget)
        self.Butt10.setObjectName(_fromUtf8("Butt10"))
        self.verticalLayout.addWidget(self.Butt10)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 10, 791, 551))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 36, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textEdit.setPalette(palette)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 570, 541, 32))
        self.layoutWidget1.setMaximumSize(QtCore.QSize(541, 16777215))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Butt11 = QtGui.QPushButton(self.layoutWidget1)
        self.Butt11.setMaximumSize(QtCore.QSize(130, 16777215))
        self.Butt11.setObjectName(_fromUtf8("Butt11"))
        self.horizontalLayout.addWidget(self.Butt11)
        self.Butt12 = QtGui.QPushButton(self.layoutWidget1)
        self.Butt12.setMaximumSize(QtCore.QSize(130, 16777215))
        self.Butt12.setObjectName(_fromUtf8("Butt12"))
        self.horizontalLayout.addWidget(self.Butt12)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.textEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Butt1.setText(_translate("MainWindow", "inxi", None))
        self.Butt2.setText(_translate("MainWindow", "PushButton", None))
        self.Butt3.setText(_translate("MainWindow", "PushButton", None))
        self.Butt4.setText(_translate("MainWindow", "PushButton", None))
        self.Butt5.setText(_translate("MainWindow", "PushButton", None))
        self.Butt6.setText(_translate("MainWindow", "PushButton", None))
        self.Butt7.setText(_translate("MainWindow", "PushButton", None))
        self.Butt8.setText(_translate("MainWindow", "PushButton", None))
        self.Butt9.setText(_translate("MainWindow", "PushButton", None))
        self.Butt10.setText(_translate("MainWindow", "PushButton", None))
        self.Butt11.setText(_translate("MainWindow", "Copy to Clipboard", None))
        self.Butt12.setText(_translate("MainWindow", "Quit", None))

