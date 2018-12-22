# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import numpy as np
import time
import pict_rc
from PyQt5.QtWidgets import *
from query import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from getStation import *
from PyQt5.QtCore import Qt,QDate,QDateTime
from PyQt5.QtGui import QPalette, QPixmap, QColor

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1600, 1400)
        mainWindow.setMinimumSize(QtCore.QSize(1600, 1400))
        mainWindow.setMaximumSize(QtCore.QSize(1600, 1400))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1600, 1400))
        self.centralwidget.setMaximumSize(QtCore.QSize(1600, 1400))
        self.centralwidget.setObjectName("centralwidget")
        #设置顶部图片
        self.label_title_img = QtWidgets.QLabel(self.centralwidget)
        self.label_title_img.setGeometry(QtCore.QRect(0, 0, 1600, 246))
        self.label_title_img.setStyleSheet("background-image: url(:/png/picture/bg1.png);")
        self.label_title_img.setText("")
        self.label_title_img.setObjectName("label_title_img")
        #输入出发地，目的地等
        self.widget_dest = QtWidgets.QWidget(self.centralwidget)
        self.widget_dest.setGeometry(QtCore.QRect(0, 246, 1600, 200))
        self.widget_dest.setStyleSheet("background-image: url(:/png/picture/bg2.png);")
        self.widget_dest.setObjectName("widget_dest")
        self.label_start = QtWidgets.QLabel(self.widget_dest)
        self.label_start.setGeometry(QtCore.QRect(40, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_start.setFont(font)
        self.label_start.setObjectName("label_start")
        self.label = QtWidgets.QLabel(self.widget_dest)
        self.label.setGeometry(QtCore.QRect(440, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_dest)
        self.label_2.setGeometry(QtCore.QRect(840, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # 日期设置
        self.dateTimeEdit_start = QtWidgets.QDateTimeEdit(self.widget_dest)
        self.dateTimeEdit_start.setGeometry(QtCore.QRect(1020, 80, 221, 61))
        self.dateTimeEdit_start.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit_start.setDisplayFormat("yyyy-MM-dd")
        self.dateTimeEdit_start.setMinimumDate(QDate.currentDate())
        self.dateTimeEdit_start.setMaximumDate(QDate.currentDate().addDays(29))
        self.dateTimeEdit_start.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";\n")
        self.dateTimeEdit_start.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateTimeEdit_start.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateTimeEdit_start.setCalendarPopup(True)
        self.dateTimeEdit_start.setObjectName("dateTimeEdit_start")
        #查询按钮
        self.pushButton_query = QtWidgets.QPushButton(self.widget_dest)
        self.pushButton_query.setGeometry(QtCore.QRect(1350, 80, 101, 51))
        self.pushButton_query.setObjectName("pushButton_query")
        self.lineEdit_start = QtWidgets.QLineEdit(self.widget_dest)
        self.lineEdit_start.setGeometry(QtCore.QRect(220, 80, 151, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.lineEdit_start.setFont(font)
        self.lineEdit_start.setObjectName("lineEdit_start")
        self.lineEdit_end = QtWidgets.QLineEdit(self.widget_dest)
        self.lineEdit_end.setGeometry(QtCore.QRect(600, 80, 151, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.lineEdit_end.setFont(font)
        self.lineEdit_end.setObjectName("lineEdit_end")
        self.widget_class = QtWidgets.QWidget(self.centralwidget)
        self.widget_class.setGeometry(QtCore.QRect(0, 446, 1600, 200))
        self.widget_class.setStyleSheet("background-image: url(:/png/picture/bg3.png);")
        self.widget_class.setObjectName("widget_class")
        self.label_traintype = QtWidgets.QLabel(self.widget_class)
        self.label_traintype.setGeometry(QtCore.QRect(40, 60, 181, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_traintype.setFont(font)
        self.label_traintype.setObjectName("label_traintype")

        #确定乘车类型
        self.checkBox_G = QtWidgets.QCheckBox(self.widget_class)
        self.checkBox_G.setGeometry(QtCore.QRect(280, 60, 151, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.checkBox_G.setFont(font)
        self.checkBox_G.setObjectName("checkBox_G")
        self.checkBox_D = QtWidgets.QCheckBox(self.widget_class)
        self.checkBox_D.setGeometry(QtCore.QRect(550, 60, 151, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.checkBox_D.setFont(font)
        self.checkBox_D.setObjectName("checkBox_D")
        self.checkBox_Z = QtWidgets.QCheckBox(self.widget_class)
        self.checkBox_Z.setGeometry(QtCore.QRect(810, 60, 161, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.checkBox_Z.setFont(font)
        self.checkBox_Z.setObjectName("checkBox_Z")
        self.checkBox_T = QtWidgets.QCheckBox(self.widget_class)
        self.checkBox_T.setGeometry(QtCore.QRect(1060, 60, 151, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.checkBox_T.setFont(font)
        self.checkBox_T.setObjectName("checkBox_T")
        self.checkBox_K = QtWidgets.QCheckBox(self.widget_class)
        self.checkBox_K.setGeometry(QtCore.QRect(1300, 60, 161, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.checkBox_K.setFont(font)
        self.checkBox_K.setObjectName("checkBox_K")
        self.label_info_img = QtWidgets.QLabel(self.centralwidget)
        self.label_info_img.setGeometry(QtCore.QRect(0, 646, 1600, 103))
        self.label_info_img.setStyleSheet("background-image: url(:/png/picture/bg4.png);")
        self.label_info_img.setText("")
        self.label_info_img.setObjectName("label_info_img")
        #表格控件
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 749, 1600, 651))
        self.model = QStandardItemModel();  # 创建存储数据的模式
        # 根据空间自动改变列宽度并且不可修改列宽度
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表头不可见
        self.tableView.horizontalHeader().setVisible(False)
        # 纵向表头不可见
        self.tableView.verticalHeader().setVisible(False)
        # 设置表格内容文字大小
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableView.setFont(font)
        # 设置表格内容不可编辑
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 垂直滚动条始终开启
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableView.setObjectName("tableView")

        mainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.lineEdit_start, self.lineEdit_end)
        mainWindow.setTabOrder(self.lineEdit_end, self.dateTimeEdit_start)
        mainWindow.setTabOrder(self.dateTimeEdit_start, self.pushButton_query)
        mainWindow.setTabOrder(self.pushButton_query, self.checkBox_G)
        mainWindow.setTabOrder(self.checkBox_G, self.checkBox_D)
        mainWindow.setTabOrder(self.checkBox_D, self.checkBox_Z)
        mainWindow.setTabOrder(self.checkBox_Z, self.checkBox_T)
        mainWindow.setTabOrder(self.checkBox_T, self.checkBox_K)
        mainWindow.setTabOrder(self.checkBox_K, self.tableView)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "辉辉-爬票"))
        self.label_start.setText(_translate("mainWindow", "出发地："))
        self.label.setText(_translate("mainWindow", "目的地："))
        self.label_2.setText(_translate("mainWindow", "出发日："))
        self.pushButton_query.setText(_translate("mainWindow", "查询"))
        self.label_traintype.setText(_translate("mainWindow", "车次类型："))
        self.checkBox_G.setText(_translate("mainWindow", "G-高铁"))
        self.checkBox_D.setText(_translate("mainWindow", "D-动车"))
        self.checkBox_Z.setText(_translate("mainWindow", "Z-直达"))
        self.checkBox_T.setText(_translate("mainWindow", "T-特快"))
        self.checkBox_K.setText(_translate("mainWindow", "K-快速"))

        self.pushButton_query.clicked.connect(self.on_click)
        self.checkBox_G.stateChanged.connect(self.change_G)
        self.checkBox_D.stateChanged.connect(self.change_D)
        self.checkBox_Z.stateChanged.connect(self.change_Z)
        self.checkBox_K.stateChanged.connect(self.change_K)
        self.checkBox_T.stateChanged.connect(self.change_T)

    def change_G(self,state):
        if state==QtCore.Qt.Checked:
            get_Ginfo()
            class_data.sort(key=lambda x:x[3])
            self.displayTable(len(class_data),16,class_data)
        else:
            remove_Ginfo()
            self.displayTable(len(class_data), 16, class_data)
    def change_D(self, state):
        if state==QtCore.Qt.Checked:
            get_Dinfo()
            class_data.sort(key=lambda x: x[3])
            self.displayTable(len(class_data),16,class_data)
        else:
            remove_Dinfo()
            self.displayTable(len(class_data), 16, class_data)
    def change_Z(self, state):
        if state==QtCore.Qt.Checked:
            get_Zinfo()
            class_data.sort(key=lambda x: x[3])
            self.displayTable(len(class_data),16,class_data)
        else:
            remove_Zinfo()
            self.displayTable(len(class_data), 16, class_data)
    def change_T(self, state):
        if state==QtCore.Qt.Checked:
            get_Tinfo()
            class_data.sort(key=lambda x: x[3])
            self.displayTable(len(class_data),16,class_data)
        else:
            remove_Tinfo()
            self.displayTable(len(class_data), 16, class_data)
    def change_K(self, state):
        if state==QtCore.Qt.Checked:
            get_Kinfo()
            self.displayTable(len(class_data),16,class_data)
        else:
            remove_Kinfo()
            self.displayTable(len(class_data), 16, class_data)
    def on_click(self):
        getStart = self.lineEdit_start.text()
        getEnd = self.lineEdit_end.text()
        getDate = self.dateTimeEdit_start.date().getDate()
        finalDate = str(getDate[0])
        finalDate += '-'+str(getDate[1]).zfill(2)
        finalDate += '-'+str(getDate[2]).zfill(2)
        if isStationExist()==True:
            station = eval(read())
            if getStart!="" and getEnd!="":
                if getStart in station and getEnd in station :
                    start = station[getStart]
                    end = station[getEnd]
                    data = query(start,end,finalDate)
                    if len(data)!=0:
                        self.displayTable(len(data),16,data)
                    else:
                        self.messageDialog('警告', '此阶段没有车辆运行！')
                else:
                    self.messageDialog('警告', '输入的站名不存在')
            else:
                self.messageDialog('警告', '请填写车站名称！')
        else:
            self.messageDialog('警告', '未下载车站查询文件！')


    # 显示消息提示框，参数title为提示框标题文字，message为提示信息
    def messageDialog(self, title, message):
        msg_box = QMessageBox(QMessageBox.Warning, title, message)
        msg_box.exec_()
    #查询结果显示在表格中
    def displayTable(self,row,col,data):
        self.model.clear()
        for i in range(row):
            for j in range(col):
                item = QStandardItem(data[i][j])
                self.model.setItem(i,j,item)
        self.tableView.setModel(self.model)


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv) #实例化application，作
    # 为主程序的入口
    MainWindow = QtWidgets.QMainWindow()   #实例化mainwindow,创建自带menu的窗体
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  #当来自操作系统的分发事件调用指派窗口时
    # 应用程序开启主循环（mainloop）过程，
    # 当窗口创建完成，需要结束主循环过程，
    # 这时候呼叫sys.exit（）方法来，结束主循环过程退出，
    # 并且释放内存。为什么用app.exec_()而不是app.exec()？
    # 因为exec是python系统默认关键字，为了以示区别，所以写成exec_

if __name__ == '__main__':
    if isStationExist()==False:
        getStation()
    show_MainWindow()
