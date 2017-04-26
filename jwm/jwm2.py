import sys
import os
from PyQt4 import QtGui, QtCore

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

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, gui_width, gui_height)
        self.setWindowTitle("JWMConf-GUI")
        self.setWindowIcon(QtGui.QIcon('manjaro.png'))
        self.home()

    def home(self):

        def bttnlables():
            global btnlabs
            btnlabs = ["Refresh Configuration JWM","Refresh Menu JWM","Check Error JWM","Edit Menu JWM","  Edit Tray JWM", "Edit Start JWM", "Edit Theme JWM", "Edit Keys JWM", "Edit Groups JWM", "Edit Preferences JWM", "Edit jwmrc", "Commands Manual JWM", "Version JWM", "Homepage JWM", "Edit Conky", "Edit Dunst", "Edit Gmrun", "Edit Bashrc", "*Edit GTK2", "*Edit GTK3", "*Edit Xresources", "*Edit LXDM", "*Edit Oblogout"]

        bttnlables()

        def pos_button():
            if btnnum % 2 > 0:
                lm1=20
            else:
                lm1=420
            return lm1;

        myFont = QtGui.QFont()
        myFont.setBold(True)

        ltxt1="\nThis is a test label"
        len1 = len(ltxt1)
        lbl1 = QtGui.QLabel(ltxt1, self)
        lbl1.setFont(myFont)
        lbl1.setFixedWidth(gui_width)
        lbl1.setAlignment(QtCore.Qt.AlignHCenter)

        btnnum=1
        btn1 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn1.clicked.connect(lambda: self.on_button(1))
        btn1.setFixedWidth(bw1)
        lm1=pos_button()
        btn1.move(lm1,(btnnum*20)+voffset)

        self.show()

    def on_button(self, n):
        button_cmds = ["filler", "gmrun", "medit"]
        #print('Button {0} clicked'.format(n))
        #print(n)
        os.system(button_cmds[n])

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
