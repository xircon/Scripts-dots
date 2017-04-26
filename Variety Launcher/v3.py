from PyQt4.QtGui import * #Qicon, QPushButton, QVBoxLayout, QMainWindow, QApplication, QWidget
from PyQt4 import QtGui, QtCore

import os

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)

        button_labels = [" Next ", " Previous ", " Delete ", " View ", " Pause ", " History ", " Downloads "]

        layout = QVBoxLayout()

        a=0
        button1 = QPushButton(button_labels[a])
        button1.setIcon(QtGui.QIcon('/usr/share/icons/Paper/16x16/actions/next.png'))
        button1.setIconSize(QtCore.QSize(24,24))
        button1.setStyleSheet("Text-align:left")
        button1.clicked.connect(lambda: self.on_button(1))

        a+=1
        button2 = QPushButton(button_labels[a])
        button2.setIcon(QtGui.QIcon('/usr/share/icons/Paper/16x16/actions/previous.png'))
        button2.setIconSize(QtCore.QSize(24,24))
        button2.clicked.connect(lambda: self.on_button(2))

        a+=1
        button3 = QPushButton(button_labels[a])
        button3.setIcon(QtGui.QIcon('/usr/share/icons/Paper/24x24/actions/process-stop.png'))
        button3.setIconSize(QtCore.QSize(24,24))
        button3.clicked.connect(lambda: self.on_button(3))

        a+=1
        button4 = QPushButton(button_labels[a])
        button4.setIcon(QtGui.QIcon('/usr/share/icons/Paper/24x24/apps/gpicview.png'))
        button4.setIconSize(QtCore.QSize(24,24))
        button4.clicked.connect(lambda: self.on_button(4))

        a+=1
        button5 = QPushButton(button_labels[a])
        #/usr/share/icons/hicolor/24x24/apps/simplescreenrecorder-paused.png
        button5.setIcon(QtGui.QIcon('/usr/share/icons/gnome/24x24/actions/stock_media-pause.png'))
        button5.setIconSize(QtCore.QSize(24,24))
        button5.clicked.connect(lambda: self.on_button(5))

        a+=1
        button6 = QPushButton(button_labels[a])
        button6.clicked.connect(lambda: self.on_button(6))
        print(a)

        a+=1
        button7 = QPushButton(button_labels[a])
        button7.clicked.connect(lambda: self.on_button(7))

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(button7)

        main_frame = QWidget()
        main_frame.setLayout(layout)

        self.setCentralWidget(main_frame)

    def on_button(self, n):
        run_cmd = ["filler", "variety -n", "variety -p", "variety -t", "xdg-open `cat ~/currentwp`", "variety --pause", "variety --history", "variety --downloads"]

        print("N= ", run_cmd[n],  n)

        os.system(run_cmd[n])

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    app.exec_()
