import os

class DBCredentials():

    credentials = {
        "dbname":os.environ['dbname'], 
        "user":os.environ['user'], 
        "password":os.environ['password'], 
        "host":os.environ['host'], 
        "port":"5432"
    }


