import sys
from PyQt4 import QtGui, QtCore

from time import strftime


class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)

        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.display(strftime("%H"+":"+"%M"))

        self.setCentralWidget(self.lcd)

#---------Window settings --------------------------------

        self.setGeometry(300,300,250,100)
        self.setWindowTitle("Clock")

#-------- Slots ------------------------------------------

    def Time(self):
        self.lcd.display(strftime("%H"+":"+"%M"))

def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
