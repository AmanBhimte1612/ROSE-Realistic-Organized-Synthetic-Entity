# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'samguiSNArKK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import picons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"*{\n"
"\n"
"   border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setStyleSheet(u"background-color:rgba(000,000,000,000);\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QFrame(self.centralwidget)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        sizePolicy.setHeightForWidth(self.slide_menu_container.sizePolicy().hasHeightForWidth())
        self.slide_menu_container.setSizePolicy(sizePolicy)
        self.slide_menu_container.setMaximumSize(QSize(0, 16777215))
        self.slide_menu_container.setStyleSheet(u"border-bottom-left-radius: 20px; border-bottom-right-radius: none;\n"
"border-top-left-radius: 20px; border-top-right-radius: none;\n"
"background-color:rgb(143, 192, 255);")
        self.slide_menu_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.slide_menu_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.sidemenu = QFrame(self.slide_menu_container)
        self.sidemenu.setObjectName(u"sidemenu")
        self.sidemenu.setMinimumSize(QSize(196, 0))
        self.sidemenu.setMaximumSize(QSize(16777215, 16777215))
        self.sidemenu.setFrameShape(QFrame.StyledPanel)
        self.sidemenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidemenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.sidemenu)
        self.top.setObjectName(u"top")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.top)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.top)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_2 = QLabel(self.top)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icon/icons/sam.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.top, 0, Qt.AlignTop)

        self.centor = QFrame(self.sidemenu)
        self.centor.setObjectName(u"centor")
        sizePolicy.setHeightForWidth(self.centor.sizePolicy().hasHeightForWidth())
        self.centor.setSizePolicy(sizePolicy)
        self.centor.setFrameShape(QFrame.StyledPanel)
        self.centor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.centor)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.centor)
        self.toolBox.setObjectName(u"toolBox")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setKerning(True)
        self.toolBox.setFont(font1)
        self.toolBox.setStyleSheet(u"\n"
"border-radius:15px;")
        self.customize = QWidget()
        self.customize.setObjectName(u"customize")
        self.customize.setGeometry(QRect(0, 0, 196, 443))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setWeight(50)
        self.customize.setFont(font2)
        self.verticalLayout_6 = QVBoxLayout(self.customize)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Buttons_1 = QFrame(self.customize)
        self.Buttons_1.setObjectName(u"Buttons_1")
        self.Buttons_1.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(204,229,255);\n"
" border-radius:25px;\n"
"    padding: 4px;\n"
"	border:none;\n"
"}\n"
"\n"
"")
        self.Buttons_1.setFrameShape(QFrame.StyledPanel)
        self.Buttons_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Buttons_1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 0, 9, 3)
        self.frame_15 = QFrame(self.Buttons_1)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 5, 9, 5)
        self.config_but = QPushButton(self.frame_15)
        self.config_but.setObjectName(u"config_but")
        self.config_but.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icon/icons/Profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.config_but.setIcon(icon)
        self.config_but.setIconSize(QSize(40, 50))

        self.verticalLayout_15.addWidget(self.config_but)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.frame_17 = QFrame(self.Buttons_1)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_17)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 5, 9, 9)
        self.cont_but = QPushButton(self.frame_17)
        self.cont_but.setObjectName(u"cont_but")
        self.cont_but.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/icons.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cont_but.setIcon(icon1)
        self.cont_but.setIconSize(QSize(40, 50))

        self.verticalLayout_14.addWidget(self.cont_but)


        self.verticalLayout_8.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.Buttons_1)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_18)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 5, 9, 5)
        self.path_but = QPushButton(self.frame_18)
        self.path_but.setObjectName(u"path_but")
        self.path_but.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/FILE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.path_but.setIcon(icon2)
        self.path_but.setIconSize(QSize(40, 50))

        self.verticalLayout_16.addWidget(self.path_but)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.frame_16 = QFrame(self.Buttons_1)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(9, 5, 9, 5)
        self.ran_but = QPushButton(self.frame_16)
        self.ran_but.setObjectName(u"ran_but")
        self.ran_but.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ran_but.setIcon(icon3)
        self.ran_but.setIconSize(QSize(40, 50))

        self.verticalLayout_17.addWidget(self.ran_but)


        self.verticalLayout_8.addWidget(self.frame_16)


        self.verticalLayout_6.addWidget(self.Buttons_1)

        self.discri_1 = QFrame(self.customize)
        self.discri_1.setObjectName(u"discri_1")
        self.discri_1.setMaximumSize(QSize(16777215, 300))
        self.discri_1.setStyleSheet(u"background-color:rgb(143, 192, 255);\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"")
        self.discri_1.setFrameShape(QFrame.StyledPanel)
        self.discri_1.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.discri_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 181, 191))
        self.label_6.setStyleSheet(u"background-color:rgb(204,229,255);\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"")

        self.verticalLayout_6.addWidget(self.discri_1)

        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.customize, icon4, u"Customize")
        self.contact_us = QWidget()
        self.contact_us.setObjectName(u"contact_us")
        self.contact_us.setGeometry(QRect(0, 0, 196, 443))
        self.verticalLayout_5 = QVBoxLayout(self.contact_us)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Buttons_2 = QFrame(self.contact_us)
        self.Buttons_2.setObjectName(u"Buttons_2")
        self.Buttons_2.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(204,229,255);\n"
