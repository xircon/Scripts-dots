import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import (Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QVBoxLayout, QLabel,
        QPushButton)

def __init__(self):
    for i in range(0,10):
        self._numberButtons += [QPushButton(str(i), self)]
        self.connect(self._numberButtons[i], SIGNAL('clicked()'), lambda : self._number(i))

def _number(self, x):
    print(x)
