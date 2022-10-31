# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QShortcut,
)
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation
from PyQt5.QtGui import QKeySequence


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.hi = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 210, 101, 81))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.move()
        )
        self.pushButton.setGeometry(QtCore.QRect(270, 380, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.hi = self.label
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hi.setText(_translate("MainWindow", "MOVE"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def move(self):
        self.animation = QPropertyAnimation(self.label, b"pos")
        x = self.label.x()
        self.animation.setDuration(500)
        self.animation.setEndValue(QPoint(x + 50, 180))
        self.animation.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    """
        def moves(self):
        print(self.path)
        lenth = len(self.path)
        temp1 = self.path[lenth - 1]
        temp2 = self.path[lenth - 2]
        temparr1 = decompress(temp1)
        temparr2 = decompress(temp2)
        i1, j1 = get_row_col(0, temparr1)  # i is row, j is column
        i2, j2 = get_row_col(0, temparr2)
        print("Here")
        if i2 > i1:
            print("No")
            # move right
            templab1 = self.label_array[i1][j1]
            templab2 = self.label_array[i2][j2]
            templab1.move(templab1.pos() + QPoint(0, 170))
            templab2.move(templab2.pos() + QPoint(0, -170))

        elif i2 < i1:
            # move left
            print("Yo")
            templab1 = self.label_array[i1][j1]
            templab2 = self.label_array[i2][j2]
            templab1.move(templab1.pos() + QPoint(0, -170))
            templab2.move(templab2.pos() + QPoint(0, 170))

        elif j2 > j1:
            templab1 = self.label_array[i1][j1]
            templab2 = self.label_array[i2][j2]
            templab1.move(templab1.pos() + QPoint(170, 0))
            templab2.move(templab2.pos() + QPoint(-170, 0))

        elif j2 < j1:
            templab1 = self.label_array[i1][j1]
            templab2 = self.label_array[i2][j2]
            templab1.move(templab1.pos() + QPoint(-170, 0))
            templab2.move(templab2.pos() + QPoint(170, 0))

        swaplab = self.label_array[i1][j1]
        self.label_array[i1][j1] = self.label_array[i2][j2]
        self.label_array[i2][j2] = swaplab
        self.path.pop()
"""
