# hello_world.py
from PyQt4.QtGui import QApplication, QPushButton
app = QApplication([])
button = QPushButton("Program 7", clicked=app.quit)
button.show()
app.exec_()
