from PyQt4.QtGui import *
import sys

def main():
      app = QApplication(sys.argv)

      groupBox 	 = QGroupBox("Exclusive Radio Buttons")
      vBoxLayout = QVBoxLayout()
      button1 	 =  QPushButton("Button 1")
      button2 	 =  QPushButton("Button 2")
      button3 	 =  QPushButton("Button 3")

      button1.setAutoExclusive(True)
      button2.setAutoExclusive(True)
      button3.setAutoExclusive(True)

      button1.setCheckable(True)
      button2.setCheckable(True)
      button3.setCheckable(True)

      vBoxLayout.addWidget(button1)
      vBoxLayout.addWidget(button2)
      vBoxLayout.addWidget(button3)

      groupBox.setLayout(vBoxLayout)
      groupBox.setWindowTitle("QGroupBox With Exclusive QPushButtons")
      groupBox.show()
      return app.exec_()

if __name__ == '__main__':
  main()    
