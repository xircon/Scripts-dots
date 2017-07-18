#! /usr/bin/env python
'''
###########################################################
##   A Demo Application showing the use of sqlite3     ##
##   and the QSqlTableModel    Class                    ##
##   written by rowinggolfer 24th Feb 2010              ##
##   version 0.1 and NOT YET WORKING!!                  ##
##   this work is in the public domain,                 ##
##   do with it as you please                           ##
###########################################################
'''
import os, sys
from PyQt4 import QtCore, QtGui, QtSql

def makeDB():
    import sqlite3
    db = sqlite3.connect("test.db")
    db.execute("create table if not exists table1 (value text, data text)")

    query = "insert into table1 (value, data) values (?, ?)"

    valueSet = (("day","today"),("time","noon"),("food","cheese"))
    for values in valueSet:
        db.execute(query, values)
    db.commit()

class TestApp(QtGui.QDialog):
    def __init__(self, model, parent = None):
        super(TestApp, self).__init__(parent)
        self.model = model

        table = QtGui.QTableView()
        table.setModel(self.model)

        button = QtGui.QPushButton("Add a row")
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(table)
        layout.addWidget(button)

        self.connect(button, QtCore.SIGNAL("clicked()"), self.addRow)

    def addRow(self):
        self.model.insertRows(self.model.rowCount(), 1)

class myModel(QtSql.QSqlTableModel):
    def __init__(self, parent = None):
        super(myModel, self).__init__(parent)
        self.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)

        self.setTable("table1")
        self.select()

if __name__ == "__main__":
    if not os.path.exists("test.db"):
        makeDB()

    myDb = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    myDb.setDatabaseName("test.db")
    if not myDb.open():
        print("Unable to create connection!")
        print("have you installed the sqlite driver?")
        print("sudo apt-get install libqt4-sql-sqlite")
        sys.exit(1)
    model = myModel()

    app = QtGui.QApplication(sys.argv)
    dl = TestApp(model)
    dl.exec_()
