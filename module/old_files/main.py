import  sys
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from resource_ui2 import Ui_MainWindow
from functools import partial

import time
import json
import traceback, sys

from module import upload as M_upload
from module import worker_pyqt as WorkQT
from module import Create_Menu_From_MD as Read_Write_Menu 

"""
#NOTE Main Window---------------------------------Main Window------------------------------------------>  
"""
class MainWindow( QMainWindow ):

    ## Initial Function
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui     =   Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.icon_only_widget.hide()
        self.ui.page_stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(1)

        # initialize variables
        self.selected_menu_json_path = None
        self.next_menu_list = None
        self.prev_menu_list = None
        self.menu_qcb_list_index = 0
        self.current_menu_list = None
        self.current_page_index = 0
        self._Menu_Json = None
        self.first_key = ""

        self.threadpool = QThreadPool()

        # initialize some module value
        self.M_Uplaod = M_upload

        #
        self.threadpool = QThreadPool()

        # initial page menu setting
        self.make_drop_down_menu()

        # getting ui elements
        self.scroll_content_0 = self.ui.scrollArea

        self.vbox_menu = QVBoxLayout()
        self.combo_box_list : QComboBox() = [] 

        # print(type(self.combo_box_list), "sdf")



    ## Function For Searching
    def on_search_btn_clicked(self):
        self.ui.page_stackedWidget.setCurrentIndex(1)
        search_text = self.ui.search_input.text().strip()

        if search_text:
            self.ui.search_label_9.setText(search_text)
            # print("Search bar text ", search_text)


    ## Function For Changing Page TO 
    ## User Page <<curently we do not need it>>
    def on_user_btn_clicked(self):
        self.ui.page_stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable 
    ## Status When page_stackedWidget index changed
    def on_stackeWidget_currentChanged(self, index):
        btn_list    =   self.ui.icon_only_widget.findChildren(QPushButton)\
                        + self.ui.full_menu_widget.findChildren( QPushButton)
        
        for btn in btn_list:
            if index in [5,6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    ## SECTION - Pagination
    ## function for changing menu page ------------------------------------------->

    def on_home_btn_1_toggled(self):        ## for uplaodpage
        self.ui.page_stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):        ## for uplaodpage
        self.ui.page_stackedWidget.setCurrentIndex(0)

    def on_dashboard_btn_1_toggled(self):   ## for  download page
        self.ui.page_stackedWidget.setCurrentIndex(1)

    def on_dashboard_btn_2_toggled(self):   ## downlaod page
        self.ui.page_stackedWidget.setCurrentIndex(1)

    #!SECTION - Pagination
    ##  ---------------------------------------------------------------------------/>



    ## SECTION - UPLOAD button pressed
    ## when click upload button --------------------------------------------------->
    def on_pushButton_pressed(self):

        # Open File Dialog
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)" )
		
		# Output filename to screen and pass it to upload module
        if fname:
            file_path   =   fname[0]
            print( " File selected ", file_path )

            worker = WorkQT.Worker(self.ongoing_proccess , file_path)
            worker.signals.progress.connect(self.show_progress)
            worker.signals.result.connect(self.show_result)
            worker.signals.finished.connect(self.show_progress)

            self.threadpool.start(worker)

    
    ## SECTION  WORKER Class method For Upload
    def ongoing_proccess(self,file_path,progress_callback):
        
        # file_path = "/home/gq/Documents/Project/GQ/Baidu_File_Management/Github/test3_adding_UI_for_future_functional/style.qss"
        progress_callback.emit("Process started")
        if (self.M_Uplaod.is_zip_file(file_path)):
            pass

        for n in range(1,100):
            value = "Checking file type for given '" + file_path + "' Pls Wait"
            progress_callback.emit(value)
            time.sleep(1)

        return "FInished"

    ## show progress
    def show_progress(self, s):
        print(s)

    ## result
    def show_result(self,s):
        print("Showing resutl done for this even ",s)

    ## thread complete
    def thread_complete(self):
        print("Thread for uplaod done")

    ## !SECTION worker methods for Upload 
    # END--------------------------------------------------------------------------/>

    ## !SECTION Upload Button
    ## END-------------------------------------------------------------------------/>



    ##  SECTION - Make Drop Down Menu
    # -------------------------------------------------------------------------------> 
    def make_drop_down_menu(self, page_index=0):

        # test ::=>
        #   json_value = Read_Write_Menu.get_json_for_menu()
        #   print(" Json value from the md fiel ", json_value)
        #   Read_Write_Menu.create_menu_json_file(json_value)

        worker = WorkQT.Worker(self.on_going_process_for_initial_menu_creation)
        worker.signals.result.connect(self.result_for_initial_menu_creation)
        self.threadpool.start(worker)

        #NOTE - making menu path empty
        self.selected_menu_json_path = ""
        self.combo_box_list = []


    def on_going_process_for_initial_menu_creation(self, progress_callback):

        progress_callback.emit ( " Reading Menu From 'menu.md' file " )
        self._Menu_Json = Read_Write_Menu.get_json_for_menu ()
        progress_callback.emit ( "Reading done successfuly " )

        self.first_key = list ( self._Menu_Json.keys() )[0]

        self.current_menu_list = list (self.get_list_from_given_data(self._Menu_Json))

        # NOTE - setting initial menu path
        self.selected_menu_json_path += self.first_key 



    def result_for_initial_menu_creation(self, s):
        label = QLabel(self)
        label.setText("Chose File" )

        combo = QComboBox(self)
        combo.addItems(self.current_menu_list)
        combo.setCurrentIndex(-1)

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(combo)

        widget = QWidget()
        widget.setFixedHeight(40)
        widget.setLayout(layout)

        self.vbox_menu.addWidget(widget)

        widget = QWidget()
        widget.setLayout(self.vbox_menu)
        self.scroll_content_0.setWidget(widget)

        self.combo_box_list.append(combo)

        temp_lenght= len(self.combo_box_list)

        # print("comobox list ", self.combo_box_list[temp_index])

        self.combo_box_list[ temp_lenght -1 ].activated[int].connect( 
            partial(self.try_to_add_menu,   temp_lenght )) 
        # combo.activated[int].connect( partial(self.try_to_add_menu,   temp_index )) 

    def try_to_add_menu(self, temp_lenght):
        
        time.sleep(1)
        # NOTE - setting menu path
        value_chosen = self.combo_box_list[
             temp_lenght -1 ].currentText()
        self.selected_menu_json_path +="."+ value_chosen

        temp_path = self.selected_menu_json_path.split(".")


        lenght = len(self.combo_box_list)
        print("1 starting lenght ", lenght , " Temporary lenght ", temp_lenght)

        if( lenght > temp_lenght ):
            print ("Combobox has children node , but previous " 
                    "node changed...needd to change all childrens node from ", temp_lenght )
            
            # self.vbox_menu.deleteLater()
            # for i in reversed(range(self.vbox_menu.count())): 

            #     self.vbox_menu.itemAt(i).widget().deleteLater()
            #     self.vbox_menu.itemAt(i).widget().setParent(None)

            for i in reversed(range(self.vbox_menu.count())): 
                
                if i >= temp_lenght :
                    self.vbox_menu.itemAt(i).widget().deleteLater()
                    self.vbox_menu.itemAt(i).widget().setParent(None)
            total_combo_parent_widget = self.scroll_content_0.findChildren(QWidget)
            
            # print(" Has total comboboxes of ",len( total_combo_parent_widget))
            self.combo_box_list = self.combo_box_list[0:temp_lenght ]

            temp_json_path_list  = self.selected_menu_json_path.split(".")

            temp_json_path_list = temp_json_path_list[:temp_lenght]

            print ("Path after cut ", temp_json_path_list)

            string= "" + temp_json_path_list[0]
            if( temp_lenght > 1):
                for x_temp_j in temp_json_path_list[1:]:
                    string += "." + x_temp_j

            
            self.selected_menu_json_path = string+"." + self.combo_box_list[temp_lenght-1].currentText()

            print("Slected json  menu path ",  self.selected_menu_json_path , " combo_box_lenght ", len(self.combo_box_list))
           
            
            self.try_to_add_menu(len(self.combo_box_list))
            
        elif ( lenght == temp_lenght ):
            print(" Jtemp path  ", temp_path)

            try:

                temp_json = self._Menu_Json[temp_path[0]]
                for last_key in temp_path[1:]:
                    temp_json = temp_json [last_key]
                self.add_children_menu_to_the_ui(temp_json)
            except:
                path = self.first_key+ "." + str( self.combo_box_list[0].currentText())
              
                for x in self.combo_box_list[1:]:
                    path +="." + str( x.currentText())
                self.selected_menu_json_path = path
                print("path for ", self.selected_menu_json_path)
        
        
        print("2 starting lenght ", lenght , " Temporary lenght ", temp_lenght)

    def get_list_from_given_data(self, value ) :
        key = list(value.keys())[0]
        return value[key].keys()


    

    def add_children_menu_to_the_ui(self, item):
       
        combo = QComboBox(self)
        combo.addItems(item)
        combo.setCurrentIndex(-1)

        layout = QHBoxLayout()
        layout.addWidget(combo)

        widget = QWidget()
        widget.setFixedHeight(40)
        widget.setLayout(layout)

        self.vbox_menu.addWidget(widget)

        self.combo_box_list.append(combo)

        temp_lenght= len(self.combo_box_list)

     

      
        self.combo_box_list[ temp_lenght -1 ].activated[int].connect(partial(self.try_to_add_menu,   temp_lenght ))

        print("path " , self.selected_menu_json_path)
        

    ##!SECTION MakeDrop Down Menu
    # END----------------------------------------------------------------------------/>

"""
 #NOTE END-Main Window---------------------------------Main Window------------------------------------------>      
"""



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

