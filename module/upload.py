import os
import time
import _thread
import zipfile
from bypy import ByPy
from pyunpack import Archive


bp = ByPy()


## SECTION - 
_Widget_Text_Edit = None
_Path = None
##-*!SECTION - 


## This is our initial method that will b
def testing(self = None, value="None Given", widget_value = None):

    # global variable so, it can be accessed
    global _Widget_Text_Edit

    # NOTE - initialize variables from main.py
    _Widget_Text_Edit = widget_value


    print ("Got Called")

    # seperate proccess to upload file
    # start_seperate_proccess(value)
    # upload_to_baidu()








## SECTION -  Below are methods that will be 
#  Callded from the woker class method ------------------------------------------------------->
def is_zip_file(path):
    return zipfile.is_zipfile(path)

##-*!SECTION ------------------------------------------------------------------------------/>



## Will start a new proccess
def start_seperate_proccess( value ):
    # initialize thread
     start_unzipping ( value )


## Uploaded file will be Unzipped
def start_unzipping(value):
    print("Value ",value)

    # show hints
    show_hints_by_print_to_the_widget( "Got the file location " + value + " will start unzipping  " )

    # prepare the uploaded file location 
    # value = r"" + value
    # Archive( value ).extractall('./module/temp')

    # start to upload to baidu yun
    return True


## From temp folder uplaod directory to the Baidu YUn
def upload_to_baidu():
    # show hints
    show_hints_by_print_to_the_widget( "Start uploading to Baidu pls wait..... " )

    bp.upload(r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\test3_adding_UI_for_future_functional\module\temp", "ONDUP")
    print(bp.list())   



""" ==========================START=============================== """
""" COMMON METHODS to give data to the UI"""

## This method will print data
def show_hints_by_print_to_the_widget(text):
    _Widget_Text_Edit.setText( text )


""" ===========================END================================= """
