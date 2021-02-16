# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openteamdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(342, 195)
        Dialog.setMinimumSize(QtCore.QSize(342, 195))
        Dialog.setMaximumSize(QtCore.QSize(342, 195))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.combo1 = QtWidgets.QComboBox(Dialog)
        self.combo1.setGeometry(QtCore.QRect(140, 50, 151, 22))
        self.combo1.setObjectName("combo1")
        import sqlite3
        cricket=sqlite3.connect("cricket.db")
        cur=cricket.cursor()
        sql="SELECT Name from teams;"
        cur.execute(sql)
        while True:
            rec=cur.fetchone()
            if rec==None:
                break
            self.combo1.addItem(rec[0])
        self.b1 = QtWidgets.QPushButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(110, 110, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(Dialog.reject)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FantasyCricket - OpenTeam"))
        self.label.setText(_translate("Dialog", "Select Team"))
        self.b1.setText(_translate("Dialog", "Open Team"))

   
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(Dialog.exec())
