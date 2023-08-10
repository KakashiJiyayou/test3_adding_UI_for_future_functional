# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\base_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.logo_label_1.setFont(font)
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap(":/icon/icon/Logo.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_2.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout_2.addWidget(self.home_btn_1)
        self.dashboard_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.dashboard_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dashboard_btn_1.setIcon(icon1)
        self.dashboard_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.dashboard_btn_1.setCheckable(True)
        self.dashboard_btn_1.setAutoExclusive(True)
        self.dashboard_btn_1.setObjectName("dashboard_btn_1")
        self.verticalLayout_2.addWidget(self.dashboard_btn_1)
        self.pushButton_3_change_password = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_3_change_password.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/group-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/group-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_3_change_password.setIcon(icon2)
        self.pushButton_3_change_password.setCheckable(True)
        self.pushButton_3_change_password.setAutoExclusive(True)
        self.pushButton_3_change_password.setObjectName("pushButton_3_change_password")
        self.verticalLayout_2.addWidget(self.pushButton_3_change_password)
        self.pushButton_2_genetate = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_2_genetate.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/edit-11-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/edit-11-49.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_2_genetate.setIcon(icon3)
        self.pushButton_2_genetate.setCheckable(True)
        self.pushButton_2_genetate.setAutoExclusive(True)
        self.pushButton_2_genetate.setObjectName("pushButton_2_genetate")
        self.verticalLayout_2.addWidget(self.pushButton_2_genetate)
        self.pushButton_2_change_language = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_2_change_language.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/product-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/product-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_2_change_language.setIcon(icon4)
        self.pushButton_2_change_language.setCheckable(True)
        self.pushButton_2_change_language.setAutoExclusive(True)
        self.pushButton_2_change_language.setObjectName("pushButton_2_change_language")
        self.verticalLayout_2.addWidget(self.pushButton_2_change_language)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_1.setCheckable(True)
        self.exit_btn_1.setAutoExclusive(True)
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout_5.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(":/icon/icon/Logo.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_3.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_3.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout.addWidget(self.home_btn_2)
        self.dashboard_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.dashboard_btn_2.setIcon(icon1)
        self.dashboard_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.dashboard_btn_2.setCheckable(True)
        self.dashboard_btn_2.setAutoExclusive(True)
        self.dashboard_btn_2.setObjectName("dashboard_btn_2")
        self.verticalLayout.addWidget(self.dashboard_btn_2)
        self.pushButton_2_change_password = QtWidgets.QPushButton(self.full_menu_widget)
        self.pushButton_2_change_password.setIcon(icon2)
        self.pushButton_2_change_password.setCheckable(True)
        self.pushButton_2_change_password.setAutoExclusive(True)
        self.pushButton_2_change_password.setObjectName("pushButton_2_change_password")
        self.verticalLayout.addWidget(self.pushButton_2_change_password)
        self.pushButton_3_generate = QtWidgets.QPushButton(self.full_menu_widget)
        self.pushButton_3_generate.setIcon(icon3)
        self.pushButton_3_generate.setCheckable(True)
        self.pushButton_3_generate.setAutoExclusive(True)
        self.pushButton_3_generate.setObjectName("pushButton_3_generate")
        self.verticalLayout.addWidget(self.pushButton_3_generate)
        self.pushButton_Change_lang = QtWidgets.QPushButton(self.full_menu_widget)
        self.pushButton_Change_lang.setIcon(icon4)
        self.pushButton_Change_lang.setCheckable(True)
        self.pushButton_Change_lang.setAutoExclusive(True)
        self.pushButton_Change_lang.setObjectName("pushButton_Change_lang")
        self.verticalLayout.addWidget(self.pushButton_Change_lang)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 413, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn_2.setCheckable(True)
        self.exit_btn_2.setAutoExclusive(True)
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout_5.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.vertical_Layout_6 = QtWidgets.QVBoxLayout()
        self.vertical_Layout_6.setObjectName("vertical_Layout_6")
        self.header_widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.header_widget_3.setObjectName("header_widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.header_widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header_widget = QtWidgets.QWidget(self.header_widget_3)
        self.header_widget.setMinimumSize(QtCore.QSize(0, 40))
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(self.header_widget)
        self.change_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/activity-feed-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon6)
        self.change_btn.setIconSize(QtCore.QSize(14, 14))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(self.header_widget)
        self.search_input.setMinimumSize(QtCore.QSize(300, 0))
        self.search_input.setMaximumSize(QtCore.QSize(99999, 16777215))
        self.search_input.setClearButtonEnabled(True)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.header_widget)
        self.search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/search-13-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon7)
        self.search_btn.setIconSize(QtCore.QSize(14, 14))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.user_btn = QtWidgets.QPushButton(self.header_widget)
        self.user_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/user-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_btn.setIcon(icon8)
        self.user_btn.setIconSize(QtCore.QSize(14, 14))
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_4.addWidget(self.user_btn)
        self.verticalLayout_5.addWidget(self.header_widget)
        self.vertical_Layout_6.addWidget(self.header_widget_3)
        self.page_stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.page_stackedWidget.setObjectName("page_stackedWidget")
        self.generate_page = QtWidgets.QWidget()
        self.generate_page.setObjectName("generate_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.generate_page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_for_scroll = QtWidgets.QWidget(self.generate_page)
        self.widget_for_scroll.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_for_scroll.setObjectName("widget_for_scroll")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_for_scroll)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_generate_page = QtWidgets.QScrollArea(self.widget_for_scroll)
        self.scrollArea_generate_page.setWidgetResizable(True)
        self.scrollArea_generate_page.setObjectName("scrollArea_generate_page")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 615, 130))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_generate_page.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_generate_page, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_for_scroll, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.generate_page)
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 300))
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.widget)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_checkbox = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_checkbox.setGeometry(QtCore.QRect(0, 0, 260, 309))
        self.scrollAreaWidgetContents_checkbox.setObjectName("scrollAreaWidgetContents_checkbox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_checkbox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollarea_checkbox_dirlist_000 = QtWidgets.QVBoxLayout()
        self.scrollarea_checkbox_dirlist_000.setSpacing(0)
        self.scrollarea_checkbox_dirlist_000.setObjectName("scrollarea_checkbox_dirlist_000")
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox.setObjectName("checkBox")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_5)
        self.checkBox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_10.setObjectName("checkBox_10")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_10)
        self.checkBox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_8.setObjectName("checkBox_8")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_9.setObjectName("checkBox_9")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_9)
        self.checkBox_13 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_13.setObjectName("checkBox_13")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_13)
        self.checkBox_14 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_14.setObjectName("checkBox_14")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_14)
        self.checkBox_17 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_17.setObjectName("checkBox_17")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_17)
        self.checkBox_12 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_12.setObjectName("checkBox_12")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_12)
        self.checkBox_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_11.setObjectName("checkBox_11")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_11)
        self.checkBox_16 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_16.setObjectName("checkBox_16")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_16)
        self.checkBox_15 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_15.setObjectName("checkBox_15")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_15)
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_7.setObjectName("checkBox_7")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_7)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_6.setObjectName("checkBox_6")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_6)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_checkbox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.scrollarea_checkbox_dirlist_000.addWidget(self.checkBox_2)
        self.gridLayout_3.addLayout(self.scrollarea_checkbox_dirlist_000, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_checkbox)
        self.horizontalLayout_12.addWidget(self.scrollArea_2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.button_add_list_to_generate = QtWidgets.QPushButton(self.widget)
        self.button_add_list_to_generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_add_list_to_generate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_add_list_to_generate.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-8-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add_list_to_generate.setIcon(icon9)
        self.button_add_list_to_generate.setIconSize(QtCore.QSize(32, 32))
        self.button_add_list_to_generate.setFlat(True)
        self.button_add_list_to_generate.setObjectName("button_add_list_to_generate")
        self.verticalLayout_10.addWidget(self.button_add_list_to_generate)
        self.button_clear_list_to_generate = QtWidgets.QPushButton(self.widget)
        self.button_clear_list_to_generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_clear_list_to_generate.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/icon/x-mark-2-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_clear_list_to_generate.setIcon(icon10)
        self.button_clear_list_to_generate.setIconSize(QtCore.QSize(32, 32))
        self.button_clear_list_to_generate.setFlat(True)
        self.button_clear_list_to_generate.setObjectName("button_clear_list_to_generate")
        self.verticalLayout_10.addWidget(self.button_clear_list_to_generate)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.horizontalLayout_12.addLayout(self.verticalLayout_10)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_12.addWidget(self.listWidget)
        self.gridLayout_7.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 2, 0, 1, 1)
        self.widget_upload = QtWidgets.QWidget(self.generate_page)
        self.widget_upload.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_upload.setObjectName("widget_upload")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_upload)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.widget_upload)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_upload)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(320, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        self.pushButton_generate_doc = QtWidgets.QPushButton(self.widget_upload)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_generate_doc.setFont(font)
        self.pushButton_generate_doc.setObjectName("pushButton_generate_doc")
        self.gridLayout_2.addWidget(self.pushButton_generate_doc, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.widget_upload, 3, 0, 1, 1)
        self.page_stackedWidget.addWidget(self.generate_page)
        self.download_page = QtWidgets.QWidget()
        self.download_page.setObjectName("download_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.download_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.search_widget = QtWidgets.QWidget(self.download_page)
        self.search_widget.setMinimumSize(QtCore.QSize(0, 10))
        self.search_widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.search_widget.setAutoFillBackground(False)
        self.search_widget.setStyleSheet("background-color:rgb(213, 246, 255)")
        self.search_widget.setObjectName("search_widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.search_widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_6.addWidget(self.search_widget, 0, 0, 1, 1)
        self.widget_upload_edit = QtWidgets.QWidget(self.download_page)
        self.widget_upload_edit.setObjectName("widget_upload_edit")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_upload_edit)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.radioButton_newDoc = QtWidgets.QRadioButton(self.widget_upload_edit)
        self.radioButton_newDoc.setObjectName("radioButton_newDoc")
        self.horizontalLayout_9.addWidget(self.radioButton_newDoc)
        self.radioButton_addImage = QtWidgets.QRadioButton(self.widget_upload_edit)
        self.radioButton_addImage.setEnabled(True)
        self.radioButton_addImage.setObjectName("radioButton_addImage")
        self.horizontalLayout_9.addWidget(self.radioButton_addImage)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_show = QtWidgets.QLabel(self.widget_upload_edit)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_show.setFont(font)
        self.label_show.setObjectName("label_show")
        self.horizontalLayout_6.addWidget(self.label_show)
        self.input_area = QtWidgets.QLineEdit(self.widget_upload_edit)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_area.setFont(font)
        self.input_area.setObjectName("input_area")
        self.horizontalLayout_6.addWidget(self.input_area)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)
        self.pushButton_upload = QtWidgets.QPushButton(self.widget_upload_edit)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.horizontalLayout_11.addWidget(self.pushButton_upload)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.gridLayout_6.addWidget(self.widget_upload_edit, 3, 0, 1, 1)
        self.widget_actions = QtWidgets.QWidget(self.download_page)
        self.widget_actions.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_actions.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_actions.setObjectName("widget_actions")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_actions)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_update = QtWidgets.QPushButton(self.widget_actions)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout_8.addWidget(self.pushButton_update)
        spacerItem7 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.pushButton_download = QtWidgets.QPushButton(self.widget_actions)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.pushButton_download.setFont(font)
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout_8.addWidget(self.pushButton_download)
        spacerItem8 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.pushButton_remove = QtWidgets.QPushButton(self.widget_actions)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        self.pushButton_remove.setFont(font)
        self.pushButton_remove.setStyleSheet("background-color:rgb(255, 79, 132)")
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.horizontalLayout_8.addWidget(self.pushButton_remove)
        self.gridLayout_6.addWidget(self.widget_actions, 2, 0, 1, 1)
        self.show_result_widget = QtWidgets.QWidget(self.download_page)
        self.show_result_widget.setObjectName("show_result_widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.show_result_widget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.plainText_show = QtWidgets.QPlainTextEdit(self.show_result_widget)
        self.plainText_show.setObjectName("plainText_show")
        self.verticalLayout_9.addWidget(self.plainText_show)
        self.progressBar = QtWidgets.QProgressBar(self.show_result_widget)
        self.progressBar.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.progressBar.setFont(font)
        self.progressBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_9.addWidget(self.progressBar)
        self.gridLayout_6.addWidget(self.show_result_widget, 4, 0, 1, 1)
        self.widget_for_scroll_download_page = QtWidgets.QWidget(self.download_page)
        self.widget_for_scroll_download_page.setMinimumSize(QtCore.QSize(0, 150))
        self.widget_for_scroll_download_page.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_for_scroll_download_page.setObjectName("widget_for_scroll_download_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_for_scroll_download_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_2_edit_page = QtWidgets.QScrollArea(self.widget_for_scroll_download_page)
        self.scrollArea_2_edit_page.setWidgetResizable(True)
        self.scrollArea_2_edit_page.setObjectName("scrollArea_2_edit_page")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 633, 148))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_2_edit_page.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.addWidget(self.scrollArea_2_edit_page)
        self.gridLayout_6.addWidget(self.widget_for_scroll_download_page, 1, 0, 1, 1)
        self.page_stackedWidget.addWidget(self.download_page)
        self.vertical_Layout_6.addWidget(self.page_stackedWidget)
        self.gridLayout_5.addLayout(self.vertical_Layout_6, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.page_stackedWidget.setCurrentIndex(0)
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.dashboard_btn_1.toggled['bool'].connect(self.dashboard_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        self.dashboard_btn_2.toggled['bool'].connect(self.dashboard_btn_1.setChecked) # type: ignore
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton_2_change_language.clicked['bool'].connect(self.pushButton_Change_lang.toggle) # type: ignore
        self.pushButton_Change_lang.clicked['bool'].connect(self.pushButton_2_change_language.toggle) # type: ignore
        self.pushButton_3_change_password.toggled['bool'].connect(self.pushButton_2_change_password.setChecked) # type: ignore
        self.pushButton_2_change_password.toggled['bool'].connect(self.pushButton_3_change_password.setChecked) # type: ignore
        self.pushButton_2_genetate.clicked['bool'].connect(self.pushButton_3_generate.setChecked) # type: ignore
        self.pushButton_3_generate.clicked['bool'].connect(self.pushButton_2_genetate.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_label_3.setText(_translate("MainWindow", "Sidebar"))
        self.home_btn_2.setText(_translate("MainWindow", "Upload"))
        self.dashboard_btn_2.setText(_translate("MainWindow", "Edit Information"))
        self.pushButton_2_change_password.setText(_translate("MainWindow", "Change Password"))
        self.pushButton_3_generate.setText(_translate("MainWindow", "Generate"))
        self.pushButton_Change_lang.setText(_translate("MainWindow", "CN"))
        self.pushButton_Change_lang.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Search...."))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_10.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_8.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_9.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_13.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_14.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_17.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_12.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_11.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_16.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_15.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.pushButton_generate_doc.setText(_translate("MainWindow", "Generate"))
        self.radioButton_newDoc.setText(_translate("MainWindow", "Replace Old Doc file And Add new Doc file"))
        self.radioButton_addImage.setText(_translate("MainWindow", "Add new images to the same old doc file"))
        self.label_show.setText(_translate("MainWindow", "Description"))
        self.pushButton_upload.setText(_translate("MainWindow", "Upload"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
        self.pushButton_download.setText(_translate("MainWindow", "Download"))
        self.pushButton_remove.setText(_translate("MainWindow", "Remove"))
import resource_rc
