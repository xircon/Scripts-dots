''' pqt_radiobutton1.py
explore the PyQT QRadioButton and QGroupBox
(dns)
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyRadioButton(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(120, 100, 300, 120)

        self.label = QLabel()

        vbox = QVBoxLayout()
        vbox.addWidget(self.createRadioButtonGroup())
        vbox.addWidget(self.label)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def createRadioButtonGroup(self):
        groupBox = QGroupBox("Radio Buttons")

        self.radio1 = QRadioButton("Radio button 1")
        self.radio1.clicked.connect(self.onRadioButton1)
        self.radio2 = QRadioButton("Radio button 2")
        self.radio2.clicked.connect(self.onRadioButton2)
        self.radio3 = QRadioButton("Radio button 3")
        self.radio3.clicked.connect(self.onRadioButton3)

        # only one RadioButton can be set at a time
        self.radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(self.radio3)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)
        return groupBox

    def onRadioButton1(self, value):
        self.label.setText('RadioButton1 clicked')
        print(value)               # True or False
        print(self.radio1.text())  # Radio button 1

    def onRadioButton2(self, value):
        self.label.setText('RadioButton2 clicked')

    def onRadioButton3(self, value):
        self.label.setText('RadioButton3 clicked')


app = QApplication([])
mrb = MyRadioButton()
mrb.show()
app.exec_()
