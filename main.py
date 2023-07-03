import  sys
from PyQt5.QtWidgets import  QMainWindow, QApplication, QPushButton, QFileDialog
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from resource_ui2 import Ui_MainWindow
from module import upload as M_upload

"""
Main Window
"""
class MainWindow( QMainWindow ):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui     =   Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.page_stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(1)

    ## function for searching
    def on_search_btn_clicked(self):
        self.ui.page_stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()

        if search_text:
            self.ui.search_label_9.setText(search_text)
            # print("Search bar text ", search_text)

    ## function for changing page to user page <<curently we do not need it>>
    def on_user_btn_clicked(self):
        self.ui.page_stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when page_stackedWidget index changed
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
    """start"""
    def on_home_btn_1_toggled(self):        ## for uplaodpage
        self.ui.page_stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):        ## for uplaodpage
        self.ui.page_stackedWidget.setCurrentIndex(0)

    def on_dashboard_btn_1_toggled(self):   ## for  download page
        self.ui.page_stackedWidget.setCurrentIndex(1)

    def on_dashboard_btn_2_toggled(self):   ## downlaod page
        self.ui.page_stackedWidget.setCurrentIndex(1)

    def on_others_btn_1_toggled(self):      ## edit page
        self.ui.page_stackedWidget.setCurrentIndex(2)

    def on_others_btn_2_toggled(self):      ## edit page
        self.ui.page_stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):    ## create new Informaion page
        self.ui.page_stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self, ):  ## create new Information page
        self.ui.page_stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):   ## search page
        self.ui.page_stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):   ## search page
        self.ui.page_stackedWidget.setCurrentIndex(4)
    """end"""
    ## function for changing menu page


    ## when click upload button
    def on_upload_btn_pressed(self):

        # Open File Dialog
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)" )
		
		# Output filename to screen and pass it to upload module
        if fname:
            file_path   =   fname[0]
            self.ui.show_textEdit.setText( file_path )
            print( " File selected ", file_path )
            M_upload.testing( file_path , self.ui.show_textEdit)
    
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

