#!/usr/bin/env python

import sys  # provides interaction with the Python interpreter
import os

from functools import partial
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot  # provides the 'pyqtSlot()' decorator
from PyQt4.QtCore import Qt  # provides Qt identifiers
from PyQt4.QtGui import QApplication, QPushButton


chkbut1=0
chkbut2=0
chkbut3=0
chkbut4=0
chkbut5=0
chkbut6=0
chkbut7=0
chkbut8=0
chkbut9=0
chkbut10=0

class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # creates the checkbox
        checkbox1 = QtGui.QCheckBox('&Inxi')  # the shortcut key is ALT + I
        checkbox2 = QtGui.QCheckBox('&xorg')  # the shortcut key is ALT + x
        checkbox3 = QtGui.QCheckBox('X&org.1 - (/var/log/Xorg.1.log)')
        checkbox4 = QtGui.QCheckBox('&pacman.log - (/var/log/pacman.log)')
        checkbox5 = QtGui.QCheckBox('journalctl.txt - (&Emergency)')
        checkbox6 = QtGui.QCheckBox('journalctl.txt - (&Alert)')
        checkbox7 = QtGui.QCheckBox('journalctl.txt - (&Critical)')
        checkbox8 = QtGui.QCheckBox('journalctl.txt - (&Failed)')
        checkbox9 = QtGui.QCheckBox('Spare 1')
        checkbox10 = QtGui.QCheckBox('Spare 2')
        btn = QPushButton("Click to Run", self)
        btn.setFocusPolicy(QtCore.Qt.ClickFocus)


        # connects the 'stateChanged()' signal with the 'checkbox_state_changed()' slot
        checkbox1.stateChanged.connect(self.checkbox1_state_changed)
        checkbox2.stateChanged.connect(self.checkbox2_state_changed)
        checkbox3.stateChanged.connect(self.checkbox3_state_changed)
        checkbox4.stateChanged.connect(self.checkbox4_state_changed)
        checkbox5.stateChanged.connect(self.checkbox5_state_changed)
        checkbox6.stateChanged.connect(self.checkbox6_state_changed)
        checkbox7.stateChanged.connect(self.checkbox7_state_changed)
        checkbox8.stateChanged.connect(self.checkbox8_state_changed)
        checkbox9.stateChanged.connect(self.checkbox9_state_changed)
        checkbox10.stateChanged.connect(self.checkbox10_state_changed)

        btn.clicked.connect(partial(self.doit))


        # creates a vertical box layout for the window
        vlayout = QtGui.QVBoxLayout()
        vlayout.addWidget(checkbox1)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox2)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox3)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox4)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox5)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox6)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox7)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox8)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox9)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox10)  # adds the checkbox to the layout
        vlayout.addWidget(btn)
        vlayout.addStretch()
        self.setLayout(vlayout)  # sets the window layout

    # 'checkbox_state_changed()' slot
    @pyqtSlot(int)
    def checkbox1_state_changed(self, state):
        global chkbut1
        if state == Qt.Checked:
            chkbut1=1
            print(chkbut1)  # debug
        else:
            chkbut1=0
            print(chkbut1)  # debug

    def checkbox2_state_changed(self, state):
        global chkbut2
        if state == Qt.Checked:
            chkbut2=1
            print(chkbut2)  # debug
        else:
            chkbut2=0
            print(chkbut2)  # debug

    def checkbox3_state_changed(self, state):
        global chkbut3
        if state == Qt.Checked:
            chkbut3=1
            print(chkbut3)  # debug
        else:
            chkbut3=0
            print(chkbut3)  # debug

    def checkbox4_state_changed(self, state):
        global chkbut4
        if state == Qt.Checked:
            chkbut4=1
            print(chkbut4)  # debug
        else:
            chkbut4=0
            print(chkbut4)  # debug

    def checkbox5_state_changed(self, state):
        global chkbut5
        if state == Qt.Checked:
            chkbut5=1
            print(chkbut5)  # debug
        else:
            chkbut5=0
            print(chkbut5)  # debug

    def checkbox6_state_changed(self, state):
        global chkbut6
        if state == Qt.Checked:
            chkbut6=1
            print(chkbut6)  # debug
        else:
            chkbut6=0
            print(chkbut6)  # debug

    def checkbox7_state_changed(self, state):
        global chkbut7
        if state == Qt.Checked:
            chkbut7=1
            print(chkbut7)  # debug
        else:
            chkbut7=0
            print(chkbut7)  # debug

    def checkbox8_state_changed(self, state):
        global chkbut8
        if state == Qt.Checked:
            chkbut8=1
            print(chkbut8)  # debug
        else:
            chkbut8=0
            print(chkbut8)  # debug

    def checkbox9_state_changed(self, state):
        global chkbut9
        if state == Qt.Checked:
            chkbut9=1
            print(chkbut9)  # debug
        else:
            chkbut9=0
            print(chkbut9)  # debug

    def checkbox10_state_changed(self, state):
        global chkbut10
        if state == Qt.Checked:
            chkbut10=1
            print(chkbut10)  # debug
        else:
            chkbut10=0
            print(chkbut10)  # debug




    def doit(self, text):
        #This is not pythonic - sort later <<<<<<<<<<<< !!!!!!!!!!!!!!!!!!!
        #Quick and dirty................
        os.system('rm -f /tmp/mlogsout.txt')
        os.system('touch /tmp/mlogsout.txt')
        if chkbut1 == 1:
           try:

              with open('/tmp/mlogsout.txt', 'w') as file:
                  file.write('\n')
                  file.write('===============\n')
                  file.write('| Inxi -Fxzc0 |   Listing computer information\n')
                  file.write('===============\n')
                  file.close()
                  os.system('inxi -Fxzc0 >> /tmp/mlogsout.txt')
                  #file.write('\n')
           except:
              print('Do you have installed: "inxi" on your system? ')

        if chkbut2 == 1:
           print("Filler")


        if chkbut3 == 1:
           print("Filler")

        if chkbut4 == 1:
           print("Filler")

        if chkbut5 == 1:
            print("Filler")


        if chkbut6 == 1:
            print("Filler")


        if chkbut7 == 1:
            print("Filler")


        if chkbut8 == 1:
            print("Filler")

        if chkbut9 == 1:
            print("Filler")

        if chkbut10 == 1:
            print("Filler")



# creates the application and takes arguments from the command line
application = QtGui.QApplication(sys.argv)

# creates the window and sets its properties
window = Window()
window.setWindowTitle('Log analyser')  # title
window.resize(280, 50)  # size
window.show()  # shows the window

# runs the application and waits for its return value at the end
sys.exit(application.exec_())