" border-radius:25px;\n"
"    padding: 4px;\n"
"	border:none;\n"
"}\n"
"")
        self.Buttons_2.setFrameShape(QFrame.StyledPanel)
        self.Buttons_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Buttons_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 0, 9, 0)
        self.Insta_but = QFrame(self.Buttons_2)
        self.Insta_but.setObjectName(u"Insta_but")
        self.Insta_but.setStyleSheet(u"")
        self.Insta_but.setFrameShape(QFrame.StyledPanel)
        self.Insta_but.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Insta_but)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.instagram_btn = QPushButton(self.Insta_but)
        self.instagram_btn.setObjectName(u"instagram_btn")
        self.instagram_btn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/icons8-instagram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.instagram_btn.setIcon(icon5)
        self.instagram_btn.setIconSize(QSize(50, 50))

        self.verticalLayout_10.addWidget(self.instagram_btn)


        self.verticalLayout_7.addWidget(self.Insta_but)

        self.face_but = QFrame(self.Buttons_2)
        self.face_but.setObjectName(u"face_but")
        self.face_but.setStyleSheet(u"")
        self.face_but.setFrameShape(QFrame.StyledPanel)
        self.face_but.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.face_but)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.facebook_btn = QPushButton(self.face_but)
        self.facebook_btn.setObjectName(u"facebook_btn")
        self.facebook_btn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/icons8-facebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.facebook_btn.setIcon(icon6)
        self.facebook_btn.setIconSize(QSize(55, 55))

        self.verticalLayout_9.addWidget(self.facebook_btn)


        self.verticalLayout_7.addWidget(self.face_but)

        self.mail_but = QFrame(self.Buttons_2)
        self.mail_but.setObjectName(u"mail_but")
        self.mail_but.setStyleSheet(u"")
        self.mail_but.setFrameShape(QFrame.StyledPanel)
        self.mail_but.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.mail_but)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.mail_btn = QPushButton(self.mail_but)
        self.mail_btn.setObjectName(u"mail_btn")
        self.mail_btn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/mail.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mail_btn.setIcon(icon7)
        self.mail_btn.setIconSize(QSize(55, 55))
        self.mail_btn.setCheckable(False)

        self.verticalLayout_12.addWidget(self.mail_btn)


        self.verticalLayout_7.addWidget(self.mail_but)


        self.verticalLayout_5.addWidget(self.Buttons_2)

        self.discri_2 = QFrame(self.contact_us)
        self.discri_2.setObjectName(u"discri_2")
        self.discri_2.setStyleSheet(u"background-color:rgb(143, 192, 255);\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"")
        self.discri_2.setFrameShape(QFrame.StyledPanel)
        self.discri_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.discri_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_5 = QLabel(self.discri_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color:rgb(204,229,255);\n"
"    border-radius: 8px;\n"
"   \n"
"")

        self.verticalLayout_13.addWidget(self.label_5)


        self.verticalLayout_5.addWidget(self.discri_2)

        self.toolBox.addItem(self.contact_us, icon4, u"Contact us")

        self.horizontalLayout_7.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.centor)

        self.bottom = QFrame(self.sidemenu)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMaximumSize(QSize(16777215, 100))
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bottom)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.bottom)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 1000))
        self.frame_11.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(204,229,255);\n"
