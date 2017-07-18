from PyQt4 import QtCore, QtGui

class Dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.groupBox = QtGui.QGroupBox(self)
        layout.addWidget(self.groupBox)
        layout = QtGui.QVBoxLayout(self.groupBox)
        global index
        index=0
        for index in range(5):
            button = QtGui.QPushButton('Button %d' % index, self.groupBox)
            layout.addWidget(button)
        self.buttonGroup = QtGui.QButtonGroup(self)
        self.buttonGroup.buttonClicked.connect(self.handleButtonClicked)
        self.updateButtonGroup()

#        self.button7callback = lambda who="7": self.anyButton(who)
#        self.connect(button7, SIGNAL("clicked()"), self.button7callback)


    def updateButtonGroup(self):
        for button in self.groupBox.findChildren(QtGui.QPushButton):
            if self.buttonGroup.id(button) < 0:
                self.buttonGroup.addButton(button)

    def handleButtonClicked(self, button):
        for item in self.buttonGroup.buttons():
            if button is item:
                item.setStyleSheet('background-color: orange')
                print(index)
            else:
                item.setStyleSheet('')

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Dialog()
    window.show()
    sys.exit(app.exec_())
