# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 700, 201))
        self.groupBox.setObjectName("groupBox")
        self.btnReadExcel = QtWidgets.QPushButton(self.groupBox)
        self.btnReadExcel.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.btnReadExcel.setObjectName("btnReadExcel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 270, 700, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setGeometry(QtCore.QRect(150, 41, 500, 181))
        self.tableView.setObjectName("tableView")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 61, 77, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCreateDB = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCreateDB.setObjectName("btnCreateDB")
        self.verticalLayout.addWidget(self.btnCreateDB)
        self.btnQueryData = QtWidgets.QPushButton(self.layoutWidget)
        self.btnQueryData.setObjectName("btnQueryData")
        self.verticalLayout.addWidget(self.btnQueryData)
        self.btnAddData = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAddData.setObjectName("btnAddData")
        self.verticalLayout.addWidget(self.btnAddData)
        self.btnDelData = QtWidgets.QPushButton(self.layoutWidget)
        self.btnDelData.setObjectName("btnDelData")
        self.verticalLayout.addWidget(self.btnDelData)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Excel操作"))
        self.btnReadExcel.setText(_translate("MainWindow", "读取Excel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "数据库操作"))
        self.btnCreateDB.setText(_translate("MainWindow", "创建数据库"))
        self.btnQueryData.setText(_translate("MainWindow", "查询数据库"))
        self.btnAddData.setText(_translate("MainWindow", "添加数据"))
        self.btnDelData.setText(_translate("MainWindow", "删除数据"))

import resource_rc
