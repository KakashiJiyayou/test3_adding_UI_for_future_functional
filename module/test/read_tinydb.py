from tinydb import TinyDB, Query


db = TinyDB( './DB/db.json' )

table = dir_list_table  = db.table( 'dir_list' )

query = Query()

print ("dir list  ", table.count( query.path == "/软件编制 资料/发票设备/QV设备15套.doc")  )