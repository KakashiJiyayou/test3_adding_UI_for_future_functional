import  sys
from PyQt5.QtWidgets import  QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from resource_ui2 import Ui_MainWindow

"""
Main Window
"""
class MainWindow( QMainWindow ):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui     =   Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(1)

    ## function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()

        if search_text:
            self.ui.search_label_9.setText(search_text)
            # print("Search bar text ", search_text)

    ## function for changing page to user page <<curently we do not need it>>
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackeWidget_currentChanged(self, index):
        btn_list    =   self.ui.icon_only_widget.findChildren(QPushButton)\
                        + self.ui.full_menu_widget.findChildren( QPushButton)
        
        for btn in btn_list:
            if index in [5,6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    ## function for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashboard_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashboard_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_others_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_others_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
"""END"""


### start the app
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## loading style file <<Although it can be done via QFile >>
    with open('style.qss', 'r') as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

