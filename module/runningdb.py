from tinydb import TinyDB, Query

# Create a TinyDB instance for the running database
running_db = TinyDB('./DB/running.json')

def open_connection ():
    global running_db
    running_db = TinyDB('./DB/running.json')

def close_connection ():
    global running_db
    running_db.close()



def change_status(status, user_id):
    # Check if the user is already in the database
    Running = Query()
    user_record = running_db.get(Running.user == user_id)

    if user_record is None:
        # If the user is not in the database, add a new record
        running_db.insert({'status': status, 'user': user_id})
    elif user_record['user'] == user_id:
        # If the user is in the database and matches the provided user_id, change the status
        running_db.update({'status': status}, Running.user == user_id)

def is_database_in_use():
    Running = Query()
    user_record = running_db.get(Running.status == 'running')

    if user_record is None:
        return False, None  # Database is free
    else:
        return True, user_record['user']  # Database is in use by user


def get_user_id():
    Running = Query()
    user_record = running_db.get(Running.status == 'running')

    if user_record is None:
        return None  # No user is currently using the database
    else:
        return user_record['user']  # Return the user ID using the database
