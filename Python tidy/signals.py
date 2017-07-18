import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        
        button = QPushButton(self.tr("Click me"))
        self.resultLabel = QLabel(self.tr("..."))
        
        # New style: uses the connect method of a pyqtSignal object.
        self.connect(button, SIGNAL("clicked()"), self.handleClick)
        
        # Old style: uses the SIGNAL function to describe the signal.
        self.connect(self, SIGNAL("sendValue(PyQt_PyObject)"), self.handleValue)
        
        layout = QVBoxLayout(self)
        layout.addWidget(button)
        layout.addWidget(self.resultLabel)
    
    def handleClick(self):
    
        # Old style: emits the signal using the SIGNAL function.
        self.emit(SIGNAL("sendValue(PyQt_PyObject)"), 1 )
    
    def handleValue(self, value):
    
        self.resultLabel.setText(repr(value))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
