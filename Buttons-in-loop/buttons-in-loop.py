import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
layout = QtGui.QGridLayout()

buttons = {}

button_labels = ["Next", "Previous", "Delete", "View", "Pause", "History", "Downloads"]

for i in range(7):
    #for j in range(10):
        # keep a reference to the buttons
        buttons[(i, 10)] = QtGui.QPushButton(button_labels[i])
        # add to the layout
        layout.addWidget(buttons[(i, 10)], i, 10)
        print(buttons)


widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())
