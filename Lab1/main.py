import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QPoint
from algos import *
import math


class Label(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QLabel.__init__(self, parent=parent)

    def mousePressEvent(self, event):
        self.clicked.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.path = []
        self.counter = 0
        self.label_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.values_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.flag = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 531, 531))
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("blackbackground.png"))
        self.label.setObjectName("label")
        self.label_a = Label(self.centralwidget)
        self.label_a.setGeometry(QtCore.QRect(10, 10, 171, 171))
        self.label_a.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_a.setObjectName("label_a")
        self.label_a.setFont(QFont("Arial", 70))
        self.label_a.setAlignment(QtCore.Qt.AlignCenter)
        self.label_a.clicked.connect(self.edita)
        self.label_b = Label(self.centralwidget)
        self.label_b.setGeometry(QtCore.QRect(180, 10, 171, 171))
        self.label_b.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_b.setObjectName("label_b")
        self.label_b.setFont(QFont("Arial", 70))
        self.label_b.setAlignment(QtCore.Qt.AlignCenter)
        self.label_b.clicked.connect(self.editb)
        self.label_c = Label(self.centralwidget)
        self.label_c.setGeometry(QtCore.QRect(350, 10, 171, 171))
        self.label_c.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_c.setObjectName("label_c")
        self.label_c.setFont(QFont("Arial", 70))
        self.label_c.setAlignment(QtCore.Qt.AlignCenter)
        self.label_c.clicked.connect(self.editc)
        self.label_f = Label(self.centralwidget)
        self.label_f.setGeometry(QtCore.QRect(350, 180, 171, 171))
        self.label_f.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_f.setObjectName("label_f")
        self.label_f.setFont(QFont("Arial", 70))
        self.label_f.setAlignment(QtCore.Qt.AlignCenter)
        self.label_f.clicked.connect(self.editf)
        self.label_e = Label(self.centralwidget)
        self.label_e.setGeometry(QtCore.QRect(180, 180, 171, 171))
        self.label_e.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_e.setObjectName("label_e")
        self.label_e.setFont(QFont("Arial", 70))
        self.label_e.setAlignment(QtCore.Qt.AlignCenter)
        self.label_e.clicked.connect(self.edite)
        self.label_d = Label(self.centralwidget)
        self.label_d.setGeometry(QtCore.QRect(10, 180, 171, 171))
        self.label_d.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_d.setObjectName("label_d")
        self.label_d.setFont(QFont("Arial", 70))
        self.label_d.setAlignment(QtCore.Qt.AlignCenter)
        self.label_d.clicked.connect(self.editd)
        self.label_i = Label(self.centralwidget)
        self.label_i.setGeometry(QtCore.QRect(350, 350, 171, 171))
        self.label_i.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_i.setObjectName("label_i")
        self.label_i.setFont(QFont("Arial", 70))
        self.label_i.setAlignment(QtCore.Qt.AlignCenter)
        self.label_i.clicked.connect(self.editi)
        self.label_h = Label(self.centralwidget)
        self.label_h.setGeometry(QtCore.QRect(180, 350, 171, 171))
        self.label_h.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_h.setObjectName("label_h")
        self.label_h.setFont(QFont("Arial", 70))
        self.label_h.setAlignment(QtCore.Qt.AlignCenter)
        self.label_h.clicked.connect(self.edith)
        self.label_g = Label(self.centralwidget)
        self.label_g.setGeometry(QtCore.QRect(10, 350, 171, 171))
        self.label_g.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_g.setObjectName("label_g")
        self.label_g.setFont(QFont("Arial", 70))
        self.label_g.setAlignment(QtCore.Qt.AlignCenter)
        self.label_g.clicked.connect(self.editg)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 50, 281, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("BFS")
        self.comboBox.addItem("DFS")
        self.comboBox.addItem("A* (manhattan)")
        self.comboBox.addItem("A* (euclidean)")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(550, 20, 141, 21))
        self.label_11.setObjectName("label_11")
        self.solvable_or_not = QtWidgets.QLabel(self.centralwidget)
        self.solvable_or_not.setGeometry(QtCore.QRect(550, 160, 281, 41))
        self.solvable_or_not.setObjectName("solvable_or_not")
        self.solvable_or_not.setFont(QFont("Arial", 15))
        self.solvable_or_not.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.run_algorithm()
        )
        self.pushButton.setGeometry(QtCore.QRect(550, 90, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.moves()
        )
        self.pushButton_2.setGeometry(QtCore.QRect(710, 90, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(550, 250, 261, 31))
        self.label_12.setObjectName("label_12")
        self.label_12.setFont(QFont("Arial", 14))
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(550, 290, 261, 31))
        self.label_13.setObjectName("label_13")
        self.label_13.setFont(QFont("Arial", 14))
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(550, 330, 261, 31))
        self.label_14.setObjectName("label_14")
        self.label_14.setFont(QFont("Arial", 14))
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(550, 370, 261, 31))
        self.label_15.setObjectName("label_15")
        self.label_15.setFont(QFont("Arial", 14))
        self.pushButton_3 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.clear()
        )
        self.pushButton_3.setGeometry(QtCore.QRect(630, 480, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_a.setText(_translate("MainWindow", ""))
        self.label_b.setText(_translate("MainWindow", ""))
        self.label_c.setText(_translate("MainWindow", ""))
        self.label_f.setText(_translate("MainWindow", ""))
        self.label_e.setText(_translate("MainWindow", ""))
        self.label_d.setText(_translate("MainWindow", ""))
        self.label_i.setText(_translate("MainWindow", ""))
        self.label_h.setText(_translate("MainWindow", ""))
        self.label_g.setText(_translate("MainWindow", ""))
        self.label_11.setText(_translate("MainWindow", "Choose solving algorithm:"))
        self.solvable_or_not.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "View"))
        self.label_12.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", ""))
        self.label_14.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", "Reset"))
        self.label_15.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", "Reset"))

    def edita(self):
        var = self.label_a
        if self.counter < 9 and self.label_array[0][0] != var:
            self.label_array[0][0] = var
            self.values_array[0][0] = self.counter
            if self.counter == 0:
                self.label_a.setText("")
                self.label_a.setStyleSheet("")
            else:
                self.label_a.setText(str(self.counter))
                self.label_a.setStyleSheet("background-color: gray")
            self.counter = self.counter + 1

    def editb(self):
        var = self.label_b
        if self.counter < 9 and self.label_array[0][1] != var:
            self.label_array[0][1] = var
            self.values_array[0][1] = self.counter
            if self.counter == 0:
                self.label_b.setText("")
                self.label_b.setStyleSheet("")
            else:
                self.label_b.setText(str(self.counter))
                self.label_b.setStyleSheet("background-color: gray")
            self.counter = self.counter + 1

    def editc(self):
        var = self.label_c
        if self.counter < 9 and self.label_array[0][2] != var:
            self.label_array[0][2] = var
            self.values_array[0][2] = self.counter
            if self.counter == 0:
                self.label_c.setText("")
                self.label_c.setStyleSheet("")
            else:
                self.label_c.setText(str(self.counter))
                self.label_c.setStyleSheet("background-color: gray")
            self.counter = self.counter + 1

    def editd(self):
        var = self.label_d
        if self.counter < 9 and self.label_array[1][0] != var:
            self.label_array[1][0] = var
            self.values_array[1][0] = self.counter
            if self.counter == 0:
                self.label_d.setText("")
                self.label_d.setStyleSheet("")
            else:
                self.label_d.setText(str(self.counter))
                self.label_d.setStyleSheet("background-color: gray")
            self.counter = self.counter + 1

    def edite(self):
        var = self.label_e
        if self.counter < 9 and self.label_array[1][1] != var:
            self.label_array[1][1] = var
            self.values_array[1][1] = self.counter
            if self.counter == 0:
                self.label_e.setText("")
                self.label_e.setStyleSheet("")
            else:
                self.label_e.setText(str(self.counter))
                self.label_e.setStyleSheet("background-color: gray")
            self.counter = self.counter + 1

    def editf(self):
        var = self.label_f
        if self.counter < 9 and self.label_array[1][2] != var:
            self.label_array[1][2] = var
            self.values_array[1][2] = self.counter
            if self.counter == 0:
                self.label_f.setText("")
                self.label_f.setStyleSheet("")
            else:
                self.label_f.setText(str(self.counter))
                self.label_f.setStyleSheet("background-color: gray")
            self.counter = self.counter + 1

    def editg(self):
        var = self.label_g
        if self.counter < 9 and self.label_array[2][0] != var:
            self.label_array[2][0] = var
            self.values_array[2][0] = self.counter
            if self.counter == 0:
                self.label_g.setText("")
                self.label_g.setStyleSheet("")
            else:
                self.label_g.setText(str(self.counter))
                self.label_g.setStyleSheet("background-color: gray")
            self.counter = self.counter + 1

    def edith(self):
        var = self.label_h
        if self.counter < 9 and self.label_array[2][1] != var:
            self.label_array[2][1] = var
            self.values_array[2][1] = self.counter
            if self.counter == 0:
                self.label_h.setText("")
                self.label_h.setStyleSheet("")
            else:
                self.label_h.setText(str(self.counter))
                self.label_h.setStyleSheet("background-color: gray")
            self.counter = self.counter + 1

    def editi(self):
        var = self.label_i
        if self.counter < 9 and self.label_array[2][2] != var:
            self.label_array[2][2] = var
            self.values_array[2][2] = self.counter
            if self.counter == 0:
                self.label_i.setText("")
                self.label_i.setStyleSheet("")
            else:
                self.label_i.setText(str(self.counter))
                self.label_i.setStyleSheet("background-color: gray")
            self.counter = self.counter + 1

    def run_algorithm(self):
        if self.comboBox.currentText() == "BFS":
            start = time.time()
            success, expanded_count, explored, parent_map = bfs(self.values_array)
            end = time.time()
            net_time = round((end - start), 6)
            self.label_12.setText("Elapsed time: " + str(net_time) + "s")
            self.label_13.setText("Nodes expanded: " + str(expanded_count))
            cost, path, depth = get_path_depth(explored, parent_map)
            self.path = path
            self.label_14.setText("Search depth: " + str(depth))
            if success:
                self.label_15.setText("Path cost: " + str(cost))
                self.solvable_or_not.setText("This is a solvable problem")
                self.solvable_or_not.setStyleSheet("background-color: lightGreen")
            else:
                self.solvable_or_not.setText("This is an unsolvable problem")
                self.solvable_or_not.setStyleSheet("background-color: #FF6961")

        if self.comboBox.currentText() == "DFS":
            start = time.time()
            success, expanded_count, explored, parent_map = dfs(self.values_array)
            end = time.time()
            net_time = round((end - start), 6)
            self.label_12.setText("Elapsed time: " + str(net_time) + "s")
            self.label_13.setText("Nodes expanded: " + str(expanded_count))
            cost, path, depth = get_path_depth(explored, parent_map)
            self.path = path
            self.label_14.setText("Search depth: " + str(depth))
            if success:
                self.label_15.setText("Path cost: " + str(cost))
                self.solvable_or_not.setText("This is a solvable problem")
                self.solvable_or_not.setStyleSheet("background-color: lightGreen")
            else:
                self.solvable_or_not.setText("This is an unsolvable problem")
                self.solvable_or_not.setStyleSheet("background-color: #FF6961")

        if self.comboBox.currentText() == "A* (manhattan)":
            start = time.time()
            success, expanded_count, explored, parent_map = a_star(
                self.values_array, manhattan
            )
            end = time.time()
            net_time = round((end - start), 6)
            self.label_12.setText("Elapsed time: " + str(net_time) + "s")
            self.label_13.setText("Nodes expanded: " + str(expanded_count))
            cost, path, depth = get_path_depth(explored, parent_map)
            self.path = path
            self.label_14.setText("Search depth: " + str(depth))
            if success:
                self.label_15.setText("Path cost: " + str(cost))
                self.solvable_or_not.setText("This is a solvable problem")
                self.solvable_or_not.setStyleSheet("background-color: lightGreen")
            else:
                self.solvable_or_not.setText("This is an unsolvable problem")
                self.solvable_or_not.setStyleSheet("background-color: #FF6961")

        if self.comboBox.currentText() == "A* (euclidean)":
            start = time.time()
            success, expanded_count, explored, parent_map = a_star(
                self.values_array, euclidean
            )
            end = time.time()
            net_time = round((end - start), 6)
            self.label_12.setText("Elapsed time: " + str(net_time) + "s")
            self.label_13.setText("Nodes expanded: " + str(expanded_count))
            cost, path, depth = get_path_depth(explored, parent_map)
            self.path = path
            self.label_14.setText("Search depth: " + str(depth))
            if success:
                self.label_15.setText("Path cost: " + str(cost))
                self.solvable_or_not.setText("This is a solvable problem")
                self.solvable_or_not.setStyleSheet("background-color: lightGreen")
            else:
                self.solvable_or_not.setText("This is an unsolvable problem")
                self.solvable_or_not.setStyleSheet("background-color: #FF6961")

    def moves(self):
        def moves(self):
            print(self.path)

        length = len(self.path)
        temp1 = self.path[length - 1]
        temp2 = self.path[length - 2]
        temp_arr1 = decompress(temp1)
        temp_arr2 = decompress(temp2)
        i1, j1 = get_row_col(0, temp_arr1)  # i is row, j is column
        i2, j2 = get_row_col(0, temp_arr2)
        if i2 > i1:
            # move right
            temp_lab1 = self.label_array[i1][j1]
            temp_lab2 = self.label_array[i2][j2]
            temp_lab1.move(temp_lab1.pos() + QPoint(0, 170))
            temp_lab2.move(temp_lab2.pos() + QPoint(0, -170))

        elif i2 < i1:
            # move left
            temp_lab1 = self.label_array[i1][j1]
            temp_lab2 = self.label_array[i2][j2]
            temp_lab1.move(temp_lab1.pos() + QPoint(0, -170))
            temp_lab2.move(temp_lab2.pos() + QPoint(0, 170))

        elif j2 > j1:
            temp_lab1 = self.label_array[i1][j1]
            temp_lab2 = self.label_array[i2][j2]
            temp_lab1.move(temp_lab1.pos() + QPoint(170, 0))
            temp_lab2.move(temp_lab2.pos() + QPoint(-170, 0))

        elif j2 < j1:
            temp_lab1 = self.label_array[i1][j1]
            temp_lab2 = self.label_array[i2][j2]
            temp_lab1.move(temp_lab1.pos() + QPoint(-170, 0))
            temp_lab2.move(temp_lab2.pos() + QPoint(170, 0))

        swap_lab = self.label_array[i1][j1]
        self.label_array[i1][j1] = self.label_array[i2][j2]
        self.label_array[i2][j2] = swap_lab
        self.path.pop()

    def clear(self):
        self.values_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for row in self.label_array:
            for label in row:
                if label != 0:
                    label.setText("")
                    label.setStyleSheet("")
        self.label_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.counter = 0


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
