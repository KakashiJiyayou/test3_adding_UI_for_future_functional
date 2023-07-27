import os
import glob
import time
import shutil
import _thread
from zipfile import ZipFile
from bypy import ByPy
from pyunpack import Archive
import traceback


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
                os.remove( os.path.join( root, name ) )
            for name in dirs:
                try :
                    os.rmdir( os.path.join( root, name ) )
                except:
                    shutil.rmtree ( os.path.join( root, name ) )
                

    except:
        status = "Erorr removing contents"
        clear_done = False
        traceback.print_exc ()
    
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
        traceback.print_exc()

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

    delete_rootDir = get_directory_path() 
    if rootDir is  None:
        rootDir =  get_directory_path() 
        delete_rootDir = rootDir

    print ( "From uplaod moduel roodDIr", rootDir)

    for path, subdirs, files in os.walk(rootDir):

        for name in files:
            p = os.path.join(path, name)
        
            print ( "From upload module path ", p)
            # put in the list if it's only file
            if os.path.isfile (p):
                path_list.append( p.replace( delete_rootDir , "" ) )

        


# copy file one folder to another
def copy_file_to_temp ( file_path_on_pc, symlinks=False, ignore=None ):

    status = None
    copy_done = False
    dst = get_directory_path ()

    try :
        
        for item in os.listdir(file_path_on_pc):
            s = os.path.join(file_path_on_pc, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
    except :
        status = "error"
        print ( "failled to copy " )
        traceback.print_exc()

    json_value = { "copy_file_to_temp" : copy_done, "status" : status }   



    return json_value


# rename file in the temp  folder
def rename_file_in_temp ( selected_file_name, rename_to ):

    file_renamed = False
    status = None
    
    try :
        rootDir = get_directory_path ()
        selected_file_path = os.path.join ( rootDir, selected_file_name )
        after_name_file_path = os.path.join ( rootDir, rename_to)
        os.rename ( selected_file_path , after_name_file_path )
        file_renamed = True
        status = "ok"
    except :
        status = "error"

    json_value = { "rename_file_in_temp" : file_renamed, "status" : status }   
    return json_value


#FIXME -  - we will use subproccess to do this, we willnot be using this one
## From temp folder uplaod directory to the Baidu YUn
def upload_to_baidu( remotePath  = ""):
    rootDir = get_directory_path()
    # folder_name = os.listdir ( rootDir )[0]
    # path = r""+ os.path.join( rootDir, folder_name )
    ONDUP = "ONDUP/" + remotePath
    bp.upload( rootDir, ONDUP)

    print(bp.list())   


# this is shell command in list
def get_bypy_upload_command ( remotePath = "" ) :
    ONDUP = "ONDUP/" + remotePath

    # TODO - later use another mofule get destination directory
    command =  [ "bypy", "upload", get_directory_path(), ONDUP ]
    return command



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
