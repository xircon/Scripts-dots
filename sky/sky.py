#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import QApplication, QPushButton

from functools import partial

from collections import OrderedDict

import os

import sys

# needs to be installed with pip???
import configparser

Config = configparser.ConfigParser()
Config.read("/home/steve/scripts/shutdown.conf")  # why doesn't ~/ work?
# Config.read("/home/steve/Documents/Python/shutdown.conf")

# Gui and button variables.
but_width = 200
voffset = 20
gui_width = 460
gui_height = 300
butnum = 1

# Which DESKTOP SESSION
dtop = os.environ['DESKTOP_SESSION']
if dtop == "/usr/share/xsessions/plasma":
   dtop = "plasma"

fpath = os.getcwd
print(fpath)

# Which Init System.
with open("/proc/1/comm", "r") as f:
    init_sys = f.read().strip()

if init_sys != "systemd":
    init_sys = "openrc"


# init_sys="openrc" #debug

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, gui_width, gui_height)
        self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowTitle(dtop.title() + " Session Manager")
        # enable custom window hint
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        # disable (but not hide) close button
        # self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        def pos_button() -> object:  # Left Margin of odd and even buttons.
            if butnum % 2 > 0:
                lm1 = 20
            else:
                lm1 = 240
            return lm1;

        dict1 = {}

        print(Config.sections())  # debug

        # Fill dic from dict1, so the loop can access in correct order.....
        # Cannot see a way to do this from dict1 immediately
        dic = OrderedDict()
        dic['Lock Screen'] = Config[dtop]['Lock']
        dic['Suspend'] = Config[init_sys]['Suspend']
        dic['Logout'] = Config[dtop]['Logout']
        dic['Restart'] = Config[init_sys]['Restart']
        dic['Shutdown'] = Config[init_sys]['Shutdown']
        dic['Edit Config'] = "xdg-open /home/steve/scripts/shutdown.conf"
        dic['Quit'] = ' '

        for key, value in dic.items():  # debug
            print("List Dic ", key, dic[key])

        Layout = Config['layout']['columns']
        print(Layout)

        # if Layout == "2":

        butnum = 1

        myFont = QtGui.QFont("", 11, QtGui.QFont.Bold)
        ltxt1 = "What do you want to do?\n"
        len1 = len(ltxt1)
        lbl1 = QtGui.QLabel(ltxt1, self)
        lbl1.setFont(myFont)
        lbl1.setFixedWidth(gui_width)
        lbl1.setAlignment(QtCore.Qt.AlignHCenter)
        lbl1.setStyleSheet('color: white')
        lbl1.move(0, 20)

        # Set colors per configuation file.
        # Main Window background colour
        color_b = Config['layout']['Main_background']

        # QPushButton - background-color
        button_b = Config['layout']['button_back']

        # QPushButton - Hover
        button_h = Config['layout']['button_hover']

        # QPushButton text color
        button_t = Config['layout']['button_text']

        style1 = "QMainWindow{background-color: %s; }" % color_b

        style2 = "QPushButton{background-color: %s; }" % button_b

        style3 = "QPushButton::hover{color: %s; }" % button_h

        style4 = "QPushButton{color: %s; }" % button_t

        self.setStyleSheet(style1 + style2 + style3 + style4)

        for key, value in dic.items():
            # global voffset
            btemp = butnum
            btn = QPushButton("   " + key, self)
            btn.setStyleSheet("Text-align:left")
            btn.setFixedWidth(but_width)
            btn.setFocusPolicy(QtCore.Qt.ClickFocus)
            btn.clicked.connect(partial(self.doit, value))
            if Layout == "2":
                # Double column of buttons.......
                lm1 = pos_button()
                if btemp % 2 == 0: btemp = btemp - 1
                btn.move(lm1, (btemp * 30) + voffset)
            else:
                # Single column of buttons.......
                new_width = but_width + 40
                new_height = 450
                self.setGeometry(50, 50, new_width, new_height)
                self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())
                lbl1.setAlignment(QtCore.Qt.AlignLeft)
                lbl1.setFixedWidth(new_width)
                lbl1.setAlignment(QtCore.Qt.AlignCenter)
                btn.move(20, (btemp * 50) + voffset)

            butnum += 1

    def doit(self, text):
        print(text)  # debug
        os.system(text)
        exit()


if __name__ == "__main__":
    app = QApplication([])
    w = Window()
    w.show()
    app.exec_()
    exit()
