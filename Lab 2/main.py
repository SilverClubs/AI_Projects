from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QPoint, QEasingCurve, pyqtSignal, QPropertyAnimation
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys

class Label(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QLabel.__init__(self, parent=parent)

    def mousePressEvent(self, event):
        self.clicked.emit()


class Ui_ConnectFour(object):
    def setupUi(self, ConnectFour):
        ConnectFour.setObjectName("ConnectFour")
        ConnectFour.resize(1254, 1058)
        self.centralwidget = QtWidgets.QWidget(ConnectFour)

        self.centralwidget.setObjectName("centralwidget")
        self.board = QtWidgets.QLabel(self.centralwidget)
        self.board.setGeometry(QtCore.QRect(10, 130, 910, 781))
        self.board.setText("")
        self.board.setPixmap(QtGui.QPixmap("connect-4-plate-6.png"))
        self.board.setObjectName("board")
        self.r11 = QtWidgets.QLabel(self.centralwidget)
        self.r11.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.r11.setText("")
        self.r11.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r11.setObjectName("r11")
        self.r12 = QtWidgets.QLabel(self.centralwidget)
        self.r12.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.r12.setText("")
        self.r12.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r12.setObjectName("r12")
        self.r13 = QtWidgets.QLabel(self.centralwidget)
        self.r13.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.r13.setText("")
        self.r13.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r13.setObjectName("r13")
        self.r14 = QtWidgets.QLabel(self.centralwidget)
        self.r14.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.r14.setText("")
        self.r14.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r14.setObjectName("r14")
        self.r15 = QtWidgets.QLabel(self.centralwidget)
        self.r15.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.r15.setText("")
        self.r15.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r15.setObjectName("r15")
        self.r16 = QtWidgets.QLabel(self.centralwidget)
        self.r16.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.r16.setText("")
        self.r16.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r16.setObjectName("r16")
        self.r23 = QtWidgets.QLabel(self.centralwidget)
        self.r23.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.r23.setText("")
        self.r23.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r23.setObjectName("r23")
        self.r25 = QtWidgets.QLabel(self.centralwidget)
        self.r25.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.r25.setText("")
        self.r25.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r25.setObjectName("r25")
        self.r26 = QtWidgets.QLabel(self.centralwidget)
        self.r26.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.r26.setText("")
        self.r26.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r26.setObjectName("r26")
        self.r22 = QtWidgets.QLabel(self.centralwidget)
        self.r22.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.r22.setText("")
        self.r22.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r22.setObjectName("r22")
        self.r21 = QtWidgets.QLabel(self.centralwidget)
        self.r21.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.r21.setText("")
        self.r21.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r21.setObjectName("r21")
        self.r24 = QtWidgets.QLabel(self.centralwidget)
        self.r24.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.r24.setText("")
        self.r24.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r24.setObjectName("r24")
        self.r35 = QtWidgets.QLabel(self.centralwidget)
        self.r35.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.r35.setText("")
        self.r35.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r35.setObjectName("r35")
        self.r31 = QtWidgets.QLabel(self.centralwidget)
        self.r31.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.r31.setText("")
        self.r31.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r31.setObjectName("r31")
        self.r33 = QtWidgets.QLabel(self.centralwidget)
        self.r33.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.r33.setText("")
        self.r33.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r33.setObjectName("r33")
        self.r36 = QtWidgets.QLabel(self.centralwidget)
        self.r36.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.r36.setText("")
        self.r36.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r36.setObjectName("r36")
        self.r32 = QtWidgets.QLabel(self.centralwidget)
        self.r32.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.r32.setText("")
        self.r32.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r32.setObjectName("r32")
        self.r34 = QtWidgets.QLabel(self.centralwidget)
        self.r34.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.r34.setText("")
        self.r34.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r34.setObjectName("r34")
        self.r42 = QtWidgets.QLabel(self.centralwidget)
        self.r42.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.r42.setText("")
        self.r42.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r42.setObjectName("r42")
        self.r46 = QtWidgets.QLabel(self.centralwidget)
        self.r46.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.r46.setText("")
        self.r46.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r46.setObjectName("r46")
        self.r44 = QtWidgets.QLabel(self.centralwidget)
        self.r44.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.r44.setText("")
        self.r44.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r44.setObjectName("r44")
        self.r45 = QtWidgets.QLabel(self.centralwidget)
        self.r45.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.r45.setText("")
        self.r45.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r45.setObjectName("r45")
        self.r43 = QtWidgets.QLabel(self.centralwidget)
        self.r43.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.r43.setText("")
        self.r43.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r43.setObjectName("r43")
        self.r41 = QtWidgets.QLabel(self.centralwidget)
        self.r41.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.r41.setText("")
        self.r41.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r41.setObjectName("r41")
        self.r52 = QtWidgets.QLabel(self.centralwidget)
        self.r52.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.r52.setText("")
        self.r52.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r52.setObjectName("r52")
        self.r56 = QtWidgets.QLabel(self.centralwidget)
        self.r56.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.r56.setText("")
        self.r56.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r56.setObjectName("r56")
        self.r54 = QtWidgets.QLabel(self.centralwidget)
        self.r54.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.r54.setText("")
        self.r54.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r54.setObjectName("r54")
        self.r55 = QtWidgets.QLabel(self.centralwidget)
        self.r55.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.r55.setText("")
        self.r55.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r55.setObjectName("r55")
        self.r53 = QtWidgets.QLabel(self.centralwidget)
        self.r53.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.r53.setText("")
        self.r53.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r53.setObjectName("r53")
        self.r51 = QtWidgets.QLabel(self.centralwidget)
        self.r51.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.r51.setText("")
        self.r51.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r51.setObjectName("r51")
        self.r62 = QtWidgets.QLabel(self.centralwidget)
        self.r62.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.r62.setText("")
        self.r62.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r62.setObjectName("r62")
        self.r66 = QtWidgets.QLabel(self.centralwidget)
        self.r66.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.r66.setText("")
        self.r66.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r66.setObjectName("r66")
        self.r64 = QtWidgets.QLabel(self.centralwidget)
        self.r64.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.r64.setText("")
        self.r64.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r64.setObjectName("r64")
        self.r65 = QtWidgets.QLabel(self.centralwidget)
        self.r65.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.r65.setText("")
        self.r65.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r65.setObjectName("r65")
        self.r63 = QtWidgets.QLabel(self.centralwidget)
        self.r63.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.r63.setText("")
        self.r63.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r63.setObjectName("r63")
        self.r61 = QtWidgets.QLabel(self.centralwidget)
        self.r61.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.r61.setText("")
        self.r61.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r61.setObjectName("r61")
        self.r73 = QtWidgets.QLabel(self.centralwidget)
        self.r73.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.r73.setText("")
        self.r73.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r73.setObjectName("r73")
        self.r76 = QtWidgets.QLabel(self.centralwidget)
        self.r76.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.r76.setText("")
        self.r76.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r76.setObjectName("r76")
        self.r75 = QtWidgets.QLabel(self.centralwidget)
        self.r75.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.r75.setText("")
        self.r75.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r75.setObjectName("r75")
        self.r72 = QtWidgets.QLabel(self.centralwidget)
        self.r72.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.r72.setText("")
        self.r72.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r72.setObjectName("r72")
        self.r74 = QtWidgets.QLabel(self.centralwidget)
        self.r74.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.r74.setText("")
        self.r74.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r74.setObjectName("r74")
        self.r71 = QtWidgets.QLabel(self.centralwidget)
        self.r71.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.r71.setText("")
        self.r71.setPixmap(QtGui.QPixmap("connect-4-puck-red.png"))
        self.r71.setObjectName("r71")
        self.y11 = QtWidgets.QLabel(self.centralwidget)
        self.y11.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.y11.setText("")
        self.y11.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y11.setObjectName("y11")
        self.y12 = QtWidgets.QLabel(self.centralwidget)
        self.y12.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.y12.setText("")
        self.y12.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y12.setObjectName("y12")
        self.y13 = QtWidgets.QLabel(self.centralwidget)
        self.y13.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.y13.setText("")
        self.y13.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y13.setObjectName("y13")
        self.y14 = QtWidgets.QLabel(self.centralwidget)
        self.y14.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.y14.setText("")
        self.y14.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y14.setObjectName("y14")
        self.y15 = QtWidgets.QLabel(self.centralwidget)
        self.y15.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.y15.setText("")
        self.y15.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y15.setObjectName("y15")
        self.y16 = QtWidgets.QLabel(self.centralwidget)
        self.y16.setGeometry(QtCore.QRect(10, 0, 130, 130))
        self.y16.setText("")
        self.y16.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y16.setObjectName("y16")
        self.y23 = QtWidgets.QLabel(self.centralwidget)
        self.y23.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.y23.setText("")
        self.y23.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y23.setObjectName("y23")
        self.y24 = QtWidgets.QLabel(self.centralwidget)
        self.y24.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.y24.setText("")
        self.y24.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y24.setObjectName("y24")
        self.y22 = QtWidgets.QLabel(self.centralwidget)
        self.y22.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.y22.setText("")
        self.y22.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y22.setObjectName("y22")
        self.y26 = QtWidgets.QLabel(self.centralwidget)
        self.y26.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.y26.setText("")
        self.y26.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y26.setObjectName("y26")
        self.y21 = QtWidgets.QLabel(self.centralwidget)
        self.y21.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.y21.setText("")
        self.y21.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y21.setObjectName("y21")
        self.y25 = QtWidgets.QLabel(self.centralwidget)
        self.y25.setGeometry(QtCore.QRect(140, 0, 130, 130))
        self.y25.setText("")
        self.y25.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y25.setObjectName("y25")
        self.y33 = QtWidgets.QLabel(self.centralwidget)
        self.y33.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.y33.setText("")
        self.y33.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y33.setObjectName("y33")
        self.y34 = QtWidgets.QLabel(self.centralwidget)
        self.y34.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.y34.setText("")
        self.y34.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y34.setObjectName("y34")
        self.y32 = QtWidgets.QLabel(self.centralwidget)
        self.y32.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.y32.setText("")
        self.y32.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y32.setObjectName("y32")
        self.y36 = QtWidgets.QLabel(self.centralwidget)
        self.y36.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.y36.setText("")
        self.y36.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y36.setObjectName("y36")
        self.y31 = QtWidgets.QLabel(self.centralwidget)
        self.y31.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.y31.setText("")
        self.y31.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y31.setObjectName("y31")
        self.y35 = QtWidgets.QLabel(self.centralwidget)
        self.y35.setGeometry(QtCore.QRect(270, 0, 130, 130))
        self.y35.setText("")
        self.y35.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y35.setObjectName("y35")
        self.y41 = QtWidgets.QLabel(self.centralwidget)
        self.y41.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.y41.setText("")
        self.y41.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y41.setObjectName("y41")
        self.y45 = QtWidgets.QLabel(self.centralwidget)
        self.y45.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.y45.setText("")
        self.y45.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y45.setObjectName("y45")
        self.y44 = QtWidgets.QLabel(self.centralwidget)
        self.y44.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.y44.setText("")
        self.y44.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y44.setObjectName("y44")
        self.y43 = QtWidgets.QLabel(self.centralwidget)
        self.y43.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.y43.setText("")
        self.y43.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y43.setObjectName("y43")
        self.y46 = QtWidgets.QLabel(self.centralwidget)
        self.y46.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.y46.setText("")
        self.y46.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y46.setObjectName("y46")
        self.y42 = QtWidgets.QLabel(self.centralwidget)
        self.y42.setGeometry(QtCore.QRect(400, 0, 130, 130))
        self.y42.setText("")
        self.y42.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y42.setObjectName("y42")
        self.y51 = QtWidgets.QLabel(self.centralwidget)
        self.y51.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.y51.setText("")
        self.y51.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y51.setObjectName("y51")
        self.y55 = QtWidgets.QLabel(self.centralwidget)
        self.y55.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.y55.setText("")
        self.y55.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y55.setObjectName("y55")
        self.y54 = QtWidgets.QLabel(self.centralwidget)
        self.y54.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.y54.setText("")
        self.y54.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y54.setObjectName("y54")
        self.y53 = QtWidgets.QLabel(self.centralwidget)
        self.y53.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.y53.setText("")
        self.y53.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y53.setObjectName("y53")
        self.y56 = QtWidgets.QLabel(self.centralwidget)
        self.y56.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.y56.setText("")
        self.y56.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y56.setObjectName("y56")
        self.y52 = QtWidgets.QLabel(self.centralwidget)
        self.y52.setGeometry(QtCore.QRect(530, 0, 130, 130))
        self.y52.setText("")
        self.y52.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y52.setObjectName("y52")
        self.y61 = QtWidgets.QLabel(self.centralwidget)
        self.y61.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.y61.setText("")
        self.y61.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y61.setObjectName("y61")
        self.y65 = QtWidgets.QLabel(self.centralwidget)
        self.y65.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.y65.setText("")
        self.y65.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y65.setObjectName("y65")
        self.y64 = QtWidgets.QLabel(self.centralwidget)
        self.y64.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.y64.setText("")
        self.y64.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y64.setObjectName("y64")
        self.y63 = QtWidgets.QLabel(self.centralwidget)
        self.y63.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.y63.setText("")
        self.y63.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y63.setObjectName("y63")
        self.y66 = QtWidgets.QLabel(self.centralwidget)
        self.y66.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.y66.setText("")
        self.y66.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y66.setObjectName("y66")
        self.y62 = QtWidgets.QLabel(self.centralwidget)
        self.y62.setGeometry(QtCore.QRect(660, 0, 130, 130))
        self.y62.setText("")
        self.y62.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y62.setObjectName("y62")
        self.y71 = QtWidgets.QLabel(self.centralwidget)
        self.y71.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.y71.setText("")
        self.y71.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y71.setObjectName("y71")
        self.y75 = QtWidgets.QLabel(self.centralwidget)
        self.y75.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.y75.setText("")
        self.y75.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y75.setObjectName("y75")
        self.y74 = QtWidgets.QLabel(self.centralwidget)
        self.y74.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.y74.setText("")
        self.y74.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y74.setObjectName("y74")
        self.y73 = QtWidgets.QLabel(self.centralwidget)
        self.y73.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.y73.setText("")
        self.y73.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y73.setObjectName("y73")
        self.y76 = QtWidgets.QLabel(self.centralwidget)
        self.y76.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.y76.setText("")
        self.y76.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y76.setObjectName("y76")
        self.y72 = QtWidgets.QLabel(self.centralwidget)
        self.y72.setGeometry(QtCore.QRect(790, 0, 130, 130))
        self.y72.setText("")
        self.y72.setPixmap(QtGui.QPixmap("connect-4-puck-yellow.png"))
        self.y72.setObjectName("y72")

        self.redPucks = [[self.r11, self.r12, self.r13, self.r14, self.r15, self.r16],
                         [self.r21, self.r22, self.r23, self.r24, self.r25, self.r26],
                         [self.r31, self.r32, self.r33, self.r34, self.r35, self.r36],
                         [self.r41, self.r42, self.r43, self.r44, self.r45, self.r46],
                         [self.r51, self.r52, self.r53, self.r54, self.r55, self.r56],
                         [self.r61, self.r62, self.r63, self.r64, self.r65, self.r66],
                         [self.r71, self.r72, self.r73, self.r74, self.r75, self.r76]]

        self.yellowPucks = [[self.y11, self.y12, self.y13, self.y14, self.y15, self.y16],
                            [self.y21, self.y22, self.y23, self.y24, self.y25, self.y26],
                            [self.y31, self.y32, self.y33, self.y34, self.y35, self.y36],
                            [self.y41, self.y42, self.y43, self.y44, self.y45, self.y46],
                            [self.y51, self.y52, self.y53, self.y54, self.y55, self.y56],
                            [self.y61, self.y62, self.y63, self.y64, self.y65, self.y66],
                            [self.y71, self.y72, self.y73, self.y74, self.y75, self.y76]]

        self.columnCount = [0, 0, 0, 0, 0, 0, 0]

        self.turn = 1  # 1 is user 0 is com

        self.finalMove = 0
        self.finalLabel = ""
        self.finalColumn = 0

        for i in range(11, 17):
            exec(f"self.r{i}.setHidden(True)")
            exec(f"self.y{i}.setHidden(True)")
        for i in range(21, 27):
            exec(f"self.r{i}.setHidden(True)")
            exec(f"self.y{i}.setHidden(True)")
        for i in range(31, 37):
            exec(f"self.r{i}.setHidden(True)")
            exec(f"self.y{i}.setHidden(True)")
        for i in range(41, 47):
            exec(f"self.r{i}.setHidden(True)")
            exec(f"self.y{i}.setHidden(True)")
        for i in range(51, 57):
            exec(f"self.r{i}.setHidden(True)")
            exec(f"self.y{i}.setHidden(True)")
        for i in range(61, 67):
            exec(f"self.r{i}.setHidden(True)")
            exec(f"self.y{i}.setHidden(True)")
        for i in range(71, 77):
            exec(f"self.r{i}.setHidden(True)")
            exec(f"self.y{i}.setHidden(True)")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(949, 20, 281, 111))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.chooseMode = QtWidgets.QPushButton(self.groupBox)
        self.chooseMode.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.chooseMode.setObjectName("chooseMode")
        self.announceWinner = QtWidgets.QLabel(self.centralwidget)
        self.announceWinner.setGeometry(QtCore.QRect(950, 160, 281, 61))
        self.announceWinner.setObjectName("announceWinner")
        self.player1Score = QtWidgets.QLabel(self.centralwidget)
        self.player1Score.setGeometry(QtCore.QRect(950, 260, 281, 61))
        self.player1Score.setObjectName("player1Score")
        self.comScore = QtWidgets.QLabel(self.centralwidget)
        self.comScore.setGeometry(QtCore.QRect(950, 330, 281, 61))
        self.comScore.setObjectName("comScore")
        self.c1 = Label(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(10, 130, 131, 781))
        self.c1.setMouseTracking(False)
        self.c1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c1.setText("")
        self.c1.setObjectName("c1")
        self.c1.clicked.connect(self.add1)
        self.c1.setStyleSheet("QLabel::hover"
                              "{"
                              "border: 6px solid black;"
                              "}")
        self.c2 = Label(self.centralwidget)
        self.c2.setGeometry(QtCore.QRect(140, 130, 131, 781))
        self.c2.setMouseTracking(False)
        self.c2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c2.setText("")
        self.c2.setObjectName("c2")
        self.c2.setStyleSheet("QLabel::hover"
                              "{"
                              "border: 6px solid black;"
                              "}")
        self.c2.clicked.connect(self.add2)
        self.c3 = Label(self.centralwidget)
        self.c3.setGeometry(QtCore.QRect(270, 130, 131, 781))
        self.c3.setMouseTracking(False)
        self.c3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c3.setText("")
        self.c3.setObjectName("c3")
        self.c3.setStyleSheet("QLabel::hover"
                              "{"
                              "border: 6px solid black;"
                              "}")
        self.c3.clicked.connect(self.add3)
        self.c4 = Label(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(400, 130, 131, 781))
        self.c4.setMouseTracking(False)
        self.c4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c4.setText("")
        self.c4.setObjectName("c4")
        self.c4.setStyleSheet("QLabel::hover"
                              "{"
                              "border: 6px solid black;"
                              "}")
        self.c4.clicked.connect(self.add4)
        self.c5 = Label(self.centralwidget)
        self.c5.setGeometry(QtCore.QRect(530, 130, 131, 781))
        self.c5.setMouseTracking(False)
        self.c5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c5.setText("")
        self.c5.setObjectName("c5")
        self.c5.setStyleSheet("QLabel::hover"
                              "{"
                              "border: 6px solid black;"
                              "}")
        self.c5.clicked.connect(self.add5)
        self.c6 = Label(self.centralwidget)
        self.c6.setGeometry(QtCore.QRect(660, 130, 131, 781))
        self.c6.setMouseTracking(False)
        self.c6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c6.setText("")
        self.c6.setObjectName("c6")
        self.c6.setStyleSheet("QLabel::hover"
                              "{"
                              "border: 6px solid black;"
                              "}")
        self.c6.clicked.connect(self.add6)
        self.c7 = Label(self.centralwidget)
        self.c7.setGeometry(QtCore.QRect(790, 130, 131, 781))
        self.c7.setMouseTracking(False)
        self.c7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.c7.setText("")
        self.c7.setObjectName("c7")
        self.c7.setStyleSheet("QLabel::hover"
                              "{"
                              "border: 6px solid black;"
                              "}")
        self.c7.clicked.connect(self.add7)

        self.confirmMove = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.call())
        self.confirmMove.setGeometry(QtCore.QRect(950, 850, 110, 41))
        self.confirmMove.setObjectName("confirmMove")

        self.removeMove = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.reset())
        self.removeMove.setGeometry(QtCore.QRect(1120, 850, 110, 41))
        self.removeMove.setObjectName("removeMove")

        self.r11.raise_()
        self.r12.raise_()
        self.r13.raise_()
        self.r14.raise_()
        self.r15.raise_()
        self.r16.raise_()
        self.r23.raise_()
        self.r25.raise_()
        self.r26.raise_()
        self.r22.raise_()
        self.r21.raise_()
        self.r24.raise_()
        self.r35.raise_()
        self.r31.raise_()
        self.r33.raise_()
        self.r36.raise_()
        self.r32.raise_()
        self.r34.raise_()
        self.r42.raise_()
        self.r46.raise_()
        self.r44.raise_()
        self.r45.raise_()
        self.r43.raise_()
        self.r41.raise_()
        self.r52.raise_()
        self.r56.raise_()
        self.r54.raise_()
        self.r55.raise_()
        self.r53.raise_()
        self.r51.raise_()
        self.r62.raise_()
        self.r66.raise_()
        self.r64.raise_()
        self.r65.raise_()
        self.r63.raise_()
        self.r61.raise_()
        self.r73.raise_()
        self.r76.raise_()
        self.r75.raise_()
        self.r72.raise_()
        self.r74.raise_()
        self.r71.raise_()
        self.y11.raise_()
        self.y12.raise_()
        self.y13.raise_()
        self.y14.raise_()
        self.y15.raise_()
        self.y16.raise_()
        self.y23.raise_()
        self.y24.raise_()
        self.y22.raise_()
        self.y26.raise_()
        self.y21.raise_()
        self.y25.raise_()
        self.y33.raise_()
        self.y34.raise_()
        self.y32.raise_()
        self.y36.raise_()
        self.y31.raise_()
        self.y35.raise_()
        self.y41.raise_()
        self.y45.raise_()
        self.y44.raise_()
        self.y43.raise_()
        self.y46.raise_()
        self.y42.raise_()
        self.y51.raise_()
        self.y55.raise_()
        self.y54.raise_()
        self.y53.raise_()
        self.y56.raise_()
        self.y52.raise_()
        self.y61.raise_()
        self.y65.raise_()
        self.y64.raise_()
        self.y63.raise_()
        self.y66.raise_()
        self.y62.raise_()
        self.y71.raise_()
        self.y75.raise_()
        self.y74.raise_()
        self.y73.raise_()
        self.y76.raise_()
        self.y72.raise_()
        self.board.raise_()
        self.groupBox.raise_()
        self.announceWinner.raise_()
        self.player1Score.raise_()
        self.comScore.raise_()
        self.c1.raise_()
        self.c2.raise_()
        self.c3.raise_()
        self.c4.raise_()
        self.c5.raise_()
        self.c6.raise_()
        self.c7.raise_()

        self.comboBox.addItem("Minimax without alpha-beta pruning")
        self.comboBox.addItem("Minimax with alpha-beta pruning")

        ConnectFour.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConnectFour)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1254, 21))
        self.menubar.setObjectName("menubar")
        ConnectFour.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConnectFour)
        self.statusbar.setObjectName("statusbar")
        ConnectFour.setStatusBar(self.statusbar)

        self.retranslateUi(ConnectFour)
        QtCore.QMetaObject.connectSlotsByName(ConnectFour)

    def retranslateUi(self, ConnectFour):
        _translate = QtCore.QCoreApplication.translate
        ConnectFour.setWindowTitle(_translate("ConnectFour", "Connect Four"))
        ConnectFour.setWindowIcon(QtGui.QIcon("icon.png"))
        self.groupBox.setTitle(_translate("ConnectFour", "Choose your mode"))
        self.chooseMode.setText(_translate("ConnectFour", "Confirm"))
        self.confirmMove.setText(_translate("ConnectFour", "Confirm move"))
        self.removeMove.setText(_translate("ConnectFour", "Undo move"))
        self.announceWinner.setText(_translate("ConnectFour", "TextLabel"))
        self.player1Score.setText(_translate("ConnectFour", "TextLabel"))
        self.comScore.setText(_translate("ConnectFour", "TextLabel"))



    def add1(self):
        if self.columnCount[0] == 6:
            self.announceWinner.setText(" No more pucks can be added here!!")
            self.announceWinner.setFont(QFont("Arial", 13))
            self.announceWinner.setStyleSheet("background-color: #FF6961")

        elif self.turn:
            i = self.columnCount[0]
            lbl = self.redPucks[0][i]
            self.finalMove = i
            self.finalLabel = lbl
            self.finalColumn = 0
            lbl.setHidden(False)
            easing_curve = QEasingCurve.OutExpo
            duration = 900
            self.animation = QPropertyAnimation(lbl, b"pos")
            self.animation.setEasingCurve(easing_curve)
            self.animation.setDuration(duration)
            self.animation.setEndValue(lbl.pos() + QPoint(0, 130*(6-i)))
            self.animation.start()
            self.columnCount[0] = self.columnCount[0] + 1
            self.turn = 0


    def add2(self):
        if self.columnCount[1] == 6:
            self.announceWinner.setText("No more pucks can be added here!!")
            self.announceWinner.setFont(QFont("Arial", 13))
            self.announceWinner.setStyleSheet("background-color: #FF6961")

        elif self.turn:
            i = self.columnCount[1]
            lbl = self.redPucks[1][i]
            self.finalMove = i
            self.finalLabel = lbl
            self.finalColumn = 1
            lbl.setHidden(False)
            easing_curve = QEasingCurve.OutExpo
            duration = 900
            self.animation = QPropertyAnimation(lbl, b"pos")
            self.animation.setEasingCurve(easing_curve)
            self.animation.setDuration(duration)
            self.animation.setEndValue(lbl.pos() + QPoint(0, 130*(6-i)))
            self.animation.start()
            self.columnCount[1] = self.columnCount[1] + 1
            self.turn = 0

    def add3(self):
        if self.columnCount[2] == 6:
            self.announceWinner.setText("No more pucks can be added here!!")
            self.announceWinner.setFont(QFont("Arial", 13))
            self.announceWinner.setStyleSheet("background-color: #FF6961")

        elif self.turn:
            i = self.columnCount[2]
            lbl = self.redPucks[2][i]
            self.finalMove = i
            self.finalLabel = lbl
            self.finalColumn = 2
            lbl.setHidden(False)
            easing_curve = QEasingCurve.OutExpo
            duration = 900
            self.animation = QPropertyAnimation(lbl, b"pos")
            self.animation.setEasingCurve(easing_curve)
            self.animation.setDuration(duration)
            self.animation.setEndValue(lbl.pos() + QPoint(0, 130*(6-i)))
            self.animation.start()
            self.columnCount[2] = self.columnCount[2] + 1
            self.turn = 0

    def add4(self):
        if self.columnCount[3] == 6:
            self.announceWinner.setText("No more pucks can be added here!!")
            self.announceWinner.setFont(QFont("Arial", 13))
            self.announceWinner.setStyleSheet("background-color: #FF6961")

        elif self.turn:
            i = self.columnCount[3]
            lbl = self.redPucks[3][i]
            self.finalMove = i
            self.finalLabel = lbl
            self.finalColumn = 3
            lbl.setHidden(False)
            easing_curve = QEasingCurve.OutExpo
            duration = 900
            self.animation = QPropertyAnimation(lbl, b"pos")
            self.animation.setEasingCurve(easing_curve)
            self.animation.setDuration(duration)
            self.animation.setEndValue(lbl.pos() + QPoint(0, 130*(6-i)))
            self.animation.start()
            self.columnCount[3] = self.columnCount[3] + 1
            self.turn = 0

    def add5(self):
        if self.columnCount[4] == 6:
            self.announceWinner.setText("No more pucks can be added here!!")
            self.announceWinner.setFont(QFont("Arial", 13))
            self.announceWinner.setStyleSheet("background-color: #FF6961")

        elif self.turn:
            i = self.columnCount[4]
            lbl = self.redPucks[4][i]
            self.finalMove = i
            self.finalLabel = lbl
            self.finalColumn = 4
            lbl.setHidden(False)
            easing_curve = QEasingCurve.OutExpo
            duration = 900
            self.animation = QPropertyAnimation(lbl, b"pos")
            self.animation.setEasingCurve(easing_curve)
            self.animation.setDuration(duration)
            self.animation.setEndValue(lbl.pos() + QPoint(0, 130*(6-i)))
            self.animation.start()
            self.columnCount[4] = self.columnCount[4] + 1
            self.turn = 0

    def add6(self):
        if self.columnCount[5] == 6:
            self.announceWinner.setText("No more pucks can be added here!!")
            self.announceWinner.setFont(QFont("Arial", 13))
            self.announceWinner.setStyleSheet("background-color: #FF6961")

        elif self.turn:
            i = self.columnCount[5]
            lbl = self.redPucks[5][i]
            self.finalMove = i
            self.finalLabel = lbl
            self.finalColumn = 5
            lbl.setHidden(False)
            easing_curve = QEasingCurve.OutExpo
            duration = 900
            self.animation = QPropertyAnimation(lbl, b"pos")
            self.animation.setEasingCurve(easing_curve)
            self.animation.setDuration(duration)
            self.animation.setEndValue(lbl.pos() + QPoint(0, 130*(6-i)))
            self.animation.start()
            self.columnCount[5] = self.columnCount[5] + 1
            self.turn = 0

    def add7(self):
        if self.columnCount[6] == 6:
            self.announceWinner.setText("No more pucks can be added here!!")
            self.announceWinner.setFont(QFont("Arial", 13))
            self.announceWinner.setStyleSheet("background-color: #FF6961")

        elif self.turn:
            i = self.columnCount[6]
            lbl = self.redPucks[6][i]
            self.finalMove = i
            self.finalLabel = lbl
            self.finalColumn = 6
            lbl.setHidden(False)
            easing_curve = QEasingCurve.OutExpo
            duration = 900
            self.animation = QPropertyAnimation(lbl, b"pos")
            self.animation.setEasingCurve(easing_curve)
            self.animation.setDuration(duration)
            self.animation.setEndValue(lbl.pos() + QPoint(0, 130*(6-i)))
            self.animation.start()
            self.columnCount[6] = self.columnCount[6] + 1
            self.turn = 0


    def reset(self):
        if not(self.turn):
            lbl = self.finalLabel
            i = self.finalMove
            c = self.finalColumn
            x = lbl.x()
            y = lbl.y()
            lbl.move(x, y - (130 * (6 - i)))
            lbl.setHidden(True)
            self.columnCount[c] = self.columnCount[c] - 1
            self.turn = 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ConnectFour = QtWidgets.QMainWindow()
    ui = Ui_ConnectFour()
    ui.setupUi(ConnectFour)
    ConnectFour.show()
    sys.exit(app.exec_())
