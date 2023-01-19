# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CONTEqGvQh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_CMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(736, 499)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Background = QFrame(self.centralwidget)
        self.Background.setObjectName(u"Background")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Background.sizePolicy().hasHeightForWidth())
        self.Background.setSizePolicy(sizePolicy1)
        self.Background.setStyleSheet(u"")
        self.Background.setFrameShape(QFrame.StyledPanel)
        self.Background.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Background)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.Background)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 35))
        self.Header.setStyleSheet(u"*{\n"
"	background-color:rgb(143, 192, 255);\n"
"	\n"
"   border-top-left-radius: 15px;border-top-right-radius: 15px;\n"
"}\n"
"\n"
"")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.frame_3 = QFrame(self.Header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(202,240,248);\n"
"	border-radius:8px;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.frame_3)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        self.open_close_side_bar_btn.setMinimumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/icons/icons/OPT_ADD.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.open_close_side_bar_btn)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.label = QLabel(self.Header)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 28))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:rgb(40,60,80)")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.frame = QFrame(self.Header)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(202,240,248);\n"
"	border-radius:8px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/mini2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMinimumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.restore_window_button)

        self.close_windowbutton = QPushButton(self.frame)
        self.close_windowbutton.setObjectName(u"close_windowbutton")
        self.close_windowbutton.setEnabled(True)
        self.close_windowbutton.setMinimumSize(QSize(28, 28))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_windowbutton.setIcon(icon3)
        self.close_windowbutton.setIconSize(QSize(35, 35))

        self.horizontalLayout_3.addWidget(self.close_windowbutton)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.Header)

        self.Main = QFrame(self.Background)
        self.Main.setObjectName(u"Main")
        sizePolicy1.setHeightForWidth(self.Main.sizePolicy().hasHeightForWidth())
        self.Main.setSizePolicy(sizePolicy1)
        self.Main.setStyleSheet(u"\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"background-color:rgb(204,229,255)")
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Main)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.side_container = QFrame(self.Main)
        self.side_container.setObjectName(u"side_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.side_container.sizePolicy().hasHeightForWidth())
        self.side_container.setSizePolicy(sizePolicy2)
        self.side_container.setMinimumSize(QSize(0, 0))
        self.side_container.setMaximumSize(QSize(0, 16777215))
        font2 = QFont()
        font2.setPointSize(9)
        self.side_container.setFont(font2)
        self.side_container.setAutoFillBackground(False)
        self.side_container.setStyleSheet(u"border-bottom-left-radius: 15px;")
        self.side_container.setFrameShape(QFrame.StyledPanel)
        self.side_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.side_container)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.side_1 = QFrame(self.side_container)
        self.side_1.setObjectName(u"side_1")
        self.side_1.setMinimumSize(QSize(150, 0))
        self.side_1.setMaximumSize(QSize(150, 16777215))
        self.side_1.setStyleSheet(u"\n"
"\n"
"background-color:rgb(204,229,255)")
        self.side_1.setFrameShape(QFrame.StyledPanel)
        self.side_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.side_1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 250))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);;\n"
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
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 71, 20))
        self.f_name_input = QLineEdit(self.frame_16)
        self.f_name_input.setObjectName(u"f_name_input")
        self.f_name_input.setGeometry(QRect(0, 20, 141, 31))
        self.f_name_input.setFont(font)
        self.f_name_input.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);\n"
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
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 81, 20))
        self.label_3.setFont(font)
        self.l_name_input = QLineEdit(self.frame_13)
        self.l_name_input.setObjectName(u"l_name_input")
        self.l_name_input.setGeometry(QRect(0, 20, 141, 31))
        self.l_name_input.setFont(font)
        self.l_name_input.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);\n"
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
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 81, 20))
        self.label_4.setFont(font)
        self.cont_input = QLineEdit(self.frame_14)
        self.cont_input.setObjectName(u"cont_input")
        self.cont_input.setGeometry(QRect(0, 20, 141, 31))
        self.cont_input.setFont(font)
        self.cont_input.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);;\n"
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
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 91, 21))
        self.label_5.setFont(font)
        self.mail_input = QLineEdit(self.frame_15)
        self.mail_input.setObjectName(u"mail_input")
        self.mail_input.setGeometry(QRect(0, 20, 141, 31))
        self.mail_input.setFont(font)
        self.mail_input.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.side_1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_11)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, -1, 141, 81))
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(102,178,255);\n"
"    border-radius:15px;\n"
"    padding: 4px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid black;\n"
"   font: bold\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.Submit_btn = QPushButton(self.frame_4)
        self.Submit_btn.setObjectName(u"Submit_btn")
        self.Submit_btn.setGeometry(QRect(0, 2, 141, 31))
        self.Submit_btn.setFont(font1)
        self.Submit_btn.setStyleSheet(u"background-color:rgb(102,178,255);")
        self.update_btn = QPushButton(self.frame_4)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(0, 40, 141, 31))
        self.update_btn.setFont(font1)
        self.update_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.frame_11)


        self.horizontalLayout_7.addWidget(self.side_1)

        self.side_3 = QFrame(self.side_container)
        self.side_3.setObjectName(u"side_3")
        self.side_3.setMinimumSize(QSize(150, 100))
        self.side_3.setStyleSheet(u"\n"
"background-color:rgb(204,229,255)")
        self.side_3.setFrameShape(QFrame.StyledPanel)
        self.side_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.side_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.side_2 = QFrame(self.side_3)
        self.side_2.setObjectName(u"side_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.side_2.sizePolicy().hasHeightForWidth())
        self.side_2.setSizePolicy(sizePolicy3)
        self.side_2.setMinimumSize(QSize(0, 0))
        self.side_2.setFrameShape(QFrame.StyledPanel)
        self.side_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.side_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 0, 10)
        self.frame_17 = QFrame(self.side_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 60))
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color:rgb(255,255,255);;\n"
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
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 141, 20))
        self.label_6.setFont(font)
        self.search_input = QLineEdit(self.frame_17)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setGeometry(QRect(0, 19, 141, 31))
        self.search_input.setFont(font)
        self.search_input.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.side_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(143, 192, 255);\n"
