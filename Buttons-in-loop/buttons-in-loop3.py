#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout, QPushButton

from functools import partial

from collections import OrderedDict

import os

but_width = 300
butnum = 1
voffset = 60

gui_width = 800
gui_height = 700

class Window(QtGui.QMainWindow):
    def __init__(self):
         super(Window, self).__init__()
         self.setGeometry(50, 50, gui_width, gui_height)
         self.setWindowTitle("Test Label-GUI")

         def pos_button():
             if butnum % 2 > 0:
                 lm1=20
             else:
                 lm1=420
             return lm1;

         #Format 'label':'progname'
         dic=OrderedDict()
         dic['Medit - Text Editor'] = 'medit'
         dic['Catfish - Find Files'] = 'catfish'
         dic['Sakura - Run a terminal'] = 'sakura'
         dic['Gmrun - Run a command'] = 'gmrun'
         dic['PCmanFM - Run a file manager'] = 'pcmanfm'
         dic['GPrename - Bulk File rename utility'] = 'pcmanfm'

         vbox = QVBoxLayout(self)

         global butnum
         butnum = 1

         myFont = QtGui.QFont()
         myFont.setBold(True)

         ltxt1="This is a test label"
         len1 = len(ltxt1)
         lbl1 = QtGui.QLabel(ltxt1, self)
         lbl1.setFont(myFont)
         lbl1.setFixedWidth(gui_width)
         lbl1.setAlignment(QtCore.Qt.AlignHCenter)
         vbox.addWidget(lbl1)

         for key,value in dic.items():
             btemp = butnum
             btn = QPushButton(key, self)
             btn.setFixedWidth(but_width)
             btn.clicked.connect(partial(self.doit, value))
             lm1 = pos_button()
             if btemp % 2 == 0: btemp=btemp-1
             btn.move(lm1, (btemp*20)+voffset)
             butnum += 1
             vbox.addWidget(btn)


    def doit(self, text):
        print("%s" % text)
        os.system(text)

if __name__ == "__main__":
    app = QApplication([])
    w = Window()
    w.show()
    app.exec_()
