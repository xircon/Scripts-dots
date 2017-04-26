#!/usr/bin/env python
from PyQt4 import QtGui

import os

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)

# "Next", "Previous", "Delete", "View", "Pause", "History", "Downloads"

        self.button1 = QtGui.QPushButton('Next', self)
        self.button1.clicked.connect(self.handleButton1)
        layout.addWidget(self.button1)

        self.button2 = QtGui.QPushButton('Previous', self)
        self.button2.clicked.connect(self.handleButton2)
        layout.addWidget(self.button2)

        self.button3 = QtGui.QPushButton('Delete', self)
        self.button3.clicked.connect(self.handleButton3)
        layout.addWidget(self.button3)

        self.button4 = QtGui.QPushButton('View', self)
        self.button4.clicked.connect(self.handleButton4)
        layout.addWidget(self.button4)

        self.button5 = QtGui.QPushButton('Pause', self)
        self.button5.clicked.connect(self.handleButton5)
        layout.addWidget(self.button5)

        self.button6 = QtGui.QPushButton('History', self)
        self.button6.clicked.connect(self.handleButton6)
        layout.addWidget(self.button6)

        self.button7 = QtGui.QPushButton('Downloads', self)
        self.button7.clicked.connect(self.handleButton7)
        layout.addWidget(self.button7)
# "variety -n", "variety -p", "variety -t", "xdg-open `cat ~/currentwp`", "variety --pause", "variety --history", "variety --downloads"

    def handleButton1(self):
        #next image
        os.system("variety -n")

    def handleButton2(self):
        #previous image
        os.system("variety -p")

    def handleButton3(self):
        #Delete (trash)
        os.system("variety -t")

    def handleButton4(self):
        #launch image in default viewer - requires minor alteration to
        #variety set wallpaper script.
        os.system("xdg-open `cat ~/currentwp`")

    def handleButton5(self):
        #pause variety
        os.system("variety --pause")

    def handleButton6(self):
        #pause variety
        os.system("variety --history")

    def handleButton7(self):
        #pause variety
        os.system("variety --downloads")

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
