import sys
from PySide.QtCore import *
from PySide.QtGui import *
 
class ExampleApp(QDialog):
    ''' An example application for PyQt. Instantiate
        and call the run method to run. '''
    def __init__(self):
        # create a Qt application --- every PyQt app needs one
        self.qt_app = QApplication(sys.argv)
 
        # The available greetings
        self.greetings = ['hello', 'goodbye', 'heyo']
 
        # Call the parent constructor on the current object
        QDialog.__init__(self, None)
 
        # Set up the window
        self.setWindowTitle('PyQt Example')
        self.setMinimumSize(300, 200)
 
        # Add a vertical layout
        self.vbox = QVBoxLayout()
 
        # The greeting combo box
        self.greeting = QComboBox(self)
        # Add the greetings
        list(map(self.greeting.addItem, self.greetings))
 
        # The recipient textbox
        self.recipient = QLineEdit('world', self)
 
        # The Go button
        self.go_button = QPushButton('&Go')
        # Connect the Go button to its callback
        self.go_button.clicked.connect(self.print_out)
 
        # Add the controls to the vertical layout
        self.vbox.addWidget(self.greeting)
        self.vbox.addWidget(self.recipient)
        # A very stretchy spacer to force the button to the bottom
        self.vbox.addStretch(100)
        self.vbox.addWidget(self.go_button)
 
        # Use the vertical layout for the current window
        self.setLayout(self.vbox)
 
    def print_out(self):
        ''' Print a greeting constructed from
            the selections made by the user. '''
        print('%s, %s!' % (self.greetings[self.greeting.currentIndex()].title(),
                           self.recipient.displayText()))
 
    def run(self):
        ''' Run the app and show the main form. '''
        self.show()
        self.qt_app.exec_()
 
app = ExampleApp()
app.run()
