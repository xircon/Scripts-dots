#!/usr/bin/env python

import sys
import os
import re

from PyQt4 import QtGui, QtCore

#sudo pip install roku first.
from roku import Roku

#set your IP here and rem out automatic discovery if automatic discovery fails.
#roku = Roku('192.168.0.7')

#Automatic discovery......
my_roku=Roku.discover(3) #2 second wait mostly works!!!! so use 3.
s1=str(my_roku)
s2=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s1).group()
print(s1, "|", s2) #for debug only
roku=Roku(s2)

#Button Width/Height
bw = 100
bw1 = 100
bh = 100
#gui dimensions
gui_width=400
gui_height=600
voffset=10

global lm1
lm1=0

icon_path="/home/steve/scripts/Roku-Remote/"

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, gui_width, gui_height)
        self.setWindowTitle("Roku Remote")
        self.setWindowIcon(QtGui.QIcon(icon_path + 'roku.png'))
        self.home()

    def handleBtn1(self): #up
        roku.up()

    def handleBtn2(self): #left
        roku.left()

    def handleBtn3(self): #right
        roku.right()

    def handleBtn4(self): #down
        roku.down()

    def handleBtn5(self): #select
        roku.select()

    def handleBtn6(self): #back
        roku.back()

    def handleBtn7(self): #home
        roku.home()

    def handleBtn8(self): #rewind
        roku.reverse()

    def handleBtn9(self): #play/pause
        roku.play()

    def handleBtn10(self): #Fastforward
        roku.forward()

    def handleBtn11(self): #info
        roku.info()

    def home(self):

        global btnnum
        btnnum=1 #up
        btn1 = QtGui.QPushButton("", self)
        btn1.clicked.connect(self.handleBtn1)
        btn1.setIcon(QtGui.QIcon(icon_path + 'triangle-64.png'))
        btn1.setIconSize(QtCore.QSize(100, 100))
        #Width, Height
        btn1.resize(bw,bh)
        btn1.move((gui_width-100)/2,90)

        btnnum=2 #left
        btn2 = QtGui.QPushButton("", self)
        btn2.clicked.connect(self.handleBtn2)
        btn2.setIcon(QtGui.QIcon(icon_path + 'triangle-64L.png'))
        btn2.setIconSize(QtCore.QSize(100, 100))
        btn2.resize(bw,bh)
        btn2.move(50,190)

        btnnum=3 #right
        btn3 = QtGui.QPushButton("", self)
        btn3.clicked.connect(self.handleBtn3)
        btn3.setIcon(QtGui.QIcon(icon_path + 'triangle-64R.png'))
        btn3.setIconSize(QtCore.QSize(100, 100))
        btn3.resize(bw,bh)
        btn3.move(250,190)

        btnnum=4 #down
        btn4 = QtGui.QPushButton("", self)
        btn4.clicked.connect(self.handleBtn4)
        btn4.setIcon(QtGui.QIcon(icon_path + 'triangle-64D.png'))
        btn4.setIconSize(QtCore.QSize(100, 100))
        btn4.resize(bw,bh)
        btn4.move((gui_width-100)/2,290)

        btnnum=5 #select
        btn5 = QtGui.QPushButton("", self)
        btn5.clicked.connect(self.handleBtn5)
        btn5.setIcon(QtGui.QIcon(icon_path + 'cd-64.png'))
        btn5.setIconSize(QtCore.QSize(100, 100))
        btn5.resize(bw,bh)
        btn5.move(150,190)

        btnnum=6 #back
        btn6 = QtGui.QPushButton("", self)
        btn6.clicked.connect(self.handleBtn6)
        btn6.setIcon(QtGui.QIcon(icon_path + 'arrow-back.png'))
        btn6.resize(60,60)
        btn6.move((gui_width-60)/2,400)

        btnnum=7 #home
        btn7 = QtGui.QPushButton("", self)
        btn7.clicked.connect(self.handleBtn7)
        btn7.setIcon(QtGui.QIcon(icon_path + 'home.png'))
        btn7.resize(60,60)
        btn7.move((gui_width-280)/2,400)

        btnnum=8 #rewind
        btn8 = QtGui.QPushButton("", self)
        btn8.clicked.connect(self.handleBtn8)
        btn8.setIcon(QtGui.QIcon(icon_path + 'rewind.png'))
        btn8.resize(60,60)
        btn8.move((gui_width-250)/2,500)

        btnnum=9 #play/Pause
        btn9 = QtGui.QPushButton("", self)
        btn9.clicked.connect(self.handleBtn9)
        btn9.setIcon(QtGui.QIcon(icon_path + 'play.png'))
        btn9.setIconSize(QtCore.QSize(50, 50))
        btn9.resize(60,60)
        btn9.move((gui_width-60)/2,500)

        btnnum=10 #Fastforward
        btn10 = QtGui.QPushButton("", self)
        btn10.clicked.connect(self.handleBtn10)
        btn10.setIcon(QtGui.QIcon(icon_path + 'fast-forward.png'))
        btn10.resize(60,60)
        btn10.move((gui_width-60+200)/2,500)

        btnnum=11 #info
        btn11 = QtGui.QPushButton("", self)
        btn11.clicked.connect(self.handleBtn11)
        btn11.setIcon(QtGui.QIcon(icon_path + 'info.png'))
        btn11.resize(60,60)
        btn11.move((gui_width-100+260)/2,400)

        ltext = "Roku IP Address " + s2.strip()

        lbl1 = QtGui.QLabel(ltext, self)
        lbl1.setFixedWidth(gui_width)
        lbl1.setAlignment(QtCore.Qt.AlignHCenter)  
        lbl1.move(1,575)

        self.show()

def run():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet("QPushButton{background: #7a37bb}\
                       QPushButton::hover{background: lightblue}\
                       QMainWindow{background: #33184d}\
                       QPushButton{color: white}\
                       QPushButton:flat{border: none}")
    GUI = Window()
    sys.exit(app.exec_())

run()