"    border-radius:15px;\n"
"    padding: 4px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid black;\n"
"   font: bold\n"
"\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.search_btn = QPushButton(self.frame_18)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(0, 10, 141, 31))
        self.search_btn.setFont(font1)
        self.search_btn.setStyleSheet(u"")
        self.view_btn = QPushButton(self.frame_18)
        self.view_btn.setObjectName(u"view_btn")
        self.view_btn.setGeometry(QRect(0, 50, 141, 31))
        self.view_btn.setFont(font1)
        self.view_btn.setStyleSheet(u"")
        self.reset_btn = QPushButton(self.frame_18)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(0, 92, 141, 31))
        self.reset_btn.setFont(font1)
        self.reset_btn.setStyleSheet(u"")
        self.delete_btn = QPushButton(self.frame_18)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(0, 132, 141, 31))
        self.delete_btn.setFont(font1)
        self.delete_btn.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.side_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 16777215))
        self.frame_19.setStyleSheet(u"\n"
"background-color:rgb(204,229,255)")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 141, 211))
        self.label_7.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"\n"
"border-radius: 8px;\n"
"")

        self.verticalLayout_5.addWidget(self.frame_19)


        self.verticalLayout_3.addWidget(self.side_2)


        self.horizontalLayout_7.addWidget(self.side_3)


        self.horizontalLayout_6.addWidget(self.side_container)

        self.maintable = QFrame(self.Main)
        self.maintable.setObjectName(u"maintable")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.maintable.sizePolicy().hasHeightForWidth())
        self.maintable.setSizePolicy(sizePolicy4)
        self.maintable.setMaximumSize(QSize(16777215, 16777215))
        self.maintable.setStyleSheet(u"\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"background-color:rgb(204,229,255)")
        self.maintable.setLocale(QLocale(QLocale.English, QLocale.India))
        self.maintable.setFrameShape(QFrame.StyledPanel)
        self.maintable.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.maintable)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(11, 0, 12, 12)
        self.tableWidget = QTableWidget(self.maintable)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Raised)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)

        self.verticalLayout_6.addWidget(self.tableWidget)


        self.horizontalLayout_6.addWidget(self.maintable)

        self.maintable.raise_()
        self.side_container.raise_()

        self.verticalLayout.addWidget(self.Main)


        self.horizontalLayout.addWidget(self.Background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Contact Manager", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
#if QT_CONFIG(tooltip)
        self.close_windowbutton.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This Button is temporarily disabled</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.close_windowbutton.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.close_windowbutton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"First Nmae", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.Submit_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SEARCH (By First Name)", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.view_btn.setText(QCoreApplication.translate("MainWindow", u"View all", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"FIRST NAME", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"LAST NAME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CONTACT", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"E-MAIL", None));
    # retranslateUi

