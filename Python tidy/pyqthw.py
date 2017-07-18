import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel

# Main Function
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)
    # Create a label and set its properties
    appLabel = QLabel()
    appLabel.setText("Hello, World!!!\n Traditional first app using PyQt5")
    appLabel.setAlignment(Qt.AlignCenter)
    appLabel.setGeometry(300, 300, 250, 175)

    # Show the Label
    appLabel.show()

    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()

