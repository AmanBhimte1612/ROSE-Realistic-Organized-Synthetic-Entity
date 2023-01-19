# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pathywzkTU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_PMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Background = QFrame(self.centralwidget)
        self.Background.setObjectName(u"Background")
        sizePolicy.setHeightForWidth(self.Background.sizePolicy().hasHeightForWidth())
        self.Background.setSizePolicy(sizePolicy)
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
        self.horizontalLayout_2.setContentsMargins(8, 5, 8, 3)
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

        self.label_5 = QLabel(self.Header)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:rgb(40,60,80)")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

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
        self.minimize_window_button.setIconSize(QSize(40, 30))

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
        self.close_windowbutton.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.close_windowbutton)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.Header)

        self.Main = QFrame(self.Background)
        self.Main.setObjectName(u"Main")
        sizePolicy.setHeightForWidth(self.Main.sizePolicy().hasHeightForWidth())
        self.Main.setSizePolicy(sizePolicy)
        self.Main.setStyleSheet(u"\n"
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"background-color:rgb(204,229,255)")
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Main)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.side_container = QFrame(self.Main)
        self.side_container.setObjectName(u"side_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_container.sizePolicy().hasHeightForWidth())
        self.side_container.setSizePolicy(sizePolicy1)
        self.side_container.setMinimumSize(QSize(0, 0))
        self.side_container.setMaximumSize(QSize(0, 16777215))
        self.side_container.setAutoFillBackground(False)
        self.side_container.setStyleSheet(u"")
        self.side_container.setFrameShape(QFrame.StyledPanel)
        self.side_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.side_container)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(8, 0, 8, 0)
        self.side_1 = QFrame(self.side_container)
        self.side_1.setObjectName(u"side_1")
        self.side_1.setMinimumSize(QSize(300, 0))
        self.side_1.setMaximumSize(QSize(150, 16777215))
        self.side_1.setFrameShape(QFrame.StyledPanel)
        self.side_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.side_1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 160))
        self.frame_9.setStyleSheet(u"\n"
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
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 8, 0)
        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 80))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 111, 31))
        self.label_2.setFont(font)
        self.f_name_input = QLineEdit(self.frame_16)
        self.f_name_input.setObjectName(u"f_name_input")
        self.f_name_input.setGeometry(QRect(0, 30, 291, 41))
        self.f_name_input.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 80))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 121, 31))
        self.label_3.setFont(font)
        self.l_name_input = QLineEdit(self.frame_13)
        self.l_name_input.setObjectName(u"l_name_input")
        self.l_name_input.setGeometry(QRect(0, 30, 291, 41))
        self.l_name_input.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.frame_13)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.side_1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border-bottom-left-radius: 15px;\n"
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
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_11)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border-bottom-left-radius: 15px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, -1)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 200))
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
        font2 = QFont()
        font2.setPointSize(12)
        self.Submit_btn.setFont(font2)
        self.Submit_btn.setStyleSheet(u"background-color:rgb(102,178,255);")
        self.update_btn = QPushButton(self.frame_4)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(0, 40, 141, 31))
        self.update_btn.setFont(font2)
        self.update_btn.setStyleSheet(u"background-color:rgb(102,178,255);")

        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 400))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_12)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_11)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(150, 16777215))
        self.frame_6.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgba(0, 85, 127, 130);\n"
"	border:none;\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 80))
        self.frame_10.setStyleSheet(u"\n"
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
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.lineEdit = QLineEdit(self.frame_10)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_8.addWidget(self.lineEdit)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(143, 192, 255);\n"
"    border-radius:12px;\n"
"    padding: 4px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid black;\n"
"   font: bold\n"
"\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.search_btn = QPushButton(self.frame_7)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setFont(font)
        self.search_btn.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.search_btn)

        self.view_btn = QPushButton(self.frame_7)
        self.view_btn.setObjectName(u"view_btn")
        self.view_btn.setFont(font)
        self.view_btn.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.view_btn)

        self.reset_btn = QPushButton(self.frame_7)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setFont(font)
        self.reset_btn.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.reset_btn)

        self.delete_btn = QPushButton(self.frame_7)
        self.delete_btn.setObjectName(u"delete_btn")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.delete_btn.setFont(font3)
        self.delete_btn.setStyleSheet(u"")
        self.delete_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.delete_btn)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.horizontalLayout_8.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_11)


        self.horizontalLayout_7.addWidget(self.side_1)


        self.horizontalLayout_6.addWidget(self.side_container)

        self.maintable = QFrame(self.Main)
        self.maintable.setObjectName(u"maintable")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.maintable.sizePolicy().hasHeightForWidth())
        self.maintable.setSizePolicy(sizePolicy2)
        self.maintable.setMaximumSize(QSize(16777215, 16777215))
        self.maintable.setStyleSheet(u"background-color:rgb(204,229,255)")
        self.maintable.setLocale(QLocale(QLocale.English, QLocale.India))
        self.maintable.setFrameShape(QFrame.StyledPanel)
        self.maintable.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.maintable)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 8, 8)
        self.label = QLabel(self.maintable)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 28))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:rgb(40,60,80)")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.frame_2 = QFrame(self.maintable)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.frame_2)

        self.tableWidget = QTableWidget(self.maintable)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color:rgb(255,255,255);")
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)

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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SAM(Beta)", None))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.Submit_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.view_btn.setText(QCoreApplication.translate("MainWindow", u"View all", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.delete_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Path Manager", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Path", None));
    # retranslateUi

