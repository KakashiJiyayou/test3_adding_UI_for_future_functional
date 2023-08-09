# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base_ui.ui'
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
        MainWindow.resize(856, 676)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
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
        font = QFont()
        font.setPointSize(14)
        self.logo_label_1.setFont(font)
        self.logo_label_1.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_label_1.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_label_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_btn_1 = QPushButton(self.icon_only_widget)
        self.home_btn_1.setObjectName(u"home_btn_1")
        icon = QIcon()
        icon.addFile(u":/icon/icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon/icon/home-4-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setIconSize(QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_btn_1)

        self.dashboard_btn_1 = QPushButton(self.icon_only_widget)
        self.dashboard_btn_1.setObjectName(u"dashboard_btn_1")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/dashboard-5-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/icon/dashboard-5-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_btn_1.setIcon(icon1)
        self.dashboard_btn_1.setIconSize(QSize(20, 20))
        self.dashboard_btn_1.setCheckable(True)
        self.dashboard_btn_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_btn_1)

        self.pushButton_3_change_password = QPushButton(self.icon_only_widget)
        self.pushButton_3_change_password.setObjectName(u"pushButton_3_change_password")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/group-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon/icon/group-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_3_change_password.setIcon(icon2)
        self.pushButton_3_change_password.setCheckable(True)
        self.pushButton_3_change_password.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_3_change_password)

        self.pushButton_2_genetate = QPushButton(self.icon_only_widget)
        self.pushButton_2_genetate.setObjectName(u"pushButton_2_genetate")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/edit-11-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon/icon/edit-11-49.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2_genetate.setIcon(icon3)
        self.pushButton_2_genetate.setCheckable(True)
        self.pushButton_2_genetate.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_2_genetate)

        self.pushButton_2_change_language = QPushButton(self.icon_only_widget)
        self.pushButton_2_change_language.setObjectName(u"pushButton_2_change_language")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/product-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icon/icon/product-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2_change_language.setIcon(icon4)
        self.pushButton_2_change_language.setCheckable(True)
        self.pushButton_2_change_language.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_2_change_language)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_btn_1 = QPushButton(self.icon_only_widget)
        self.exit_btn_1.setObjectName(u"exit_btn_1")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/close-window-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QSize(20, 20))
        self.exit_btn_1.setCheckable(True)
        self.exit_btn_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.exit_btn_1)


        self.gridLayout_5.addWidget(self.icon_only_widget, 0, 0, 1, 1)

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
        self.logo_label_2.setMinimumSize(QSize(50, 50))
        self.logo_label_2.setMaximumSize(QSize(40, 40))
        self.logo_label_2.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo_label_2)

        self.logo_label_3 = QLabel(self.full_menu_widget)
        self.logo_label_3.setObjectName(u"logo_label_3")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.logo_label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.logo_label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_btn_2 = QPushButton(self.full_menu_widget)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QSize(14, 14))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_btn_2)

        self.dashboard_btn_2 = QPushButton(self.full_menu_widget)
        self.dashboard_btn_2.setObjectName(u"dashboard_btn_2")
        self.dashboard_btn_2.setIcon(icon1)
        self.dashboard_btn_2.setIconSize(QSize(14, 14))
        self.dashboard_btn_2.setCheckable(True)
        self.dashboard_btn_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_btn_2)

        self.pushButton_2_change_password = QPushButton(self.full_menu_widget)
        self.pushButton_2_change_password.setObjectName(u"pushButton_2_change_password")
        self.pushButton_2_change_password.setIcon(icon2)
        self.pushButton_2_change_password.setCheckable(True)
        self.pushButton_2_change_password.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_2_change_password)

        self.pushButton_3_generate = QPushButton(self.full_menu_widget)
        self.pushButton_3_generate.setObjectName(u"pushButton_3_generate")
        self.pushButton_3_generate.setIcon(icon3)
        self.pushButton_3_generate.setCheckable(True)
        self.pushButton_3_generate.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_3_generate)

        self.pushButton_Change_lang = QPushButton(self.full_menu_widget)
        self.pushButton_Change_lang.setObjectName(u"pushButton_Change_lang")
        self.pushButton_Change_lang.setIcon(icon4)
        self.pushButton_Change_lang.setCheckable(True)
        self.pushButton_Change_lang.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_Change_lang)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 413, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exit_btn_2 = QPushButton(self.full_menu_widget)
        self.exit_btn_2.setObjectName(u"exit_btn_2")
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QSize(14, 14))
        self.exit_btn_2.setCheckable(True)
        self.exit_btn_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.exit_btn_2)


        self.gridLayout_5.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        self.vertical_Layout_6 = QVBoxLayout()
        self.vertical_Layout_6.setObjectName(u"vertical_Layout_6")
        self.header_widget_3 = QWidget(self.centralwidget)
        self.header_widget_3.setObjectName(u"header_widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.header_widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.header_widget_3)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.change_btn = QPushButton(self.header_widget)
        self.change_btn.setObjectName(u"change_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/activity-feed-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.change_btn.setIcon(icon6)
        self.change_btn.setIconSize(QSize(14, 14))
        self.change_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.change_btn)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_input = QLineEdit(self.header_widget)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(300, 0))
        self.search_input.setMaximumSize(QSize(99999, 16777215))
        self.search_input.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.search_input)

        self.search_btn = QPushButton(self.header_widget)
        self.search_btn.setObjectName(u"search_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/search-13-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon7)
        self.search_btn.setIconSize(QSize(14, 14))

        self.horizontalLayout.addWidget(self.search_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.user_btn = QPushButton(self.header_widget)
        self.user_btn.setObjectName(u"user_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/user-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon8)
        self.user_btn.setIconSize(QSize(14, 14))

        self.horizontalLayout_4.addWidget(self.user_btn)


        self.verticalLayout_5.addWidget(self.header_widget)


        self.vertical_Layout_6.addWidget(self.header_widget_3)

        self.page_stackedWidget = QStackedWidget(self.centralwidget)
        self.page_stackedWidget.setObjectName(u"page_stackedWidget")
        self.generate_page = QWidget()
        self.generate_page.setObjectName(u"generate_page")
        self.gridLayout_4 = QGridLayout(self.generate_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_for_scroll = QWidget(self.generate_page)
        self.widget_for_scroll.setObjectName(u"widget_for_scroll")
        self.widget_for_scroll.setMaximumSize(QSize(16777215, 150))
        self.gridLayout = QGridLayout(self.widget_for_scroll)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea_generate_page = QScrollArea(self.widget_for_scroll)
        self.scrollArea_generate_page.setObjectName(u"scrollArea_generate_page")
        self.scrollArea_generate_page.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 615, 130))
        self.scrollArea_generate_page.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea_generate_page, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_for_scroll, 0, 0, 1, 1)

        self.widget = QWidget(self.generate_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.widget.setMaximumSize(QSize(16777215, 300))
        self.gridLayout_7 = QGridLayout(self.widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.scrollArea_2 = QScrollArea(self.widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(200, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_checkbox = QWidget()
        self.scrollAreaWidgetContents_checkbox.setObjectName(u"scrollAreaWidgetContents_checkbox")
        self.scrollAreaWidgetContents_checkbox.setGeometry(QRect(0, 0, 260, 309))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_checkbox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollarea_checkbox_dirlist = QVBoxLayout()
        self.scrollarea_checkbox_dirlist.setSpacing(0)
        self.scrollarea_checkbox_dirlist.setObjectName(u"scrollarea_checkbox_dirlist")
        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox.setObjectName(u"checkBox")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox)

        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_5)

        self.checkBox_10 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_10)

        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_8)

        self.checkBox_9 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_9)

        self.checkBox_13 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_13)

        self.checkBox_14 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_14)

        self.checkBox_17 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_17)

        self.checkBox_12 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_12)

        self.checkBox_11 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_11)

        self.checkBox_16 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_16)

        self.checkBox_15 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_15)

        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_7)

        self.checkBox_6 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_6)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_4)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.scrollarea_checkbox_dirlist.addWidget(self.checkBox_2)


        self.gridLayout_3.addLayout(self.scrollarea_checkbox_dirlist, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_checkbox)

        self.horizontalLayout_12.addWidget(self.scrollArea_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.button_add_list_to_generate = QPushButton(self.widget)
        self.button_add_list_to_generate.setObjectName(u"button_add_list_to_generate")
        self.button_add_list_to_generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_add_list_to_generate.setLayoutDirection(Qt.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/arrow-8-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.button_add_list_to_generate.setIcon(icon9)
        self.button_add_list_to_generate.setIconSize(QSize(32, 32))
        self.button_add_list_to_generate.setFlat(True)

        self.verticalLayout_10.addWidget(self.button_add_list_to_generate)

        self.button_clear_list_to_generate = QPushButton(self.widget)
        self.button_clear_list_to_generate.setObjectName(u"button_clear_list_to_generate")
        self.button_clear_list_to_generate.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/x-mark-2-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.button_clear_list_to_generate.setIcon(icon10)
        self.button_clear_list_to_generate.setIconSize(QSize(32, 32))
        self.button_clear_list_to_generate.setFlat(True)

        self.verticalLayout_10.addWidget(self.button_clear_list_to_generate)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)


        self.horizontalLayout_12.addLayout(self.verticalLayout_10)

        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_12.addWidget(self.listWidget)


        self.gridLayout_7.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 2, 0, 1, 1)

        self.widget_upload = QWidget(self.generate_page)
        self.widget_upload.setObjectName(u"widget_upload")
        self.widget_upload.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_2 = QGridLayout(self.widget_upload)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.widget_upload)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget_upload)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(320, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.pushButton_generate_doc = QPushButton(self.widget_upload)
        self.pushButton_generate_doc.setObjectName(u"pushButton_generate_doc")
        self.pushButton_generate_doc.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_generate_doc, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget_upload, 3, 0, 1, 1)

        self.page_stackedWidget.addWidget(self.generate_page)
        self.download_page = QWidget()
        self.download_page.setObjectName(u"download_page")
        self.gridLayout_6 = QGridLayout(self.download_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.search_widget = QWidget(self.download_page)
        self.search_widget.setObjectName(u"search_widget")
        self.search_widget.setMinimumSize(QSize(0, 10))
        self.search_widget.setMaximumSize(QSize(16777215, 100))
        self.search_widget.setAutoFillBackground(False)
        self.search_widget.setStyleSheet(u"background-color:rgb(213, 246, 255)")
        self.horizontalLayout_7 = QHBoxLayout(self.search_widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_6.addWidget(self.search_widget, 0, 0, 1, 1)

        self.widget_upload_edit = QWidget(self.download_page)
        self.widget_upload_edit.setObjectName(u"widget_upload_edit")
        self.verticalLayout_8 = QVBoxLayout(self.widget_upload_edit)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_newDoc = QRadioButton(self.widget_upload_edit)
        self.radioButton_newDoc.setObjectName(u"radioButton_newDoc")

        self.horizontalLayout_9.addWidget(self.radioButton_newDoc)

        self.radioButton_addImage = QRadioButton(self.widget_upload_edit)
        self.radioButton_addImage.setObjectName(u"radioButton_addImage")
        self.radioButton_addImage.setEnabled(True)

        self.horizontalLayout_9.addWidget(self.radioButton_addImage)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_show = QLabel(self.widget_upload_edit)
        self.label_show.setObjectName(u"label_show")
        self.label_show.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_show)

        self.input_area = QLineEdit(self.widget_upload_edit)
        self.input_area.setObjectName(u"input_area")
        self.input_area.setFont(font2)

        self.horizontalLayout_6.addWidget(self.input_area)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)

        self.pushButton_upload = QPushButton(self.widget_upload_edit)
        self.pushButton_upload.setObjectName(u"pushButton_upload")
        font3 = QFont()
        font3.setFamily(u"Poppins")
        font3.setPointSize(14)
        self.pushButton_upload.setFont(font3)

        self.horizontalLayout_11.addWidget(self.pushButton_upload)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.gridLayout_6.addWidget(self.widget_upload_edit, 3, 0, 1, 1)

        self.widget_actions = QWidget(self.download_page)
        self.widget_actions.setObjectName(u"widget_actions")
        self.widget_actions.setMinimumSize(QSize(0, 30))
        self.widget_actions.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_actions)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_update = QPushButton(self.widget_actions)
        self.pushButton_update.setObjectName(u"pushButton_update")
        self.pushButton_update.setFont(font3)

        self.horizontalLayout_8.addWidget(self.pushButton_update)

        self.horizontalSpacer_5 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.pushButton_download = QPushButton(self.widget_actions)
        self.pushButton_download.setObjectName(u"pushButton_download")
        self.pushButton_download.setFont(font3)

        self.horizontalLayout_8.addWidget(self.pushButton_download)

        self.horizontalSpacer_6 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.pushButton_remove = QPushButton(self.widget_actions)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        self.pushButton_remove.setFont(font3)
        self.pushButton_remove.setStyleSheet(u"background-color:rgb(255, 79, 132)")

        self.horizontalLayout_8.addWidget(self.pushButton_remove)


        self.gridLayout_6.addWidget(self.widget_actions, 2, 0, 1, 1)

        self.show_result_widget = QWidget(self.download_page)
        self.show_result_widget.setObjectName(u"show_result_widget")
        self.verticalLayout_9 = QVBoxLayout(self.show_result_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.plainText_show = QPlainTextEdit(self.show_result_widget)
        self.plainText_show.setObjectName(u"plainText_show")

        self.verticalLayout_9.addWidget(self.plainText_show)

        self.progressBar = QProgressBar(self.show_result_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        font4 = QFont()
        font4.setPointSize(15)
        self.progressBar.setFont(font4)
        self.progressBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_9.addWidget(self.progressBar)


        self.gridLayout_6.addWidget(self.show_result_widget, 4, 0, 1, 1)

        self.widget_for_scroll_download_page = QWidget(self.download_page)
        self.widget_for_scroll_download_page.setObjectName(u"widget_for_scroll_download_page")
        self.widget_for_scroll_download_page.setMinimumSize(QSize(0, 150))
        self.widget_for_scroll_download_page.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_7 = QVBoxLayout(self.widget_for_scroll_download_page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2_edit_page = QScrollArea(self.widget_for_scroll_download_page)
        self.scrollArea_2_edit_page.setObjectName(u"scrollArea_2_edit_page")
        self.scrollArea_2_edit_page.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 633, 148))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_2_edit_page.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_7.addWidget(self.scrollArea_2_edit_page)


        self.gridLayout_6.addWidget(self.widget_for_scroll_download_page, 1, 0, 1, 1)

        self.page_stackedWidget.addWidget(self.download_page)

        self.vertical_Layout_6.addWidget(self.page_stackedWidget)


        self.gridLayout_5.addLayout(self.vertical_Layout_6, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.home_btn_1.toggled.connect(self.home_btn_2.setChecked)
        self.dashboard_btn_1.toggled.connect(self.dashboard_btn_2.setChecked)
        self.home_btn_2.toggled.connect(self.home_btn_1.setChecked)
        self.dashboard_btn_2.toggled.connect(self.dashboard_btn_1.setChecked)
        self.change_btn.toggled.connect(self.icon_only_widget.setVisible)
        self.change_btn.toggled.connect(self.full_menu_widget.setHidden)
        self.exit_btn_2.clicked.connect(MainWindow.close)
        self.exit_btn_1.clicked.connect(MainWindow.close)
        self.pushButton_2_change_language.clicked.connect(self.pushButton_Change_lang.toggle)
        self.pushButton_Change_lang.clicked.connect(self.pushButton_2_change_language.toggle)
        self.pushButton_3_change_password.toggled.connect(self.pushButton_2_change_password.setChecked)
        self.pushButton_2_change_password.toggled.connect(self.pushButton_3_change_password.setChecked)
        self.pushButton_2_genetate.clicked.connect(self.pushButton_3_generate.setChecked)
        self.pushButton_3_generate.clicked.connect(self.pushButton_2_genetate.setChecked)

        self.page_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label_1.setText("")
        self.home_btn_1.setText("")
        self.dashboard_btn_1.setText("")
        self.pushButton_3_change_password.setText("")
        self.pushButton_2_genetate.setText("")
        self.pushButton_2_change_language.setText("")
        self.exit_btn_1.setText("")
        self.logo_label_2.setText("")
        self.logo_label_3.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.home_btn_2.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.dashboard_btn_2.setText(QCoreApplication.translate("MainWindow", u"Edit Information", None))
        self.pushButton_2_change_password.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.pushButton_3_generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.pushButton_Change_lang.setText(QCoreApplication.translate("MainWindow", u"CN", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Change_lang.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.exit_btn_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.change_btn.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search....", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.user_btn.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.button_add_list_to_generate.setText("")
        self.button_clear_list_to_generate.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.pushButton_generate_doc.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.radioButton_newDoc.setText(QCoreApplication.translate("MainWindow", u"Replace Old Doc file And Add new Doc file", None))
        self.radioButton_addImage.setText(QCoreApplication.translate("MainWindow", u"Add new images to the same old doc file", None))
        self.label_show.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.pushButton_upload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.pushButton_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
    # retranslateUi

