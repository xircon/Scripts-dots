# hello_world.py
from PyQt4.QtGui import QApplication, QPushButton
app = QApplication([])
button = QPushButton("Program 1", clicked=app.quit)
button.show()
app.exec_()
