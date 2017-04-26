from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os

global a
a=99

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        button_labels = ["Refresh Configuration JWM","Refresh Menu JWM","Check Error JWM","Edit Menu JWM","  Edit Tray JWM", "Edit Start JWM", "Edit Theme JWM", "Edit Keys JWM", "Edit Groups JWM", "Edit Preferences JWM", "Edit jwmrc", "Commands Manual JWM", "Version JWM", "Homepage JWM", "Edit Conky", "Edit Dunst", "Edit Gmrun", "Edit Bashrc", "*Edit GTK2", "*Edit GTK3", "*Edit Xresources", "*Edit LXDM", "*Edit Oblogout"]

        layout = QVBoxLayout()

        global a,x
        a=0
        x=0

        a=0
        button1 = QPushButton(button_labels[a])
        button1.clicked.connect(lambda: self.on_button(1))

        a+=1
        button2 = QPushButton(button_labels[a])
        #button2.clicked.connect(lambda: self.on_button(2))
        button2.clicked.connect(lambda state, x=2: self.on_button(x))


        a+=1
        button3 = QPushButton(button_labels[a])
        button3.clicked.connect(lambda: self.on_button(3))

        a+=1
        button4 = QPushButton(button_labels[a])
        button4.clicked.connect(lambda: self.on_button(4))

        a+=1
        button5 = QPushButton(button_labels[a])
        button5.clicked.connect(lambda: self.on_button(5))

        a+=1
        button6 = QPushButton(button_labels[a])
        button6.clicked.connect(lambda: self.on_button(6))

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)


        main_frame = QWidget()
        main_frame.setLayout(layout)

        self.setCentralWidget(main_frame)

    def on_button(self, n):
#        btncmnds = ["medit", "gmrun", "jwm -reload", "jwm -p", "medit ~/.jwm/menu", "medit ~/.jwm/tray", "medit ~/.jwm/start", "medit ~/.jwm/theme", "medit ~/.jwm/keys", "medit ~/.jwm/groups", "medit ~/.jwm/preferences", "medit ~/.jwmrc", "man jwm", "jwm -v", "elinks http://joewing.net/projects/jwm/index.shtml", "medit ~/.conkyrc", "medit ~/.config/dunst/dunstrc", "medit ~/.gmrunrc", "medit $HOME/.bashrc", "medit $HOME/.gtkrc-2.0", "medit $HOME/.config/gtk-3.0/settings.ini", "medit $HOME/.Xresources", "sudo medit /etc/lxdm/lxdm.conf", "sudo medit /etc/oblogout.conf"]
        btncmnds = ["python ~/scripts/TestProgs/p1.py", "gmrun", "jwm -reload", "jwm -p", "medit ~/.jwm/menu", "medit ~/.jwm/tray", "medit ~/.jwm/start", "medit ~/.jwm/theme", "medit ~/.jwm/keys", "medit ~/.jwm/groups", "medit ~/.jwm/preferences", "medit ~/.jwmrc", "man jwm", "jwm -v", "elinks http://joewing.net/projects/jwm/index.shtml", "medit ~/.conkyrc", "medit ~/.config/dunst/dunstrc", "medit ~/.gmrunrc", "medit $HOME/.bashrc", "medit $HOME/.gtkrc-2.0", "medit $HOME/.config/gtk-3.0/settings.ini", "medit $HOME/.Xresources", "sudo medit /etc/lxdm/lxdm.conf", "sudo medit /etc/oblogout.conf"]

        #print("x= ", x, a)

        os.system(btncmnds[n])

        print(' Button {0} clicked'.format(n))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    app.exec_()
