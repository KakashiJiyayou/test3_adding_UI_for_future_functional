import  sys
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from functools import partial
from resource_ui2 import Ui_MainWindow


import time
import json
import subprocess
import traceback, sys


from module import upload as M_upload
from module import worker_pyqt as WorkQT
from module import  database as Database
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
        self._folder_chosen = True

        self.Upload_Button_Clicked = False
        self.Update_Button_Clicked = False

    

        self._search_path_list = []

        self.threadpool = QThreadPool()

        # initialize some module value
        self.M_Uplaod = M_upload

        #
        self.threadpool = QThreadPool()

        # getting ui elements
        self.scroll_content_0 = self.ui.scrollArea_2_edit_page
        self.vbox_menu = QVBoxLayout()
        self.combo_box_list : QComboBox() = [] 

        

        self.setting_up_app()


    ## Function For Searching
    def on_search_btn_clicked(self):
        self.ui.page_stackedWidget.setCurrentIndex(1)
        search_text = self.ui.search_input.text().strip()

        if search_text:
            self.ui.search_label_9.setText( search_text)
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
        
        # for now we will use 2nd index of stack widget
        self.ui.page_stackedWidget.setCurrentIndex(1)

        # set QPushbutton( upload in first page ) text
        self.ui.pushButton_upload.setText("Chose File")

        # set up for search completer
        self.searh_completer = QCompleter ( self._search_path_list )
        self.searh_completer.setCaseSensitivity(0)
        self.ui.search_input.setCompleter ( self.searh_completer )

        # initial methods
        # initial page menu setting
        self.make_drop_down_menu()

        # make_goup_one visible and enable

    
    ## Group1 
    def enable_show_g1 ( self ):
        self.ui.pushButton_upload.setEnabled ( True )


    ## Group1 disable
    def disable_g1( self ):
        self.ui.pushButton_upload.setEnabled ( False )


    ## Group Edit 2 
    def enable_show_ge2( self ):
        self.ui.pushButton_update.setEnabled ( True )
        self.ui.pushButton_download.setEnabled ( True )
        self.ui.pushButton_remove.setEnabled ( True )
        self.ui.radioButton_newDoc.setEnabled ( True )
        self.ui.radioButton_addImage.setEnabled ( True)
        self.ui.search_btn.setEnabled ( True )
        self.ui.search_input.setEnabled (True)


    ## Group Edit 2 disable
    def disable_ge2( self ):
        self.ui.pushButton_update.setEnabled ( False )
        self.ui.pushButton_download.setEnabled ( False )
        self.ui.pushButton_remove.setEnabled ( False )
        self.ui.radioButton_newDoc.setEnabled ( False )
        self.ui.radioButton_addImage.setEnabled ( False )
        self.ui.search_btn.setEnabled ( False)
        self.ui.search_input.setEnabled ( False )

    
    ## Group side bar
    def enable_side_bar ( self ):
        self.ui.home_btn_1.setEnabled ( True )
        self.ui.home_btn_2.setEnabled ( True )
        self.ui.dashboard_btn_1.setEnabled ( True )
        self.ui.dashboard_btn_2.setEnabled ( True )


    ## Group side bar disable
    def diasble_side_bar ( self ):
        self.ui.home_btn_1.setEnabled ( False )
        self.ui.home_btn_2.setEnabled ( False )
        self.ui.dashboard_btn_1.setEnabled ( False )
        self.ui.dashboard_btn_2.setEnabled ( False )



    ##----------------------------------------------------------------------------/>
    ## !SECTION


    ## SECTION - Pagination
    ## function for changing menu page ------------------------------------------->

    def on_home_btn_1_toggled(self):        ## for uplaodpage
        self._current_page_index = 0
        self.update_page_status ()
    

    def on_home_btn_2_toggled(self):        ## for uplaodpage
        self._current_page_index = 0
        self.update_page_status ()
    

    def on_dashboard_btn_1_toggled(self):   ## for  download page
        self._current_page_index = 1
        self.update_page_status ()
    

    def on_dashboard_btn_2_toggled(self):   ## downlaod page
        self._current_page_index = 1
        self.update_page_status ()
    

    def update_page_status( self ):
        if self._current_page_index == 0 :
            self.enable_show_g1 ()
            self.disable_ge2 ()
        else:
            self.enable_show_ge2 ()
            self.disable_g1 ()


    ##  --------------------------------------------------------------------------/>
    ## !SECTION - Pagination


    ## SECTION - Remove Acton
    ## ---------------------------------------------------------------------------->

    ## when user clicked remove push button
    def on_pushButton_remove_pressed ( self ):

        # show message_box do they really want to delete
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Removing Contents")
        dlg.setText("Are  you sure you are willing to remove contents ??")
        dlg.setStandardButtons ( QMessageBox.Yes |  QMessageBox.No )
        button = dlg.exec ()

        if button == QMessageBox.Yes :
            dlg1 = QMessageBox(self)
            dlg1.setWindowTitle("Removing Contents now")
            dlg1.setText("We will remove now ??")
            dlg1.setStandardButtons ( QMessageBox.Yes |  QMessageBox.No )
            button1 = dlg1.exec ()
            if button1 == QMessageBox.Yes :
                print ( "Removing Contents" )

    ## later need to use worker signal to the background work

    ## ----------------------------------------------------------------------------/>
    ## !SECTION - Remove Action



    ## SECTION - Download Action
    ## ---------------------------------------------------------------------------->

    ## when user clicked remove push button
    def on_pushButton_download_pressed ( self ):

        # show folder opening option
        fname = QFileDialog.getExistingDirectory(self, 'Select Folder')

        if fname:
            print ( "Selected path " , fname)
        else:
            print ( "User did not chose anything " )

    ## later need to use worker signal to the background work

    ## ----------------------------------------------------------------------------/>
    ## !SECTION - Download Action



    ## SECTION - Update Action
    ## ----------------------------------------------------------------------------->
    ## when update button pressed
    def on_pushButton_update_pressed ( self ):

        # check the text vlaue in search input
        search_input = self.ui.search_input.text(  ).strip ( )
        
        if search_input :
            print ( "user selected contents ", search_input )
        else :
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Search Content Empty")
            dlg.setText("Pls , selec file contents from search area ")
            dlg.setStandardButtons ( QMessageBox.Ok  )
            dlg.exec ()



    ## ----------------------------------------------------------------------------/>
    ## !SECTION - Update Action




    ## SECTION - UPLOAD button pressed
    ## when click upload button --------------------------------------------------->

    def on_pushButton_upload_pressed( self ):

        #
        self.Upload_Button_Clicked = True

        # disble upload button 
        self.ui.pushButton_upload.setDisabled ( True )

        # 
        self.show_dialog_chosing_file()
        

    ## NOTE - show dialog box
    # 
    def show_dialog_chosing_file( self ): 
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Opening File")
        dlg.setText("Here chose wheter to chose directory or" +
                     " Just want to open file (.zip, .png, .jpg etc...) ")
        
        # setting buttons for dialog
        # dlg.setStandardButtons(QMessageBox.Yes| QMessageBox.No)
        chose_folder = QPushButton()
        chose_file  = QPushButton()
        close_button = QPushButton()
        chose_folder.setText( "Chose Folder" )
        chose_file.setText(" Chose File" )

        chose_folder.clicked.connect(  self.folder_chosen )
        chose_file.clicked.connect(  self.file_chosen )
        close_button.clicked.connect ( self.file_chose_window_got_cancled )
        
        dlg.addButton ( chose_folder, QMessageBox.YesRole )
        dlg.addButton ( chose_file, QMessageBox.NoRole )
        # dlg.addButton ( close_button, QMessageBox.Cancel )

        # dlg.addButton ( )
        # dlg.setStandardButtons (  )
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button != QMessageBox.YesRole or button != QMessageBox.NoAll :
            self.file_chose_window_got_cancled()


    ##  
    def file_chose_window_got_cancled ( self ):
        #
        self.Upload_Button_Clicked = False

        # disble upload button 
        self.ui.pushButton_upload.setEnabled ( True )

    ##
    def folder_chosen(self):
        self._folder_chosen = True
        self.start_chosing()

    ##
    def file_chosen(self):
        self._folder_chosen = False
        self.start_chosing()

    ##
    ## Here we will start threadpool and other part
    def start_chosing(self):

        if self._folder_chosen:
            fname = QFileDialog.getExistingDirectory(self, 'Select Folder')
        else:
            fname = QFileDialog.getOpenFileName(self, "Select file", "", "All Files (*)" )
            

        # Open File Dialog
        # fname = QFileDialog.getOpenFileName(self, "Select Folder", "", "All Files (*)" )
		
		# Output filename to screen and pass it to upload module
        if fname:
            if self._folder_chosen:
                file_path   =   fname
            else:
                file_path = fname[0]
            print( " File selected ", file_path )

            worker = WorkQT.Worker(self.ongoing_proccess , file_path)
            worker.signals.progress.connect(self.show_progress)
            worker.signals.result.connect(self.show_result)
            worker.signals.finished.connect(self.thread_complete)

            self.threadpool.start(worker)

            # test method for uplaod
            # self.test(file_path)


    ## Test methods for uplaod
    ##
    def unzip_upload_insert( self, path , menu , progress_callback ):

        print ("Menu given ", menu)

        # clearing temp folder
        clear_dir = M_upload.clear_temp_dir() 
        print ( "clear_dir ", clear_dir["clear_temp_dir"] )
        progress_callback.emit ( "clear_dir"  )

        # checking giving path belongs to a zip
        is_zip_file = M_upload.is_zip_file( path )
        if is_zip_file :

            # unzip
            result = M_upload.start_unzipping ( path )

            # if unzip succesfull
            if result[ "start_unzipping" ]:
                print ( "Unzipped , will uplaod to baidu ")

        progress_callback.emit( "Unzipped" )

        # getting the list
        folder_list = M_upload.get_folder_list() 
        # print ( "Is zip file ", M_upload.is_zip_file( path ) )
        print ( "List of directorries ", folder_list, menu )


        
        progress_callback.emit( "uploading to baidu" )

        # call upload module get the path
        command = M_upload.get_bypy_upload_command ()

        # use subproccess to uplaod 
        self.suproccess_show_plaintext ( command, progress_callback)
        
        progress_callback.emit( "uploading to baidu is done" )
        
        # clearing temp directory
        print ( " Clear temp folder ", M_upload.clear_temp_dir() )

        # insterting data
        insert_result = Database.insert_dir_list ( folder_list, menu )
        print ( "DB insert result" , insert_result )

        # enable upload button
        self.ui.pushButton_upload.setEnabled(True)

        #  
        self.Upload_Button_Clicked = False



    
    ## SECTION  WORKER Class method For Upload
    def ongoing_proccess(self,file_path,progress_callback):
        
        # show thar process starte
        progress_callback.emit("Process started")

        # first check all the comboxes selected or not
        all_comboboxes_selected = False
        all_text = ""

        # check all existing comboboxes in scroll_area_editpage
        i = 0
        for menu in self.combo_box_list :
            text = menu.currentText ()

            if text :
                print ( "Got selected menu ", text )
                all_comboboxes_selected = True
                if i > 0:
                    all_text += "." + text
                else:
                    all_text +=  text
            else :
                print ( "Combobox not selected" )
                all_comboboxes_selected = False
            i += 1

        # if comboboxes are not all set show message
        if not all_comboboxes_selected :
            self.show_popup_text ( "Menu missing !!" , "All menu not selected, pls selected" +
                              " all menu first thne click uplod" )
        else :
            self.unzip_upload_insert ( file_path, all_text, progress_callback )

        
    

        #
        # if (self.M_Uplaod.is_zip_file(file_path)):
        #     pass

        # for n in range(1,100):
        #     value = "Checking file type for given '" + file_path + "' Pls Wait"
        #     progress_callback.emit(value)
        #     time.sleep(1)

        return "Finished Uploading"

    ## show progress
    def show_progress(self, s):
        self.ui.plainText_show.setPlainText ( s )
        print("from worker ",s)

    ## result
    def show_result(self, s):
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

            # add values to the last indexed combo list 
            self.reset_comboxes_item()

            # reset selected_json_path
            temp_p = self.reset_selected_json_path(index) 

            self.show_curren_selected_json_path("Try, where user previous click got clicked")

            # reset VBOX layout 
            self.reset_v_box_layout(self.vbox_menu, index)

           
            
        except Exception as e:
            print("Next Menu Does not exits or other problem" , e)
            print(traceback.format_exc())

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
    # we need to check, the "KEY" has list or not
    def reset_combo_list( self, index ):

        add_item = 1

        # before adding two lets confirm, the current menu has submen or not
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
        print ("Vbox count ", layout.count() , " len of combo boxes ", len(self.combo_box_list))
        
        for i in reversed( range( layout.count() ) ): 
                if layout.count() <= len(self.combo_box_list):
                    break
                layout.itemAt( i ).widget().deleteLater()
                layout.itemAt( i ).widget().setParent(None)
                

    # reseting comboboxes items at -1th position
    def reset_comboxes_item( self  ):

        i = 0
        temp_json = self._Menu_Json[ self._first_key ] 

        for item in self.combo_box_list:
            if item.currentText():
                print("Comboxes text ", item.currentText() )
                temp_json = temp_json[ item.currentText() ]
                pass
            else :
                if isinstance(temp_json, dict ): 
                    print( "Curent index does not have text, so will add dic \n\t\t ",
                        " ", temp_json.keys() )
                    
                    new_list = list ( temp_json.keys() )
                    self.combo_box_list[-1].addItems(new_list)
                    self.combo_box_list[-1].setCurrentIndex(-1)
                elif isinstance( temp_json, str ):
                    print( "Curent index does not have text, so will add str \n\t\t ",
                        " ", temp_json, "\t size", len(temp_json)  )
                    
                    self.combo_box_list[-1].addItem(temp_json)
                    self.combo_box_list[-1].setCurrentIndex(-1)

                    if (len (temp_json) == 0 ):
                        print (" Size of list ", len (self.combo_box_list) )
                        self.combo_box_list = self.combo_box_list[:-1]
                        print("poping list ")
                        print (" Size of list ", len (self.combo_box_list) )

                elif isinstance( temp_json, list ):
                    print( "Curent index does not have text, so will add list \n\t\t ",
                        " ", temp_json )
                    self.combo_box_list[-1].addItems(temp_json)
                    self.combo_box_list[-1].setCurrentIndex(-1)

    
    # chec selected menu has sub menu or not
    def selected_has_sub_menu(self, text, index):
        temp_json = self._Menu_Json[ self._first_key ] 

    def show_curren_selected_json_path(self, from_where=None):
        print("Path " , self._selected_menu_json_path , "   From ", from_where 
              , "\t lenght of current menu list ", len(self.combo_box_list))
        
    ## END----------------------------------------------------------------------------/>
    ## !SECTION MakeDrop Down Menu


    ## SECTION Search Result 
    #  -------------------------------------------------------------------------------->
    # Update search path list
    # This method will take value for "self._search_path_list"
    # It will just add them to the completer
    def update_search_path( self ):
        model = self.searh_completer.model ()
        model.setStringList( self._search_path_list)
        print ("Search completer updated ")
        

    # get search list from 
    def get_search_path_list_from_db ( self, progress_callback ):

        # Comobox nth menu for now by deafult None
        # if loop through all menu return no text , it will be none
        # we will get from another method
        filter_json = None
        # for i in range ( 0, 4):
        #     filter_list = []

        # Try to get text from search
        searc_txt = self.ui.search_input

        # call database to get data on this 
        result_list = Database.get_dir_list()
        print ( result_list )

        # put the list in self._search_path_list
        self._search_path_list = result_list

        print ("Now update the completer")
        self.update_search_path()



    def on_search_input_textChanged ( self ):

        worker = WorkQT.Worker ( self.get_search_path_list_from_db )

        self.threadpool.start ( worker )

    

    #  -------------------------------------------------------------------------------/>
    ## !SECTION



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



    # show message box without tex
    def show_popup_text ( self , title, details ) :
        # show message_box do they really want to delete
        dlg = QMessageBox( self )
        dlg.setWindowTitle( title )
        dlg.setText( details )
        dlg.setStandardButtons ( QMessageBox.Ok )
        dlg.exec ()


    # NOTE - using subproccessing to do bypy work 
    def suproccess_show_plaintext ( self, command_list , progress_callback )  :

        proc =  subprocess.Popen( command_list  , stdout=subprocess.PIPE )

        while True:
            line = proc.stdout.readline()
            if not line:
                break

            # print ( "test:", line.rstrip() )
            value = str ( line, "utf-8") 
            print("subprocces ", value)

            progress_callback.emit ( value )


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

