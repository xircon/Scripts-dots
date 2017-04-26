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

    def bttncmnds():
        global btncmnds
        btncmnds = ["jwm -restart", "jwm -reload", "jwm -p", "medit ~/.jwm/menu", "medit ~/.jwm/tray", "medit ~/.jwm/start", "medit ~/.jwm/theme", "medit ~/.jwm/keys", "medit ~/.jwm/groups", "medit ~/.jwm/preferences", "medit ~/.jwmrc", "man jwm", "jwm -v", "elinks http://joewing.net/projects/jwm/index.shtml", "medit ~/.conkyrc", "medit ~/.config/dunst/dunstrc", "medit ~/.gmrunrc", "medit $HOME/.bashrc", "medit $HOME/.gtkrc-2.0", "medit $HOME/.config/gtk-3.0/settings.ini", "medit $HOME/.Xresources", "sudo medit /etc/lxdm/lxdm.conf", "sudo medit /etc/oblogout.conf"]

    bttncmnds()


    def handleBtn1(self):
        print("Button1")
        #os.system("metacity --no-composite --replace &")

    def handleBtn2(self):

        print("Button2")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn3(self):

        print("Button3")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn4(self):

        print("Button4")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn5(self):

        print("button5")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn6(self):

        print("button6")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn7(self):

        print("button7")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn7(self):

        print("button7")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn8(self):

        print("button8")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn9(self):

        print("button9")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn10(self):

        print("button10")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn11(self):

        print("button11")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn12(self):

        print("button12")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn13(self):

        print("button13")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn14(self):

        print("button14")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn14(self):

        print("button14")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn15(self):

        print("button15")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn16(self):

        print("button16")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn16(self):

        print("button16")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn17(self):

        print("button17")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn18(self):

        print("button18")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn19(self):

        print("button19")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn20(self):

        print("button20")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn21(self):

        print("button21")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn22(self):

        print("button22")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")

    def handleBtn23(self):

        print("button23")
        #os.system("killall compton")
        #os.system("metacity --no-composite --replace &")



    def home(self):

        def bttnlables():
            global btnlabs
            btnlabs = ["Refresh Configuration JWM","Refresh Menu JWM","Check Error JWM","Edit Menu JWM","  Edit Tray JWM", "Edit Start JWM", "Edit Theme JWM", "Edit Keys JWM", "Edit Groups JWM", "Edit Preferences JWM", "Edit jwmrc", "Commands Manual JWM", "Version JWM", "Homepage JWM", "Edit Conky", "Edit Dunst", "Edit Gmrun", "Edit Bashrc", "*Edit GTK2", "*Edit GTK3", "*Edit Xresources", "*Edit LXDM", "*Edit Oblogout"]

        bttnlables()

        def pos_button():
            #print("but_num"+str(btnnum))
            #print("even", btnnum % 2)
            if btnnum % 2 > 0:
                lm1=20
            else:
                lm1=420
            return lm1;

        myFont = QtGui.QFont()
        myFont.setBold(True)

        ltxt1="\nJWMConf Configuration Tool" + "\n" + "WARNING! USE WITH CAUTION!"
        len1 = len(ltxt1)
        lbl1 = QtGui.QLabel(ltxt1, self)
        lbl1.setFont(myFont)
        #lbl1.move(150-len1,00)
        lbl1.setFixedWidth(gui_width)
        lbl1.setAlignment(QtCore.Qt.AlignHCenter)

        ltxt2="\nWARNING! USE WITH CAUTION!"
        len2 = len(ltxt2)
        lbl2 = QtGui.QLabel(ltxt2, self)
        lbl2.setFont(myFont)
        lbl2.move(00,20)
        lbl2.setFixedWidth(gui_width)
        lbl2.setAlignment(QtCore.Qt.AlignHCenter)

        global btnnum

        btnnum=1
        btn1 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn1.clicked.connect(lambda: self.handleBtn1(1))
        btn1.setFixedWidth(bw1)
        #btn1.resize(100,100)
        lm1=pos_button()
        btn1.move(lm1,(btnnum*20)+voffset)

        btnnum=2
        btemp=btnnum
        btn2 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn2.clicked.connect(lambda: self.handleBtn1(2))
        btn2.setFixedWidth(bw1)
        lm1=pos_button()
        print(lm1)
        print(btnnum)
        if btemp % 2 == 0: btemp=btemp-1
        btn2.move(lm1,(btemp*20)+voffset)
        print("btemp ",btemp, "btnnum", btnnum)

        btnnum=3
        btn3 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn1.clicked.connect(lambda: self.handleBtn1(3))
        btn3.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn3.move(lm1,(btnnum*20)+voffset)

        btnnum=4
        btn4 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn4.clicked.connect(self.handleBtn4)
        btn4.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn4.move(lm1,(btnnum*20)+voffset)

        btnnum=5
        btn5 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn5.clicked.connect(self.handleBtn5)
        btn5.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn5.move(lm1,(btnnum*20)+voffset)

        btnnum=6
        btn6 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn6.clicked.connect(self.handleBtn6)
        btn6.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn6.move(lm1,(btnnum*20)+voffset)

        btnnum=7
        btn7 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn7.clicked.connect(self.handleBtn7)
        btn7.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn7.move(lm1,(btnnum*20)+voffset)

        btnnum=8
        btn8 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn8.clicked.connect(self.handleBtn8)
        btn8.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn8.move(lm1,(btnnum*20)+voffset)

        btnnum=9
        btn9 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn9.clicked.connect(self.handleBtn9)
        btn9.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn9.move(lm1,(btnnum*20)+voffset)

        btnnum=10
        btn10 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn10.clicked.connect(self.handleBtn10)
        btn10.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn10.move(lm1,(btnnum*20)+voffset)

        btnnum=11
        btn11 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn11.clicked.connect(self.handleBtn11)
        btn11.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn11.move(lm1,(btnnum*20)+voffset)

        btnnum=12
        btn12 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn12.clicked.connect(self.handleBtn12)
        btn12.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn12.move(lm1,(btnnum*20)+voffset)

        btnnum=13
        btn13 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn13.clicked.connect(self.handleBtn13)
        btn13.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn13.move(lm1,(btnnum*20)+voffset)

        btnnum=14
        btn14 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn14.clicked.connect(self.handleBtn14)
        btn14.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn14.move(lm1,(btnnum*20)+voffset)

        btnnum=15
        btn15 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn15.clicked.connect(self.handleBtn15)
        btn15.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn15.move(lm1,(btnnum*20)+voffset)

        btnnum=16
        btn16 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn16.clicked.connect(self.handleBtn16)
        btn16.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn16.move(lm1,(btnnum*20)+voffset)

        btnnum=17
        btn17 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn17.clicked.connect(self.handleBtn17)
        btn17.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn17.move(lm1,(btnnum*20)+voffset)

        btnnum=18
        btn18 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn18.clicked.connect(self.handleBtn18)
        btn18.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn18.move(lm1,(btnnum*20)+voffset)

        btnnum=19
        btn19 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn19.clicked.connect(self.handleBtn19)
        btn19.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn19.move(lm1,(btnnum*20)+voffset)

        btnnum=20
        btn20 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn20.clicked.connect(self.handleBtn20)
        btn20.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn20.move(lm1,(btnnum*20)+voffset)

        btnnum=21
        btn21 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn21.clicked.connect(self.handleBtn21)
        btn21.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn21.move(lm1,(btnnum*20)+voffset)

        btnnum=22
        btn22 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn22.clicked.connect(self.handleBtn22)
        btn22.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn22.move(lm1,(btnnum*20)+voffset)

        btnnum=23
        btn23 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn23.clicked.connect(self.handleBtn23)
        btn23.setFixedWidth(bw1)
        lm1=pos_button()
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn23.move(lm1,(btnnum*20)+voffset)
        #btnnum=1
        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