"	border:none;\n"
"}\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.exit_button = QPushButton(self.frame_11)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy2)
        self.exit_button.setMaximumSize(QSize(100, 10000000))
        self.exit_button.setBaseSize(QSize(12, 12))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.exit_button.setFont(font3)
        self.exit_button.setStyleSheet(u"text-align: left;\n"
"border-radius:25px;\n"
"\n"
"border-radius:15px;")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon8)
        self.exit_button.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.exit_button)


        self.verticalLayout_3.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.bottom, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.sidemenu)


        self.horizontalLayout.addWidget(self.slide_menu_container)

        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        sizePolicy1.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy1)
        self.main.setStyleSheet(u"")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy3)
        self.header_frame.setMaximumSize(QSize(16777215, 600))
        self.header_frame.setStyleSheet(u"\n"
"border-top-left-radius: 15px; border-top-right-radius: 15px;\n"
"\n"
"background-color:rgb(143, 192, 255);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(202,240,248);\n"
"	border-radius:4px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.open_close_side_bar_btn = QPushButton(self.frame_2)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        self.open_close_side_bar_btn.setGeometry(QRect(10, 0, 31, 31))
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/opt2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon9)
        self.open_close_side_bar_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.header_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(202,240,248);\n"
"	border-radius:8px;\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.alert_but = QPushButton(self.frame_7)
        self.alert_but.setObjectName(u"alert_but")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/alert.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alert_but.setIcon(icon10)
        self.alert_but.setIconSize(QSize(35, 35))

        self.horizontalLayout_8.addWidget(self.alert_but, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.manual_but = QPushButton(self.frame_7)
        self.manual_but.setObjectName(u"manual_but")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/icons8-info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manual_but.setIcon(icon11)
        self.manual_but.setIconSize(QSize(35, 35))

        self.horizontalLayout_8.addWidget(self.manual_but, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame_7, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_8 = QFrame(self.header_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(202,240,248);\n"
"	border-radius:8px;\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame_8)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon12 = QIcon()
        icon12.addFile(u":/icon/icons/mini2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon12)
        self.minimize_window_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_5.addWidget(self.minimize_window_button, 0, Qt.AlignRight|Qt.AlignTop)

        self.restore_window_button = QPushButton(self.frame_8)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon13 = QIcon()
        icon13.addFile(u":/icon/icons/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon13)
        self.restore_window_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_5.addWidget(self.restore_window_button, 0, Qt.AlignRight|Qt.AlignTop)

        self.close_windowbutton = QPushButton(self.frame_8)
        self.close_windowbutton.setObjectName(u"close_windowbutton")
        icon14 = QIcon()
        icon14.addFile(u":/icon/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_windowbutton.setIcon(icon14)
        self.close_windowbutton.setIconSize(QSize(35, 35))

        self.horizontalLayout_5.addWidget(self.close_windowbutton, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_8, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.centre_main = QFrame(self.main)
        self.centre_main.setObjectName(u"centre_main")
        sizePolicy1.setHeightForWidth(self.centre_main.sizePolicy().hasHeightForWidth())
        self.centre_main.setSizePolicy(sizePolicy1)
        self.centre_main.setStyleSheet(u"\n"
"background-color:rgb(204,229,255);")
        self.centre_main.setFrameShape(QFrame.StyledPanel)
        self.centre_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.centre_main)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centre_main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 10)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(300, 295))
        self.frame_6.setStyleSheet(u"text-align:left;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-30, -10, 391, 421))
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(261, 421))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setStyleSheet(u"text-align:centre;")
        self.label_3.setPixmap(QPixmap(u":/icon/icons/char1.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_20.addWidget(self.frame_6)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy3)
        self.frame_12.setMaximumSize(QSize(16777215, 70))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_12)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(15, 0, 15, 0)
        self.frame_9 = QFrame(self.frame_12)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color:rgb(255, 144, 144);\n"
"    border-radius: 8px;\n"
"   \n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.sam_text = QTextBrowser(self.frame_9)
        self.sam_text.setObjectName(u"sam_text")
        self.sam_text.setStyleSheet(u"background-color:rgb(255, 221, 167);\n"
"font: 14pt \"Rockwell\";\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"")

        self.verticalLayout_22.addWidget(self.sam_text)


        self.verticalLayout_21.addWidget(self.frame_9)


        self.verticalLayout_20.addWidget(self.frame_12)


        self.verticalLayout_18.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.centre_main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 150))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet(u"background-image: url(D:\\project\\pro\\icons\\text)")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, 0, 20, 12)
        self.frame_14 = QFrame(self.frame_4)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.frame_14.setStyleSheet(u"background-color:rgb(255, 144, 144);\n"
"    border-radius: 8px;\n"
"   \n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_14)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.user_said_text = QTextBrowser(self.frame_14)
        self.user_said_text.setObjectName(u"user_said_text")
        self.user_said_text.setStyleSheet(u"background-color:rgb(255, 221, 167);\n"
"font: 14pt \"Rockwell\";\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"")

        self.verticalLayout_19.addWidget(self.user_said_text)


        self.horizontalLayout_10.addWidget(self.frame_14)


        self.verticalLayout_18.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.centre_main)

        self.footer = QFrame(self.main)
        self.footer.setObjectName(u"footer")
        sizePolicy3.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy3)
        self.footer.setStyleSheet(u"border-bottom-left-radius: 20px; border-bottom-right-radius:none;\n"
"\n"
"\n"
"\n"
"background-color:rgb(143, 192, 255);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(8, 0, 0, 0)
        self.frame = QFrame(self.footer)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setPointSize(10)
        self.label_4.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_4, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(202,240,248);\n"
"	border-radius:8px;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.run_btn = QPushButton(self.frame_5)
        self.run_btn.setObjectName(u"run_btn")
        icon15 = QIcon()
        icon15.addFile(u":/icon/icons/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.run_btn.setIcon(icon15)
        self.run_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.run_btn, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.termi_btn = QPushButton(self.frame_5)
        self.termi_btn.setObjectName(u"termi_btn")
        icon16 = QIcon()
        icon16.addFile(u":/icon/icons/terminate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.termi_btn.setIcon(icon16)
        self.termi_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.termi_btn)


        self.horizontalLayout_3.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SAM", None))
        self.label_2.setText("")
        self.config_but.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.cont_but.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.path_but.setText(QCoreApplication.translate("MainWindow", u"Path manager", None))
        self.ran_but.setText(QCoreApplication.translate("MainWindow", u"random", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.customize), QCoreApplication.translate("MainWindow", u"Customize", None))
        self.instagram_btn.setText(QCoreApplication.translate("MainWindow", u"Instagram", None))
        self.facebook_btn.setText(QCoreApplication.translate("MainWindow", u"FaceBook", None))
        self.mail_btn.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Description ", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.contact_us), QCoreApplication.translate("MainWindow", u"Contact us", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.open_close_side_bar_btn.setText("")
        self.alert_but.setText("")
        self.manual_but.setText("")
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_windowbutton.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SAM (Beta) 1.0", None))
        self.run_btn.setText("")
        self.termi_btn.setText("")
    # retranslateUi

