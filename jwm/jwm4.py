import sys

import os

from PyQt4 import QtGui, QtCore

from functools import partial

from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout, QPushButton

from collections import OrderedDict

#Button Width
bw1 = 300

#gui dimensions
gui_width=800
gui_height=700
voffset=60

global lm1
lm1=0

global lm2
lm2=420

dic=OrderedDict()
dic['Medit - Text Editor'] = 'medit'
dic['Catfish - Find Files'] = 'catfish'
dic['Sakura - Run a terminal'] = 'sakura'
dic['Gmrun - Run a command'] = 'gmrun'


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, gui_width, gui_height)
        self.setWindowTitle("Test Title")
        self.setWindowIcon(QtGui.QIcon('manjaro.png'))

#    def home(self):

#        def pos_button():
#            if btnnum % 2 > 0:
#                lm1=20
#            else:
#                lm1=420
#            return lm1;

            #Format 'label':'progname'


        for key,value in list(dic.items()):
            btnnum=1
            btn = QPushButton(key, self)
            btn.setFixedWidth(bw1)
            btn.clicked.connect(partial(self.doit, value))
            #lm1=pos_button()
            lm1=0
            btn.move(lm1,(btnnum*20)+voffset)
            btnnum+=1

            self.show()


        myFont = QtGui.QFont()
        myFont.setBold(True)

        ltxt1="\nThis is a test label"
        len1 = len(ltxt1)
        lbl1 = QtGui.QLabel(ltxt1, self)
        lbl1.setFont(myFont)
        lbl1.setFixedWidth(gui_width)
        lbl1.setAlignment(QtCore.Qt.AlignHCenter)

        self.show()

    def doit(self, text):
        print("%s" % text)
        os.system(text)




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
