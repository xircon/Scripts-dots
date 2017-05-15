#!/usr/bin/python

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *

# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it
#label = QLabel("Hello World")
label = QLabel("<font color=red size=40>Hello World</font>")
label.show()
# Enter Qt application main loop
app.exec_()
sys.exit()