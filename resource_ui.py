# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resource.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 617)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.widget_3)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.change_btn = QPushButton(self.header_widget)
        self.change_btn.setObjectName(u"change_btn")
        icon = QIcon()
        icon.addFile(u":/icon/icon/activity-feed-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.change_btn.setIcon(icon)
        self.change_btn.setIconSize(QSize(14, 14))
        self.change_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.change_btn)

        self.horizontalSpacer = QSpacerItem(216, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_input = QLineEdit(self.header_widget)
        self.search_input.setObjectName(u"search_input")

        self.horizontalLayout.addWidget(self.search_input)

        self.search_btn = QPushButton(self.header_widget)
        self.search_btn.setObjectName(u"search_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/search-13-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QSize(14, 14))

        self.horizontalLayout.addWidget(self.search_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(216, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.user_btn = QPushButton(self.header_widget)
        self.user_btn.setObjectName(u"user_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/user-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon2)
        self.user_btn.setIconSize(QSize(14, 14))

        self.horizontalLayout_4.addWidget(self.user_btn)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(26)
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_8 = QGridLayout(self.page_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_7 = QGridLayout(self.page_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_6 = QGridLayout(self.page_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.search_label_9 = QLabel(self.page_6)
        self.search_label_9.setObjectName(u"search_label_9")
        self.search_label_9.setFont(font1)

        self.gridLayout_6.addWidget(self.search_label_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_5 = QGridLayout(self.page_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = QLabel(self.page_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_label_1 = QLabel(self.icon_only_widget)
        self.logo_label_1.setObjectName(u"logo_label_1")
        self.logo_label_1.setMinimumSize(QSize(50, 50))
        self.logo_label_1.setMaximumSize(QSize(50, 50))
        font2 = QFont()
        font2.setPointSize(14)
        self.logo_label_1.setFont(font2)
        self.logo_label_1.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_label_1.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_label_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_btn_1 = QPushButton(self.icon_only_widget)
        self.home_btn_1.setObjectName(u"home_btn_1")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon/icon/home-4-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.home_btn_1.setIcon(icon3)
        self.home_btn_1.setIconSize(QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_btn_1)

        self.dashboard_btn_1 = QPushButton(self.icon_only_widget)
        self.dashboard_btn_1.setObjectName(u"dashboard_btn_1")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/dashboard-5-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icon/icon/dashboard-5-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_btn_1.setIcon(icon4)
        self.dashboard_btn_1.setIconSize(QSize(20, 20))
        self.dashboard_btn_1.setCheckable(True)
        self.dashboard_btn_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_btn_1)

        self.others_btn_1 = QPushButton(self.icon_only_widget)
        self.others_btn_1.setObjectName(u"others_btn_1")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/activity-feed-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icon/icon/activity-feed-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.others_btn_1.setIcon(icon5)
        self.others_btn_1.setIconSize(QSize(20, 20))
        self.others_btn_1.setCheckable(True)
        self.others_btn_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.others_btn_1)

        self.products_btn_1 = QPushButton(self.icon_only_widget)
        self.products_btn_1.setObjectName(u"products_btn_1")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/product-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icon/icon/product-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.products_btn_1.setIcon(icon6)
        self.products_btn_1.setIconSize(QSize(20, 20))
        self.products_btn_1.setCheckable(True)
        self.products_btn_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.products_btn_1)

        self.customers_btn_1 = QPushButton(self.icon_only_widget)
        self.customers_btn_1.setObjectName(u"customers_btn_1")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/group-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icon/icon/group-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.customers_btn_1.setIcon(icon7)
        self.customers_btn_1.setIconSize(QSize(20, 20))
        self.customers_btn_1.setCheckable(True)
        self.customers_btn_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.customers_btn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_btn_1 = QPushButton(self.icon_only_widget)
        self.exit_btn_1.setObjectName(u"exit_btn_1")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/close-window-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn_1.setIcon(icon8)
        self.exit_btn_1.setIconSize(QSize(20, 20))
        self.exit_btn_1.setCheckable(True)
        self.exit_btn_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.exit_btn_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.logo_label_2 = QLabel(self.full_menu_widget)
        self.logo_label_2.setObjectName(u"logo_label_2")
        self.logo_label_2.setMinimumSize(QSize(40, 40))
        self.logo_label_2.setMaximumSize(QSize(40, 40))
        self.logo_label_2.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo_label_2)

        self.logo_label_3 = QLabel(self.full_menu_widget)
        self.logo_label_3.setObjectName(u"logo_label_3")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(15)
        self.logo_label_3.setFont(font3)

        self.horizontalLayout_3.addWidget(self.logo_label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_btn_2 = QPushButton(self.full_menu_widget)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setIcon(icon3)
        self.home_btn_2.setIconSize(QSize(14, 14))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_btn_2)

        self.dashboard_btn_2 = QPushButton(self.full_menu_widget)
        self.dashboard_btn_2.setObjectName(u"dashboard_btn_2")
        self.dashboard_btn_2.setIcon(icon4)
        self.dashboard_btn_2.setIconSize(QSize(14, 14))
        self.dashboard_btn_2.setCheckable(True)
        self.dashboard_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_btn_2)

        self.others_btn_2 = QPushButton(self.full_menu_widget)
        self.others_btn_2.setObjectName(u"others_btn_2")
        self.others_btn_2.setIcon(icon5)
        self.others_btn_2.setIconSize(QSize(14, 14))
        self.others_btn_2.setCheckable(True)
        self.others_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.others_btn_2)

        self.products_btn_2 = QPushButton(self.full_menu_widget)
        self.products_btn_2.setObjectName(u"products_btn_2")
        self.products_btn_2.setIcon(icon6)
        self.products_btn_2.setIconSize(QSize(14, 14))
        self.products_btn_2.setCheckable(True)
        self.products_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.products_btn_2)

        self.customers_btn_2 = QPushButton(self.full_menu_widget)
        self.customers_btn_2.setObjectName(u"customers_btn_2")
        self.customers_btn_2.setIcon(icon7)
        self.customers_btn_2.setIconSize(QSize(14, 14))
        self.customers_btn_2.setCheckable(True)
        self.customers_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.customers_btn_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 413, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exit_btn_2 = QPushButton(self.full_menu_widget)
        self.exit_btn_2.setObjectName(u"exit_btn_2")
        self.exit_btn_2.setIcon(icon8)
        self.exit_btn_2.setIconSize(QSize(14, 14))
        self.exit_btn_2.setCheckable(True)
        self.exit_btn_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.exit_btn_2)


        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.home_btn_1.toggled.connect(self.home_btn_2.setChecked)
        self.dashboard_btn_1.toggled.connect(self.dashboard_btn_2.setChecked)
        self.others_btn_1.toggled.connect(self.others_btn_2.setChecked)
        self.products_btn_2.toggled.connect(self.products_btn_1.setChecked)
        self.products_btn_1.toggled.connect(self.products_btn_2.setChecked)
        self.customers_btn_1.toggled.connect(self.customers_btn_2.setChecked)
        self.home_btn_2.toggled.connect(self.home_btn_1.setChecked)
        self.dashboard_btn_2.toggled.connect(self.dashboard_btn_1.setChecked)
        self.others_btn_2.toggled.connect(self.others_btn_1.setChecked)
        self.customers_btn_2.toggled.connect(self.customers_btn_1.setChecked)
        self.change_btn.toggled.connect(self.icon_only_widget.setVisible)
        self.change_btn.toggled.connect(self.full_menu_widget.setHidden)
        self.exit_btn_2.clicked.connect(MainWindow.close)
        self.exit_btn_1.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.change_btn.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search....", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.user_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Others", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.search_label_9.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Userpage", None))
        self.logo_label_1.setText("")
        self.home_btn_1.setText("")
        self.dashboard_btn_1.setText("")
        self.others_btn_1.setText("")
        self.products_btn_1.setText("")
        self.customers_btn_1.setText("")
        self.exit_btn_1.setText("")
        self.logo_label_2.setText("")
        self.logo_label_3.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.home_btn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.dashboard_btn_2.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.others_btn_2.setText(QCoreApplication.translate("MainWindow", u"Others", None))
        self.products_btn_2.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.customers_btn_2.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.exit_btn_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

