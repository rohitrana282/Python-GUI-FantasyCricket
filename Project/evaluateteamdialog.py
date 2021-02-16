# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluateteamdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(592, 447)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.combo3 = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo3.setFont(font)
        self.combo3.setObjectName("combo3")
        import sqlite3
        cricket=sqlite3.connect("cricket.db")
        cur=cricket.cursor()
        sql="SELECT Name from teams;"
        cur.execute(sql)
        while True:
            row=cur.fetchone()
            if row==None:
                break
            self.combo3.addItem(row[0])
        cricket.close()
        self.horizontalLayout_4.addWidget(self.combo3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.combo2 = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo2.setFont(font)
        self.combo2.setObjectName("combo2")
        self.combo2.addItem("Match1")
        self.combo2.addItem("Match2")
        self.combo2.addItem("Match3")
        self.combo2.addItem("Match4")
        self.combo2.addItem("Match5")
        self.horizontalLayout_5.addWidget(self.combo2)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.list1 = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.list1.setFont(font)
        self.list1.setObjectName("list1")
        self.horizontalLayout_6.addWidget(self.list1)
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.list2 = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.list2.setFont(font)
        self.list2.setStyleSheet("color: rgb(0, 170, 255);")
        self.list2.setObjectName("list2")
        self.horizontalLayout_6.addWidget(self.list2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem7 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.horizontalLayout_9.addWidget(self.pushButton)
        spacerItem8 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FantasyCricket - EvaluateTeam"))
        self.label_3.setText(_translate("Dialog", "Evaluate the Performance of your Fantasy Team"))
        self.label_4.setText(_translate("Dialog", "Team"))
        self.label.setText(_translate("Dialog", "Match"))
        self.label_5.setText(_translate("Dialog", "Players"))
        self.label_6.setText(_translate("Dialog", "Points"))
        self.label_7.setText(_translate("Dialog", "00"))
        self.pushButton.setText(_translate("Dialog", "Calculate"))

    def calculate(self):
        import sqlite3
        cricket=sqlite3.connect("cricket.db")
        cur=cricket.cursor()
        team=self.combo3.currentText()
        self.list1.clear()
        sql1="SELECT Players,Value from teams WHERE Name='"+team+"'"
        cur.execute(sql1)
        while True:
            row=cur.fetchone()
            if row==None:
                break
            selected=row[0].split(',')
            self.list1.addItems(selected)
        total=0
        self.list2.clear()
        match=self.combo2.currentText()
        count=self.list1.count()
        for i in range(count):
            name=self.list1.item(i).text()
            tt=0
            batscore=0
            bowlscore=0
            fieldscore=0

            sq="SELECT * from "+match+" WHERE Player='"+name+"';"
            cur.execute(sq)
            row=cur.fetchone()

            batscore=int(row[1]/2)
            if row[1]>50:
                batscore+=5
            if row[1]>100:
                batscore+=10
            if row[2]>0:
                sr=row[1]/row[2]*100
                if sr>=80 and sr<100:
                    batscore+=2
                if sr>=100:
                    batscore+=4
            batscore+=row[3]
            batscore+=2*row[4]

            bowlscore=row[8]*10
            if row[8]>=3:
                bowlscore+=5
            if row[8]>=5:
                bowlscore+=10
            if row[5]>0:
                er=6*row[7]/row[5]
                if er<=2:
                    bowlscore=bowlscore+10
                if er>2 and er<=3.5:
                    bowlscore=bowlscore+7
                if er>3.5 and er<=4.5:
                    bowlscore=bowlscore+4
            fieldscore=(row[9]+row[10]+row[11])*10
            tt=batscore+bowlscore+fieldscore
            self.list2.addItem(str(tt))
            total+=tt
        self.label_7.setText(str(total))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(Dialog.exec())
