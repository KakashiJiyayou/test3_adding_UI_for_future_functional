import os
import glob
import time
import shutil
import _thread
from zipfile import ZipFile
from bypy import ByPy
from pyunpack import Archive


bp = ByPy()

path_list = []

def is_zip_file(path):

    is_true = False
    status = "Ok"

    try:
        is_true = ".zip" in str(path)
    except:
        status = "error"
        is_true = False

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
def start_unzipping( path ):

    unzipped = True
    status = "ok"
    print( "Value ",path )

    try:
        # prepare the uploaded file location 
        value = r"" + path
        # with ZipFile ( value, "r" ) as zObj:
        #     zObj.extractall ( path= './module/temp'  )
        
        Archive( path ).extractall( './module/temp' )
    except:
        unzipped = False
        status = "Could not unzipped"

    json_value = { "start_unzipping" : unzipped , "status" : status }

    return json_value


## get folder list as JSON
def get_folder_list():
    global path_list
    path_list = []
    folder_list()
    return path_list
    

def folder_list( rootDir = None ):
    global path_list
    if rootDir is  None:
        rootDir =  get_directory_path() 

    for lists in os.listdir( rootDir ):
        path_list.append( lists )
        print ( "From upload module path ", lists )
        p = os.path.join( rootDir, lists)

        if os.path.isdir( p ):
            folder_list( p )


## From temp folder uplaod directory to the Baidu YUn
def upload_to_baidu():
    rootDir = get_directory_path()
    folder_name = os.listdir ( rootDir )[0]
    path = r""+ os.path.join( rootDir, folder_name )
    bp.upload( path, "ONDUP" )
    print(bp.list())   



### common methods
def get_directory_path():
    # will get current python working directory
    cwd = os.path.dirname( os.path.abspath( __file__ ) )
    
    # add folder path to the working dire
    # y
    path =  os.path.join ( cwd , "temp")
    return path




""" ==========================START=============================== """
""" COMMON METHODS to give data to the UI"""




""" ===========================END================================= """
