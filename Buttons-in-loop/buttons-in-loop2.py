#!/usr/bin/env python

from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout, QPushButton
from functools import partial
from collections import OrderedDict

import os

class MainWidget(QWidget):
    def __init__(self):
         super(MainWidget, self).__init__()
         self.setWindowTitle("JWMConf-GUI")


         #Format 'label':'progname'
         dic=OrderedDict()
         dic['Medit - Text Editor'] = 'medit'
         dic['Catfish - Find Files'] = 'catfish'
         dic['Sakura - Run a terminal'] = 'sakura'
         dic['Gmrun - Run a command'] = 'gmrun'

         vbox = QVBoxLayout(self)

         for key,value in dic.items():
             btn = QPushButton(key, self)
             btn.clicked.connect(partial(self.doit, value))
             vbox.addWidget(btn)


    def doit(self, text):
        print("%s" % text)
        os.system(text)

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet("QPushButton{background: blue} QPushButton::hover{background: lightyellow}\
    MainWidget{background: lightgreen}")
    w = MainWidget()
    w.show()
    app.exec_()
