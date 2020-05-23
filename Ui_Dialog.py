# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Dialog.ui'
##
# Created by: Qt User Interface Compiler version 5.14.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QSize, QTimer)
from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import (
    QVBoxLayout, QLabel, QHBoxLayout, QLCDNumber, QSizePolicy, QFrame)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(878, 528)
        icon = QIcon()
        icon.addFile("./aa.ico")
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.questionLable = QLabel(Dialog)
        self.questionLable.setObjectName(u"questionLable")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(12)
        self.questionLable.setFont(font)
        self.questionLable.setWordWrap(True)
        self.questionLable.setMargin(0)
        self.questionLable.setIndent(0)

        self.horizontalLayout.addWidget(self.questionLable)

        self.lcd = QLCDNumber(Dialog)
        self.lcd.setObjectName(u"lcd")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd.sizePolicy().hasHeightForWidth())
        self.lcd.setSizePolicy(sizePolicy)
        self.lcd.setMinimumSize(QSize(120, 60))
        self.lcd.setSmallDecimalPoint(True)
        self.lcd.setDigitCount(4)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setProperty("value", 120.000000000000000)

        self.horizontalLayout.addWidget(self.lcd)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.answerLable = QLabel(Dialog)
        self.answerLable.setObjectName(u"answerLable")
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI")
        font1.setPointSize(14)
        self.answerLable.setFont(font1)
        self.answerLable.setWordWrap(True)

        self.verticalLayout.addWidget(self.answerLable)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

    def setupUi_(self, question, answer, time):
        self.questionLable.setText(question)
        self.answerLable.setText(answer)
        self.lcd.setDigitCount(3)  # 设置lcd的显示位数
        self.lcd.display(time)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.setlcd1)
        self.timer1.start(1000)
        # self.timer2 = QTimer()
        # self.timer2.timeout.connect(self.setlcd2)

    def setlcd1(self):
        self.lcd.display(self.lcd.intValue() - 1)
        if self.lcd.intValue() == 0:
            self.timer1.stop()

            # self.lcd.setSegmentStyle(QLCDNumber.Flat)
            # self.lcd.setStyleSheet("color: red;")

            # self.timer2.start(1000)

    def setlcd2(self):
        self.lcd.display(self.lcd.intValue() + 1)
