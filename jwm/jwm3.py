import sys
import os
from PyQt4 import QtGui, QtCore

#Button Width/Height
bw1 = 100
bh = 50
#gui dimensions
gui_width=400
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


    def home(self):

        def bttnlables():
            global btnlabs
            btnlabs = ["","","","","", "Back", "Home", "Rewind", "Play/Pause", "FastF", "Filler"]

        bttnlables()

        #QFont = serifFont("", 40, QFont.Bold);
        myFont = QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(10)
        ltxt1="\nRoku Remote"
        len1 = len(ltxt1)
        lbl1 = QtGui.QLabel(ltxt1, self)
        lbl1.setFont(myFont)
        #lbl1.move(150-len1,00)
        lbl1.setFixedWidth(gui_width)
        lbl1.setAlignment(QtCore.Qt.AlignHCenter)

        global btnnum

        #QWidget.QPushButton.setStyleSheet("font-size:40px;background-color:#333333;\
        #    border: 2px solid #222222")

        btnnum=1
        btn1 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn1.clicked.connect(self.handleBtn1)
        btn1.setIcon(QtGui.QIcon('/usr/share/icons/oxygen/base/48x48/actions/arrow-up.png'))
        btn1.resize(100,100)
        btn1.move((gui_width-100)/2,90)

        btnnum=2
        btemp=btnnum
        btn2 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn2.clicked.connect(self.handleBtn2)
        btn2.setIcon(QtGui.QIcon('/usr/share/icons/oxygen/base/48x48/actions/arrow-left.png'))
        btn2.resize(100,100)
        btn2.move(50,190)

        btnnum=3
        btn3 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn3.clicked.connect(self.handleBtn3)
        btn3.setIcon(QtGui.QIcon('/usr/share/icons/oxygen/base/48x48/actions/arrow-right.png'))
        btn3.resize(100,100)
        btn3.move(250,190)

        btnnum=4
        btn4 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn4.clicked.connect(self.handleBtn4)
        btn4.setIcon(QtGui.QIcon('/usr/share/icons/oxygen/base/48x48/actions/arrow-down.png'))
        btn4.resize(100,100)
        btn4.move((gui_width-100)/2,290)

        btnnum=5
        btn5 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn5.clicked.connect(self.handleBtn5)
        btn5.setIcon(QtGui.QIcon('/usr/share/icons/oxygen/base/48x48/actions/media-record.png'))
        btn5.resize(100,100)
        btn5.move(150,190)

        btnnum=6
        btn6 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn6.clicked.connect(self.handleBtn6)
        btn6.setFixedWidth(bw1)
        btn6.setFixedHeight(bh)
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn6.move((gui_width-100)/2,400)

        btnnum=7
        btn7 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn7.clicked.connect(self.handleBtn7)
        btn7.setFixedWidth(bw1)
        btn7.setFixedHeight(bh)
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn7.move(lm1,(btnnum*20)+voffset)

        btnnum=8
        btn8 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn8.clicked.connect(self.handleBtn8)
        btn8.setFixedWidth(bw1)
        btn8.setFixedHeight(bh)
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn8.move(lm1,(btnnum*20)+voffset)

        btnnum=9
        btn9 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn9.clicked.connect(self.handleBtn9)
        btn9.setFixedWidth(bw1)
        btn9.setFixedHeight(bh)
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn9.move(lm1,(btnnum*20)+voffset)

        btnnum=10
        btn10 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn10.clicked.connect(self.handleBtn10)
        btn10.setFixedWidth(bw1)
        btn10.setFixedHeight(bh)
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn10.move(lm1,(btnnum*20)+voffset)

        btnnum=11
        btn11 = QtGui.QPushButton(btnlabs[btnnum-1], self)
        btn11.clicked.connect(self.handleBtn11)
        btn11.setFixedWidth(bw1)
        btn11.setFixedHeight(bh)
        if btnnum % 2 == 0: btnnum=btnnum-1
        btn11.move(lm1,(btnnum*20)+voffset)

        self.show()


def run():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet("QPushButton{background: lightblue} QPushButton::hover{background: lightgreen}\
                        QMainWindow{background: blue}")
    GUI = Window()
    sys.exit(app.exec_())

run()
