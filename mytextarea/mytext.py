#!/usr/bin/env python
 
from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import design  # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods

from sh import inxi 


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setFamily('Cousine') 
        self.textEdit.setFont(font)
        self.Butt1.clicked.connect(self.butt1Func)  
        self.Butt2.clicked.connect(self.butt2Func)  
        self.Butt3.clicked.connect(self.butt3Func)  
        self.Butt4.clicked.connect(self.butt4Func)  
        self.Butt5.clicked.connect(self.butt5Func)  
        self.Butt6.clicked.connect(self.butt6Func)  
        self.Butt7.clicked.connect(self.butt7Func)  
        self.Butt8.clicked.connect(self.butt8Func)  
        self.Butt9.clicked.connect(self.butt9Func)  
        self.Butt10.clicked.connect(self.butt10Func)  
        self.Butt11.clicked.connect(self.butt11Func)  
        self.Butt12.clicked.connect(self.butt12Func)  
   

    def butt1Func(self):
        self.textEdit.clear() # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if directory: # if user didn't pick a directory don't continue
            for file_name in os.listdir(directory): # for all files, if any, in the directory
                self.textEdit.append(file_name)  # add file to the listWidget

    def butt2Func(self):
        self.Butt2.setText("Clicked")
        self.textEdit.append(str(inxi('-Fxzc0')))
        print("filler2")

    def butt3Func(self):
        print("filler3")

    def butt4Func(self):
        print("filler4")

    def butt5Func(self):
        print("filler5")

    def butt6Func(self):
        print("filler6")

    def butt7Func(self):
        print("filler7")

    def butt8Func(self):
        print("filler8")

    def butt9Func(self):
        print("filler9")

    def butt10Func(self):
        print("filler10")

    def butt11Func(self):
        print("filler11")

    def butt12Func(self):
        exit()


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function