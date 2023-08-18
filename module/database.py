import datetime
import traceback
from tinydb import TinyDB, Query , where

db = TinyDB( './DB/db.json' )

def open_db_connection ():
    global db ,dir_list_table 
    # path for db
    db = TinyDB( './DB/db.json' )
    
    dir_list_table  = db.table( 'dir_list' )

def close_db_connection():
    global db
    db.close()


# SECTION Directory table
# NOTE - table column structure :
#        path , created_at, updated_at,   created_by, last_modified , update_by

# create_table_for folder list
dir_list_table  = db.table( 'dir_list' )


# insert value to the 'dir_list'
# NOTE - for inserting 
def insert_dir_list( list, menu = None ):
    global dir_list_table

    print ("insert DB path ", list)

    user_info = get_logge_user_info()
    query = Query()
    insert_done = False
    status = None

    path = list
    if path:
        print ("insert DB path  for path in list", path)

        status = "Error"
        insert_done = False

        #first check whether value exist or not
        try:
            path_exists = dir_list_table.count ( query.path == path )
        except:
            path_exists = False
            print (" Error while counting in 'path_exists'")
        

        if path_exists >0:
            status = "path already exists"
        else :
            created_at = str ( datetime.date.today() )
            path =""+ str ( path ) +""
            # path = path.encode ( "utf-8" )
            dir_list_table.insert ( { 
                "path" : path,
                "created_at" : created_at,
                "updated_at" : None,
                "created_by" : user_info,
                "updated_by" : None,
                "sku_filter" : menu
            } )

            insert_done = True
            status = "ok"

    value = { "insert_done": insert_done, "status": status }
    return value


# def insert_dir ( path, menu ):
#     try:
#         user_info = get_logge_user_info ()
#         created_at = str ( datetime.date.today() )
#         path =""+ str ( path ) +""
#         # path = path.encode ( "utf-8" )
#         dir_list_table.insert ( { 
#             "path" : path,
#             "created_at" : created_at,
#             "updated_at" : None,
#             "created_by" : user_info,
#             "updated_by" : None,
#             "sku_filter" : menu
#         } )

#         insert_done = True
#         status = "ok"
#     except :
#         insert_done = False
#         status = "Error"


#     value = { "insert_done": insert_done, "status": status }
#     return value








# Query data
# NOTE - its for search completer 
# Later we can pass value with menu filter 
def get_dir_list( menu ):
    menu = menu.strip (".")
    # print ( "get_dir_list menu  ", menu  )
    global dir_list_table

    path_list = Query()
    result = None
    try :
        result = [ item  for  item in dir_list_table.search (  path_list.path.exists ( )  ) ]
        temp_result = result
        result = []
        for item in temp_result:
            # print ( " get_dir menu ", item [ "sku_filter" ], "\t path ", item["path"])
            temp_path = item[ "path" ]
            temp_str_list = temp_path.split("/")
            last_str = temp_str_list[-1]
            if menu in item [ "sku_filter" ]:
                temp_value = last_str + "  Directory:" + temp_path
                result.append(temp_value)
    except Exception as e:
        print( traceback.format_exc() )
    return result


# 
def get_info_based_on_path ( path ) :
    path_list = Query()
    # ( where('subject') == 'MySQL' )
    result = dir_list_table.search ( ( where( 'path') == path)   & path_list.path.exists() ) 
    return result


#
def delete_path_list ( path ):
    status = None
    path_deleted = False
    try:
        qury = Query ()
        dir_list_table.remove ( qury.path == path )

        status = "ok"
        path_deleted = True
    except:
        print (" failled to delete data")




# !SECTION


## NOTE - Common methods for all to use
def get_logge_user_info ( ) :
    # send user_name and user_id
    value = { "user_name" : "Super Admin" , "user_id": 1 }
    return value

