# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'MainWindow.ui'
##
# Created by: Qt User Interface Compiler version 5.14.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, QRegExp, Signal, Slot, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient, QRegExpValidator)
from PySide2.QtWidgets import *

from Ui_Dialog import Ui_Dialog

from random import sample
import xlrd
import os


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 820)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MainLayout = QVBoxLayout(self.centralwidget)
        self.MainLayout.setSpacing(5)
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setContentsMargins(40, -1, 40, 20)
        self.MenuLayout = QHBoxLayout()
        self.MenuLayout.setSpacing(4)
        self.MenuLayout.setObjectName(u"MenuLayout")
        self.MenuLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.Select = QPushButton(self.centralwidget)
        self.Select.setObjectName(u"Select")

        self.MenuLayout.addWidget(self.Select)

        self.horizontalSpacer_2 = QSpacerItem(
            98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MenuLayout.addItem(self.horizontalSpacer_2)

        self.label1 = QLabel(self.centralwidget)
        self.label1.setObjectName(u"label1")

        self.MenuLayout.addWidget(self.label1)

        self.MinSelect = QLineEdit(self.centralwidget)
        self.MinSelect.setObjectName(u"MInSelect")
        self.MinSelect.setMaximumSize(QSize(50, 16777215))

        self.MenuLayout.addWidget(self.MinSelect)

        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)

        self.MenuLayout.addWidget(self.label2)

        self.MaxSelect = QLineEdit(self.centralwidget)
        self.MaxSelect.setObjectName(u"MaxSelect")
        self.MaxSelect.setMaximumSize(QSize(50, 16777215))

        self.MenuLayout.addWidget(self.MaxSelect)

        self.Button = QPushButton(self.centralwidget)
        self.Button.setObjectName(u"Button")
        self.Button.setMinimumSize(QSize(100, 0))

        self.MenuLayout.addWidget(self.Button)

        self.horizontalSpacer_3 = QSpacerItem(
            148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.MenuLayout.addItem(self.horizontalSpacer_3)

        self.MainLayout.addLayout(self.MenuLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.MainLayout.addWidget(self.line)

        self.BankLayout = QVBoxLayout()
        self.BankLayout.setObjectName(u"BankLayout")
        self.label_0 = QLabel(self.centralwidget)
        self.label_0.setObjectName(u"label_0")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(12)
        self.label_0.setFont(font1)
        self.label_0.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_0.setWordWrap(True)

        self.BankLayout.addWidget(self.label_0)

        self.line_1 = QFrame(self.centralwidget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.BankLayout.addWidget(self.line_1)

        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font1)
        self.label_1.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_1.setWordWrap(True)

        self.BankLayout.addWidget(self.label_1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.BankLayout.addWidget(self.line_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_2.setWordWrap(True)

        self.BankLayout.addWidget(self.label_2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.BankLayout.addWidget(self.line_3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_3.setWordWrap(True)

        self.BankLayout.addWidget(self.label_3)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.BankLayout.addWidget(self.line_4)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_4.setWordWrap(True)

        self.BankLayout.addWidget(self.label_4)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.BankLayout.addWidget(self.line_5)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_5.setWordWrap(True)

        self.BankLayout.addWidget(self.label_5)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.BankLayout.addWidget(self.line_6)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_6.setWordWrap(True)

        self.BankLayout.addWidget(self.label_6)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.BankLayout.addWidget(self.line_7)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_7.setWordWrap(True)

        self.BankLayout.addWidget(self.label_7)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.BankLayout.addWidget(self.line_8)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_8.setWordWrap(True)

        self.BankLayout.addWidget(self.label_8)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.BankLayout.addWidget(self.line_9)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_9.setWordWrap(True)

        self.BankLayout.addWidget(self.label_9)

        self.MainLayout.addLayout(self.BankLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.MinSelect, self.MaxSelect)
        QWidget.setTabOrder(self.MaxSelect, self.Button)
        QWidget.setTabOrder(self.Button, self.Select)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.setupUi_()  # setupUI的补充

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.Select.setText(QCoreApplication.translate(
            "MainWindow", u"\u9009\u62e9", None))
        self.label1.setText(QCoreApplication.translate(
            "MainWindow", u"\u9898\u76ee\u8303\u56f4\uff1a", None))
        self.MinSelect.setText(
            QCoreApplication.translate("MainWindow", u"1", None))
        self.label2.setText(QCoreApplication.translate(
            "MainWindow", u"\u2014", None))
        self.MaxSelect.setText(
            QCoreApplication.translate("MainWindow", u"300", None))
        self.Button.setText(QCoreApplication.translate(
            "MainWindow", u"\u62bd\u9898", None))
        self.label_0.setText(QCoreApplication.translate(
            "MainWindow", u"1\u3001", None))
        self.label_1.setText(QCoreApplication.translate(
            "MainWindow", u"2\u3001", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"3\u3001", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"4\u3001", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"5\u3001", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"6\u3001", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"7\u3001", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"8\u3001", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"9\u3001", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"10\u3001", None))
    # retranslateUi

    # --------------------------------------------------------------------

    def setupUi_(self):
        # Set constant
        self.LABEL_N = {0: self.label_0,
                        1: self.label_1,
                        2: self.label_2,
                        3: self.label_3,
                        4: self.label_4,
                        5: self.label_5,
                        6: self.label_6,
                        7: self.label_7,
                        8: self.label_8,
                        9: self.label_9}
        self.QUESTIONS = [i for i in range(1, 11)]

        self.FILE = "./货运组理论试题.xls"
        if os.access(self.FILE, os.F_OK) == False:
            self.selectFile()

        # Action
        self.Select.clicked.connect(self.selectFile)
        self.Button.clicked.connect(self.cilckButton)
        for i in self.LABEL_N:
            _label = self.LABEL_N[i]
            _label.installEventFilter(self)  # 安装事件过滤器

        # Filter
        _regex = QRegExp("^[0-9]*[1-9][0-9]*$")  # 正则表达式：正整数
        _validator = QRegExpValidator(_regex)
        self.MinSelect.setValidator(_validator)
        self.MaxSelect.setValidator(_validator)

    # opstion----------------------------------

    def selectFile(self):
        # 选择文件
        self.FILE = QFileDialog.getOpenFileName(
            caption="打开execl格式题库", filter="Execl files(*.xls;*.xlsx)")

    def cilckButton(self):
        # 抽题号
        MIN = int(self.MinSelect.text())
        MAX = int(self.MaxSelect.text())
        MAX += 1
        if MAX - MIN <= 9:
            return
        self.QUESTIONS = sample(range(MIN, MAX, 1), 10)
        self.readExecl()

    def readExecl(self):
        # 读取execl
        wb = xlrd.open_workbook(self.FILE)
        sheet = wb.sheet_by_index(0)
        for i in range(0, 10):
            text = sheet.cell(self.QUESTIONS[i]-1, 1).value
            ANSWER = sheet.cell(self.QUESTIONS[i]-1, 2).value
            TIME = sheet.cell(self.QUESTIONS[i]-1, 5).value
            self.setLabel(i, text, ANSWER, TIME)

    def setLabel(self, i, text, ANSWER, TIME):
        # 设置label
        _label = self.LABEL_N[i]
        _label.setText(text)
        _label.ANSWER = ANSWER
        _label.TIME = TIME

    def callDialog(self, question, ANSWER, TIME):
        # 打开答案窗口
        dialog = Ui_Dialog()
        dialogWindow = QDialog()
        dialog.setupUi(dialogWindow)
        dialog.setupUi_(question, ANSWER, TIME)
        dialogWindow.exec_()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            self.callDialog(obj.text(), obj.ANSWER, obj.TIME)
            return True
        else:
            return False


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
