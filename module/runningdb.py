from tinydb import TinyDB, Query, where

# Create a TinyDB instance for the running database
running_db = TinyDB('./DB/running.json')

def open_connection ():
    global running_db
    running_db = TinyDB('./DB/running.json')

def close_connection ():
    global running_db
    running_db.close()



def change_status ( given_status, given_user_id ):

    status_from = running_db.get(doc_id=1)["status"].strip()
    user_id_from = running_db.get(doc_id=1)["user_id"].strip()

    given_status = given_status.strip()
    given_user_id = given_user_id.strip()

    # print("From Database user_id_from *", user_id_from, "*\t status *", status_from,"*")
    # print("From Given da user_id_from *", given_user_id, "*\t status *", given_status,"*")

    status = "not started"
    change_status = False
    result = given_status

    if status_from == "free":
        running_db.update({'status': given_status, 'user_id': given_user_id},  doc_ids=[1])
        status = "ok"
        change_status = True

    elif ( status_from == "running" ) and ( user_id_from == given_user_id ) :
        running_db.update({'status': given_status, 'user_id': given_user_id},  doc_ids=[1])
        status = "ok"
        change_status = True

    elif ( status_from == "running" ) and ( user_id_from != given_user_id ) :
        status = "User ID does not matched with "
        change_status = False

    status_from = running_db.get(doc_id=1)["status"].strip()
    json = { "status" : status, "expected_result": result, "original_result": status_from, "status_changed" : change_status }

    return  json



def is_database_in_use():
    status_from = running_db.get(doc_id=1)["status"].strip()
    user_id_from = running_db.get(doc_id=1)["user_id"].strip()

    if status_from == "free":
        return False, user_id_from  # Database is free
    else:
        return True, user_id_from  # Database is in use by user



def get_user_id():
    
    user_id_from = running_db.get(doc_id=1)["user_id"].strip()

    return user_id_from
