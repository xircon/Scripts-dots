import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class SelectionWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ILCheck = False

        ILCheckbox = QCheckBox(self)
        ILCheckbox.setCheckState(Qt.Unchecked)

        ILCheckbox.stateChanged.connect(self.ILCheckbox_changed)

        MainLayout = QGridLayout()
        MainLayout.addWidget(ILCheckbox, 0, 0, 1, 1)

        #self.setLayout(MainLayout)

    def ILCheckbox_changed(self, state):
        self.ILCheck = (state == Qt.Checked)

        print(self.ILCheck)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = SelectionWindow()

  window.show()
  sys.exit(app.exec_())
