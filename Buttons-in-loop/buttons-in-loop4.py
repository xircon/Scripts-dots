#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout, QPushButton

from functools import partial

from collections import OrderedDict

import os

but_width = 300
butnum = 1

global voffset
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
         dic['1. Refresh Configuration JWM'] = 'jwm -restart'
         dic['2. Refresh Menu JWM'] = 'jwm -reload'
         dic['3. Check Error JWM'] = 'jwm -p'
         dic['4. Edit Menu JWM'] = 'medit ~/.jwm/menu'
         dic['5. Edit Tray JWM'] = 'medit ~/.jwm/tray'
         dic['6. Edit Start JWM'] = 'medit ~/.jwm/start'
         dic['7. Edit Theme JWM'] = 'medit ~/.jwm/theme'
         dic['8. Edit Keys JWM'] = 'medit ~/.jwm/keys'
         dic['9. Edit Groups JWM'] = 'medit ~/.jwm/groups'
         dic['10. Edit Preferences JWM'] = 'medit ~/.jwm/preferences'
         dic['11. Edit jwmrc'] = 'medit ~/.jwmrc'
         dic['12. Commands Manual JWM'] = 'man jwm'
         dic['13. Version JWM'] = 'jwm -v'
         dic['14. Homepage JWM'] = 'elinks http://joewing.net/projects/jwm/index.shtml'
         dic['15. Edit Conky'] = 'medit ~/.conkyrc'
         dic['16. Edit Dunst'] = 'medit ~/.config/dunst/dunstrc'
         dic['17. Edit Gmrun'] = 'medit ~/.gmrunrc'
         dic['18. Edit Bashrc'] = 'medit $HOME/.bashrc'
         dic['19. *Edit GTK2'] = 'medit $HOME/.gtkrc-2.0'
         dic['20. *Edit GTK3'] = 'medit $HOME/.config/gtk-3.0/settings.ini'
         dic['21. *Edit Xresources'] = 'medit $HOME/.Xresources'
         dic['22. *Edit LXDM'] = 'sudo medit /etc/lxdm/lxdm.conf'
         dic['23. *Edit Oblogout'] = 'sudo medit /etc/oblogout.conf'

         vbox = QVBoxLayout(self)

         global butnum
         butnum = 1


         myFont = QtGui.QFont("", 15, QtGui.QFont.Bold)
         ltxt1="JWMConf Configuration Tool - WARNING! USE WITH CAUTION!"
         len1 = len(ltxt1)
         lbl1 = QtGui.QLabel(ltxt1, self)
         lbl1.setFont(myFont)
         lbl1.setFixedWidth(gui_width)
         lbl1.setAlignment(QtCore.Qt.AlignHCenter)
         lbl1.move(0,20)
         vbox.addWidget(lbl1)

         ltxt2="ATTENTION *Numbers 19, 20, 21, 22 and 23 can break your system. WARNING! USE WITH CAUTION."
         len2 = len(ltxt2)
         lbl2 = QtGui.QLabel(ltxt2, self)
         myFont = QtGui.QFont("", 10,QtGui.QFont.Bold)
         lbl2.setFont(myFont)
         lbl2.setFixedWidth(gui_width)
         lbl2.setAlignment(QtCore.Qt.AlignHCenter)
         lbl2.move(0,655)
         vbox.addWidget(lbl2)

         ltxt3="__________________________________________________________"
         len3 = len(ltxt3)
         lbl3 = QtGui.QLabel(ltxt3, self)
         myFont = QtGui.QFont("", 20,QtGui.QFont.Bold)
         lbl3.setFont(myFont)
         lbl3.setFixedWidth(gui_width)
         lbl3.setAlignment(QtCore.Qt.AlignHCenter)
         lbl3.move(0,360)
         vbox.addWidget(lbl3)


         for key,value in dic.items():
             global voffset
             btemp = butnum
             btn = QPushButton("   " + key, self)
             btn.setStyleSheet("Text-align:left")
             btn.setFixedWidth(but_width)
             btn.clicked.connect(partial(self.doit, value))
             lm1 = pos_button()
             if btemp % 2 == 0: btemp=btemp-1
             btn.move(lm1, (btemp*20)+voffset)
             butnum += 1
             if butnum == 15:
                voffset=120
             vbox.addWidget(btn)


    def doit(self, text):
        print("%s" % text)
        os.system(text)

if __name__ == "__main__":
    app = QApplication([])
    w = Window()
    w.show()
    app.exec_()
