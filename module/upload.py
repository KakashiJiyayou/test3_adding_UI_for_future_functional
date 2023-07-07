import os
import glob
import time
import shutil
import _thread
import zipfile
from bypy import ByPy
from pyunpack import Archive


bp = ByPy()



def is_zip_file(path):

    is_true = False
    status = "Ok"

    try:
        is_true = zipfile.is_zipfile(path)
    except:
        status = "error"

    return is_true


def clear_temp_dir():

    clear_done = True
    status = "ok"
    try:
        path = get_directory_path()
        # search each content and delete them
        for root, dirs, files in os.walk( path ):
            for name in files:
                shutil.rmtree( os.path.join( root, name ) )
            for name in dirs:
                shutil.rmtree( os.path.join( root, name ) )

    except:
        status = "Erorr removing contents"
        clear_done = False
    
    json_value = { "clear_temp_dir": clear_done, "status":status }
    return json_value


## Uploaded file will be Unzipped
def start_unzipping(path):

    unzipped = True
    status = "ok"
    print("Value ",value)

    try:
        # prepare the uploaded file location 
        value = r"" + value
        Archive( value ).extractall('./module/temp')
    except:
        unzipped = False
        status = "Could not unzipped"

    json_value = { "start_unzipping" : False, "status" : status }

    return json_value


## get folder list as JSON
def get_folder_list():
    path_list = os.listdir( get_directory_path() )

    return path_list



## From temp folder uplaod directory to the Baidu YUn
def upload_to_baidu():
    bp.upload(r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\test3_adding_UI_for_future_functional\module\temp", "ONDUP")
    print(bp.list())   



### common methods
def get_directory_path():
    # will get current python working directory
    cwd = os.path.dirname( os.path.abspath( __file__ ) )
    
    # add folder path to the working dire
    # y
    path = cwd + "/module/temp"
    return path




""" ==========================START=============================== """
""" COMMON METHODS to give data to the UI"""




""" ===========================END================================= """
