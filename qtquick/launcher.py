#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtQuick import QQuickView
       
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
  
    view = QQuickView()
    view.setSource(QUrl('basic.qml'))
    view.show()

    sys.exit(app.exec_())