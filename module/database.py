import datetime
from tinydb import TinyDB, Query



# path for db
db = TinyDB( './DB/db.json' )


# SECTION Directory table
# NOTE - table column structure :
#        path , created_at, updated_at,   created_by, last_modified , update_by

# create_table_for folder list
dir_list_table  = db.table( 'dir_list' )


# insert value to the 'dir_list'
def insert_dir_list( list ):
    global dir_list_table

    user_info = get_logge_user_info()
    query = Query()

    for path in list:

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
                "updated_by" : None
            } )

        insert_done = True
        status = "ok"

    value = { "insert_done": insert_done, "status": status }
    return value

# !SECTION


## NOTE - Common methods for all to use
def get_logge_user_info ( ) :
    # send user_name and user_id
    value = { "user_name" : "Super Admin" , "user_id": 1 }
    return value

