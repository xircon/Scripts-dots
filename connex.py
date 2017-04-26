#!/usr/bin/env python3
# Copyright (c) 2008-9 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.
###########################################
## And bastardised by xirconuk@gmail.com ##
###########################################

import sys
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import (Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QVBoxLayout, QLabel,
        QPushButton, QHBoxLayout)


class Form(QDialog):
#class Window(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        button5 = QPushButton("Five")
        #self.label = QLabel("Click a button...")

        layout = QVBoxLayout()
        layout.stretch
        layout.addWidget(button1)
        button1.move(100,100)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        layout.addStretch()
        #layout.addWidget(self.label)
        self.setLayout(layout)

        self.button1callback = lambda who="1": self.anyButton(who)
        self.connect(button1, SIGNAL("clicked()"), self.button1callback)

        self.button2callback = lambda who="2": self.anyButton(who)
        self.connect(button2, SIGNAL("clicked()"), self.button2callback)

        self.button3callback = lambda who="3": self.anyButton(who)
        self.connect(button3, SIGNAL("clicked()"), self.button3callback)

        self.button4callback = lambda who="4": self.anyButton(who)
        self.connect(button4, SIGNAL("clicked()"), self.button4callback)

        self.button5callback = lambda who="5": self.anyButton(who)
        self.connect(button5, SIGNAL("clicked()"), self.button5callback)

        self.setWindowTitle("Connections")

    def anyButton(self, who):
        run_cmd = ["Filler!", "medit", "gmrun", "pamac-manager", "wm-switcher", "angrysearch"]
        #self.label.setText("You clicked button '{0}'".format(who))
        a = int(who)
        os.system(run_cmd[a])

app = QApplication(sys.argv)
form = Form()
form.show()
#window = Window()
#window.show()
app.exec_()
