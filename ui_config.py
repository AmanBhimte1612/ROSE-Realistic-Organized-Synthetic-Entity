# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configaGIIVO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cicons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(501, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"background-color:rgb(204,229,255);\n"
"    border-radius:15px;\n"
"    padding: 4px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.frame_2)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 40))
        self.header_frame.setMaximumSize(QSize(16777215, 45))
        self.header_frame.setStyleSheet(u"background-color:rgba(000,000,000,000);\n"
"")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.header_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 0, 6, 0)
        self.frame_10 = QFrame(self.header_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color:rgb(255,255,255);    \n"
"border-radius:15px;\n"
"    padding: 4px;\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)

        self.verticalLayout_14.addWidget(self.label_7)


        self.horizontalLayout_3.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(202,240,248);\n"
"	border:none;\n"
"}\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame_12)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon = QIcon()
        icon.addFile(u":/icon/icons/mini2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon)
        self.minimize_window_button.setIconSize(QSize(25, 30))

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame_12)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon1)
        self.restore_window_button.setIconSize(QSize(25, 40))

        self.horizontalLayout_4.addWidget(self.restore_window_button, 0, Qt.AlignRight|Qt.AlignTop)

        self.close_windowbutton = QPushButton(self.frame_12)
        self.close_windowbutton.setObjectName(u"close_windowbutton")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_windowbutton.setIcon(icon2)
        self.close_windowbutton.setIconSize(QSize(25, 30))

        self.horizontalLayout_4.addWidget(self.close_windowbutton, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.frame_12, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.header_frame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 200))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(300, 16777215))
        self.frame_6.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 6)
        self.frame_17 = QFrame(self.frame_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 100))
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame_17)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)

        self.verticalLayout_11.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignTop)

        self.full_name = QLineEdit(self.frame_17)
        self.full_name.setObjectName(u"full_name")
        self.full_name.setMaximumSize(QSize(16777215, 40))
        self.full_name.setFont(font)
        self.full_name.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"	background-color:rgb(223,239,255);\n"
"    border-radius:10px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color:rgb(202,240,248);\n"
"    border: 1px solid black\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_11.addWidget(self.full_name)


        self.verticalLayout_5.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 100))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_18)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_6, 0, Qt.AlignLeft|Qt.AlignTop)

        self.nick_name = QLineEdit(self.frame_18)
        self.nick_name.setObjectName(u"nick_name")
        self.nick_name.setMaximumSize(QSize(16777215, 40))
        self.nick_name.setFont(font)
        self.nick_name.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"	background-color:rgb(223,239,255);\n"
"    border-radius:10px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color:rgb(202,240,248);\n"
"    border: 1px solid black\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_10.addWidget(self.nick_name)


        self.verticalLayout_5.addWidget(self.frame_18)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(250, 16777215))
        self.frame_8.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 10, -1, 20)
        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_2.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_5.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_5, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.frame_16, 0, Qt.AlignTop)

        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 500))
        self.frame_15.setStyleSheet(u"QRadioButton:hover{\n"
"	background-color:rgb(202,240,248);\n"
"  \n"
"\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.male_btn = QRadioButton(self.frame_15)
        self.male_btn.setObjectName(u"male_btn")
        self.male_btn.setFont(font3)

        self.verticalLayout_9.addWidget(self.male_btn)

        self.female_btn = QRadioButton(self.frame_15)
        self.female_btn.setObjectName(u"female_btn")
        self.female_btn.setFont(font3)

        self.verticalLayout_9.addWidget(self.female_btn)

        self.nick_btn = QRadioButton(self.frame_15)
        self.nick_btn.setObjectName(u"nick_btn")
        self.nick_btn.setFont(font3)

        self.verticalLayout_9.addWidget(self.nick_btn)


        self.verticalLayout_6.addWidget(self.frame_15, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(200, 16777215))
        self.frame_9.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 10, -1, 10)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.contact_no = QLineEdit(self.frame_9)
        self.contact_no.setObjectName(u"contact_no")
        self.contact_no.setMaximumSize(QSize(16777215, 40))
        self.contact_no.setFont(font)
        self.contact_no.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"	background-color:rgb(223,239,255);\n"
"    border-radius:10px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color:rgb(202,240,248);\n"
"    border: 1px solid black\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.contact_no)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(300, 16777215))
        self.frame_11.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_11)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_23)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_23)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_4)

        self.E_mail = QLineEdit(self.frame_23)
        self.E_mail.setObjectName(u"E_mail")
        self.E_mail.setMaximumSize(QSize(16777215, 40))
        self.E_mail.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color:rgb(223,239,255);\n"
"    border-radius:10px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color:rgb(202,240,248);\n"
"    border: 1px solid black\n"
"\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.E_mail)


        self.verticalLayout_8.addWidget(self.frame_23)

        self.frame_7 = QFrame(self.frame_11)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_8)

        self.password = QLineEdit(self.frame_7)
        self.password.setObjectName(u"password")
        self.password.setMaximumSize(QSize(16777215, 40))
        self.password.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color:rgb(223,239,255);\n"
"    border-radius:10px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	background-color:rgb(202,240,248);\n"
"    border: 1px solid black\n"
"\n"
"}\n"
"")

        self.verticalLayout_16.addWidget(self.password)


        self.verticalLayout_8.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_11)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 125))
        self.frame_5.setStyleSheet(u"background-color:rgb(204,229,255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 40))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_22)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(223,239,255);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(143, 192, 255);\n"
"\n"
"}\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(12, 0, 12, 0)
        self.ok_btn = QPushButton(self.frame_24)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setMinimumSize(QSize(70, 30))
        self.ok_btn.setMaximumSize(QSize(70, 30))
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.ok_btn.setFont(font4)
        self.ok_btn.setStyleSheet(u"\n"
"border: 1px solid black")
        self.ok_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.ok_btn, 0, Qt.AlignLeft)

        self.apply_btn = QPushButton(self.frame_24)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setMinimumSize(QSize(70, 30))
        self.apply_btn.setMaximumSize(QSize(70, 30))
        self.apply_btn.setFont(font4)
        self.apply_btn.setStyleSheet(u"\n"
"border: 1px solid black")
        self.apply_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.apply_btn)

        self.cancel_btn = QPushButton(self.frame_24)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(70, 30))
        self.cancel_btn.setMaximumSize(QSize(70, 30))
        self.cancel_btn.setFont(font4)
        self.cancel_btn.setStyleSheet(u"\n"
"border: 1px solid black")
        self.cancel_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.cancel_btn, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.frame_24, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 40))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_21)


        self.verticalLayout_12.addWidget(self.frame_19)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_windowbutton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nick Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"(to be called by)", None))
        self.male_btn.setText(QCoreApplication.translate("MainWindow", u"Male (Sir)", None))
        self.female_btn.setText(QCoreApplication.translate("MainWindow", u"Female (Mam)", None))
        self.nick_btn.setText(QCoreApplication.translate("MainWindow", u"Prefered nick name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contact No", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.ok_btn.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

