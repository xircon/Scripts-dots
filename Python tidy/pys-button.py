#!/usr/bin/python
# -'''- coding: utf-8 -'''-
 
import sys, os
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtGui
 
def sayHello():
    os.system("variety -n")
def prev():
    os.system("variety -p")

 
# Create the Qt Application
app = QApplication(sys.argv)
grid = QtGui.QGridLayout()
grid.addWidget(QtGui.QLabel(''), 0, 2)
# Create a button, connect it and show it

button = QtGui.QPushButton("Next")
button.clicked.connect(sayHello)
button.show()

button2 = QtGui.QPushButton("Previous")
button2.clicked.connect(prev)
button2.show()


# Run the main Qt loop
app.exec_()
