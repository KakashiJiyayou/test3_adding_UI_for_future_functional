import os
import pip
import sys
import time

import pkgutil
import importlib.util
import traceback
import subprocess
# from subprocess import CREATE_NEW_CONSOLE, run
from enum import Enum

class Color(Enum):
    PUPLE = 95
    CYAN = 96
    DARK_CYAN = 36
    BLUE = 94
    GREEN = 92
    YELLOW = 93
    RED = 31
    # (Add any further colors you want to use...)

def color_print(text, color):
    """Print text in the specified color."""
    
    print(f'\033[{color.value}m{text}\033[0m')


# set initiale package list
list_package = [
    { "name" : "PyQt5", "installed" : False },
    { "name" : "tinydb", "installed" : False },
    { "name" : "markdown_to_json", "installed" : False },
    { "name" : "ntpath", "installed" : False },
    { "name" : "bypy", "installed" : False }
]


def package_installed ( package_name ):
    try:
        
        eggs_loader = pkgutil.find_loader(package_name)
        found = eggs_loader is not None
        # found = importlib.util.find_spec(package_name)
        return found
    except:
        return False
    


# def isntall_library ( package_name ):
#     try :
#         # pip._internal
#         # pip.main(['install', package_name])
#         string = "pip install " + str ( package_name)
#         os.system(string)
#         # subprocess.call([ 'pip', 'install', package_name], creationflags=subprocess.CREATE_NEW_CONSOLE)
#         # subprocess.([sys.executable, "-m",  "pip", "install", package_name])
#     except:
#         traceback.print_exc() 


def packages_check_installed ():
    for item in list_package:
        is_installed = package_installed ( item["name"] )

        if is_installed:
            item["installed"] = True
        else:
            print (" installing library pls wait, it can take 10 mins ")
       

def close_application_if_package_not_installed():
    packages_not_installed = False
    for item in list_package:
        is_installed = package_installed ( item["name"] )

        if not is_installed:
            packages_not_installed = True

    if packages_not_installed:
        color_print ( "Pls Installed the missing packages", Color.PUPLE )
        color_print ( list_package , Color.BLUE)
        print ( "" )
        time.sleep (20)
        sys.exit()

# def is_url( link ):
#     if "https://openapi.baidu.com/oauth"in link:
#         return True
#     else :
#         return False


def check_bypy_information (  ):
    try:
        subprocess.call([ "bypy", "list"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except:
        traceback.print_exc()
        

packages_check_installed ()
time.sleep(4)
close_application_if_package_not_installed()
check_bypy_information ()


    