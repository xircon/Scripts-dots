#!/usr/bin/env python
import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

CONFIG_DATABASE_PATH = "./"
CONFIG_DATABASE_NAME = "comboboxexample.db"

class EditItemDlg(QDialog):
    def __init__(self, parent=None):
        super(EditItemDlg, self).__init__(parent)
        self.setWindowTitle("Edit Phone Number")

        # Create model
        self.model = QSqlTableModel(self)
        self.model.setTable("phone_number_type")
        self.model.select()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                     QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)

        self.phoneEdit = QLineEdit()
        phoneLabel = QLabel("&Phone Number:")
        phoneLabel.setBuddy(self.phoneEdit)

        # Create combo and set its model
        self.typeComboBox = QComboBox()
        self.typeComboBox.setModel(self.model)
        self.typeComboBox.setModelColumn(
                          self.model.fieldIndex("label"))
        typeLabel = QLabel("&Type:")
        typeLabel.setBuddy(self.typeComboBox)

        controlLayout = QGridLayout()
        controlLayout.addWidget(phoneLabel, 0, 0)
        controlLayout.addWidget(self.phoneEdit, 0, 1)
        controlLayout.addWidget(typeLabel, 0, 2)
        controlLayout.addWidget(self.typeComboBox, 0, 3)
        controlLayout.addWidget(buttonBox, 1, 0, 1, 4,
                                Qt.AlignRight)

        self.setLayout(controlLayout)
        self.resize(500, 125)

        self.connect(buttonBox, SIGNAL("accepted()"),
                     self, SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"),
                     self, SLOT("reject()"))

def main():
    app = QApplication(sys.argv)

    filename = os.path.join(CONFIG_DATABASE_PATH,
                            CONFIG_DATABASE_NAME)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "Combo Box Example",
            QString("Database Error: %1").arg(db.lastError().text()))
        sys.exit(1)

    # Would normally be invoked as modal dialog.
    # But for simplicity we use it as the main form here.
    form = EditItemDlg()
    form.show()
    app.exec_()
    del form
    del db


if __name__ == '__main__':
    main()
