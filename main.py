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
        # Variables with "_" prefix will be shared between pages
        self._selected_menu_json_path = None
        self._initial_menu_list = None
        self._current_page_index = 0
        self._Menu_Json = None
        self._first_key = ""

        self.threadpool = QThreadPool()

        # initialize some module value
        self.M_Uplaod = M_upload

        #
        self.threadpool = QThreadPool()

        # getting ui elements
        self.scroll_content_0 = self.ui.scrollArea
        self.vbox_menu = QVBoxLayout()
        self.combo_box_list : QComboBox() = [] 

        # initial methods
        # initial page menu setting
        self.make_drop_down_menu()

        self.setting_up_app()


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


    ## SECTION - Settign Up 
    ## -------------------------------------------------------------------------->
    def setting_up_app(self):
        
        # set QPushbutton( upload in first page ) text
        self.ui.pushButton.setText("Chose File")

       


    ##----------------------------------------------------------------------------/>
    ## !SECTION


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

    ##  ---------------------------------------------------------------------------/>
    ## !SECTION - Pagination



    ## SECTION - UPLOAD button pressed
    ## when click upload button --------------------------------------------------->
    def on_pushButton_pressed(self):

        self.ui.pushButton.setDisabled ( True )

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

        # for n in range(1,100):
        #     value = "Checking file type for given '" + file_path + "' Pls Wait"
        #     progress_callback.emit(value)
        #     time.sleep(1)

        return "Finished Uploading"

    ## show progress
    def show_progress(self, s):
        print(s)

    ## result
    def show_result(self,s):
        print("Showing resutl done for this even ",s)

    ## thread complete
    def thread_complete(self):
        print("Thread for uplaod done")

    # END--------------------------------------------------------------------------/>
    ## !SECTION worker methods for Upload 

    ## END-------------------------------------------------------------------------/>
    ## !SECTION Upload Button



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
        self._selected_menu_json_path = ""
        self.combo_box_list = []


    def on_going_process_for_initial_menu_creation(self, progress_callback):

        progress_callback.emit ( " Reading Menu From 'menu.md' file " )
        self._Menu_Json = Read_Write_Menu.get_json_for_menu ()
        progress_callback.emit ( "Reading done successfuly " )

        self._first_key = list ( self._Menu_Json.keys() )[0]

        self._initial_menu_list = list (self.get_list_from_given_data(self._Menu_Json))

        # NOTE - setting initial menu path
        self._selected_menu_json_path += self._first_key 



    def result_for_initial_menu_creation(self, s):
        label = QLabel(self)
        label.setText("Chose File" )

        combo = QComboBox(self)
        combo.addItems(self._initial_menu_list)
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

        self.combo_box_list[ temp_lenght -1 ].activated[int].connect( 
            partial(self.try_to_add_next_menu,   temp_lenght )) 
        
        

    def try_to_add_next_menu(self, next_menu_index):

        current_menu_text = ""

        try :

            # If we are getting a value here, means user pressed a previous menu button
            current_menu_text = self.combo_box_list[ next_menu_index ]

            # index will be -1 
            index = next_menu_index -1

            # Based on current menu index we will do the deletion of menu
            print(" Menu combo box selected is  ", index)

            # We need to reset few thing:
            #                        1.  selected_json_path
            #                        2.  combox_list
            #                        3.  VBOX_layout
            #                        4.  Add value to last indexed list

            # reset combo_list 
            temp_combo_list = self.reset_combo_list(index)

            # reset selected_json_path
            temp_p = self.reset_selected_json_path(index) 

            self.show_curren_selected_json_path("Try, where user previous click got clicked")

            # reset VBOX layout 
            self.reset_v_box_layout(self.vbox_menu, index)

            # add values to the last indexed combo list 
            self.reset_comboxes_item()
            
        except Exception as e:
            print("Next Menu Does not exits or other problem" , e)

            # lets check our menu list size
            current_menu_size = len ( self.combo_box_list)

            # next menu list does not exist
            # so lenght of  menu list will be same as next_menu_index
            if( next_menu_index == current_menu_size):


                #
                #***Another scenerio where lenght and menu_index can be same 
                # The JSON list is already at the end
                # currently it's does not create any problem
                # So we can let it be as it is

                # NOTE - updating menu path 
                self.update_menu_path()
                 
                # self.show_curren_selected_json_path("\\try_to_add_menu\\")
                
                #
                # creating menu
                # first create a list for current path
                temp_path_list = self._selected_menu_json_path.split(".")


                try:
                    # The initial key is not present , we take it in advance
                    temp_json = self._Menu_Json[temp_path_list[0]]

                    # then based on current trail we will make new menu
                    for last_key in temp_path_list[1:]:
                        temp_json = temp_json [last_key]
                    self.add_children_menu_to_the_ui(temp_json)

                except:
                    path = self._first_key+ "." + str( self.combo_box_list[0].currentText())
                
                    for x in self.combo_box_list[1:]:
                        path +="." + str( x.currentText())
                    self._selected_menu_json_path = path
                    print("path for ", self._selected_menu_json_path)
            

            #  
            # Now maybe user clicked Menu which is not last branch
            # let we need to check if selected JSON menu has more list
            # Even we do not check it will work
            else:
                print("we are here exception did not handle some issues"  )

       



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
      
        self.combo_box_list[ temp_lenght -1 ].activated[int].connect(partial(self.try_to_add_next_menu,   temp_lenght ))

        self.show_curren_selected_json_path("\\add_children_menu_to_the_ui\\")


    def get_list_from_given_data(self, value ) :
        key = list(value.keys())[0]
        return value[key].keys()

    # adding new value when combo box  is slected 
    # only call when user selected the current menu
    def update_menu_path(self):
        self._selected_menu_json_path = self._first_key
        for item in self.combo_box_list:
            self._selected_menu_json_path += "." + item.currentText()


    # reseting combo list
    # we will get index of curent selected menu 
    # need to add 1, 
    # which  means from 0th positon, 
    # we will take n(index)th number of element
    def reset_combo_list( self, index ):
        self.combo_box_list = self.combo_box_list[ 0 : index + 2 ]

        self.combo_box_list[-1].clear()
        
        return self._selected_menu_json_path


    # reset selected_json_path
    # here one extra key always added from the begining
    # 
    def reset_selected_json_path( self, current_menu_index):
        temp = self._first_key
        for item in self.combo_box_list:
            temp += "." + item.currentText()
        self._selected_menu_json_path = temp

        return temp


    # resetting Vbox layout
    def reset_v_box_layout( self,layout, index ):
        index = index + 2
        for i in reversed( range( layout.count() ) ): 
            if i >= index :
                layout.itemAt( i ).widget().deleteLater()
                layout.itemAt( i ).widget().setParent(None)

    # reseting comboboxes items at -1th position
    def reset_comboxes_item( self ):
        temp_json = self._Menu_Json[ self._first_key ] 
        for item in self.combo_box_list:
            if item.currentText():
                # print("Comboxes text ", item.currentText() )
                temp_json = temp_json[ item.currentText() ]
                pass
            else :
                print( "Curent index does not have text, so will add these \n\t\t ",
                      " ", temp_json.keys() )
                
                new_list = list ( temp_json.keys() )
                self.combo_box_list[-1].addItems(new_list)
                self.combo_box_list[-1].setCurrentIndex(-1)

    


    def show_curren_selected_json_path(self, from_where=None):
        print("Path " , self._selected_menu_json_path , "   From ", from_where 
              , "\t lenght of current menu list ", len(self.combo_box_list))
        
    ## END----------------------------------------------------------------------------/>
    ## !SECTION MakeDrop Down Menu



    ## SECTION - common methods for UI
    ## --------------------------------------------------------------------------------->

    def change_button_text( self, widget , text ):
        widget.setText(text)


    def change_button_state( self, widget, text ):
        pass


    # here state false means, disable
    def enable_button( self,  widget, state ):

        if not state:
            widget.setDisabled()
        else:
            widget.setEnabled()

    ## ---------------------------------------------------------------------------------/>
    ## !SECTION

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

