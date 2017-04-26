# hello_world.py
from PyQt4.QtGui import QApplication, QPushButton
app = QApplication([])
button = QPushButton("Program 9", clicked=app.quit)
button.show()
app.exec_()
