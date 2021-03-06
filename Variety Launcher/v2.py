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
from PyQt4.QtGui import (QApplication, QDialog, QVBoxLayout, QLabel, QPushButton)

class Form(QDialog):



    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        button_labels = ["Next", "Previous", "Delete", "View", "Pause", "History", "Downloads"]

        i=0
        button1 = QPushButton(button_labels[i])
        button2 = QPushButton(button_labels[i+1])
        button3 = QPushButton(button_labels[i+2])
        button4 = QPushButton(button_labels[i+3])
        button5 = QPushButton(button_labels[i+4])
        button6 = QPushButton(button_labels[i+5])
        button7 = QPushButton(button_labels[i+6])

        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(button7)

        layout.addStretch()
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

        self.button6callback = lambda who="6": self.anyButton(who)
        self.connect(button6, SIGNAL("clicked()"), self.button6callback)

        self.button7callback = lambda who="7": self.anyButton(who)
        self.connect(button7, SIGNAL("clicked()"), self.button7callback)

        self.setWindowTitle("Variety")

    def anyButton(self, who):
        run_cmd = ["filler","variety -n", "variety -p", "variety -t", "xdg-open `cat ~/currentwp`", "variety --pause", "variety --history", "variety --downloads"]

        a = int(who)
        print(run_cmd[a])
        os.system(run_cmd[a])

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
