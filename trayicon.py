#from http://stackoverflow.com/questions/893984/pyqt-show-menu-in-a-system-tray-application
import sys
import os
from PyQt4 import QtGui, QtCore

class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
       QtGui.QSystemTrayIcon.__init__(self, icon, parent)
       menu = QtGui.QMenu(parent)
       runAction = menu.addAction("File Manager")
       exitAction = menu.addAction("Exit")
       self.setContextMenu(menu)
       QtCore.QObject.connect(runAction,QtCore.SIGNAL('triggered()'), self.runner)
       QtCore.QObject.connect(exitAction,QtCore.SIGNAL('triggered()'), self.exit)

    def exit(self):
      QtCore.QCoreApplication.exit()
      exit()

    def runner(self):
      os.system("pcmanfm &")

def main():
   app = QtGui.QApplication(sys.argv)

   w = QtGui.QWidget()
   trayIcon = SystemTrayIcon(QtGui.QIcon("/usr/share/icons/hicolor/16x16/apps/manjaro.png"), w)

   trayIcon.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
    main()
