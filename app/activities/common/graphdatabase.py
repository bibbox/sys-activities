from flask import g
import os
import pyorient

_orientdb_config = None # Holds database config

def init(app):
    """ Function must be called to initalize this module """
    global _db_config
    global close_connection
#   _db_config = app.config['DATABASE']
#    Manually apply @app.teardown_appcontext decorator
#    close_connection = app.teardown_appcontext(close_connection)


def _graphdatabase_connect():
#    if _db_config is None:
#        raise Exception('Call init first') # or whatever error you want

    try:
        if 'PYCHARM_HOSTED' in os.environ.keys():
            client = pyorient.OrientDB("127.0.0.1", 2424)
            return  client.db_open( "activities-v1", "bibboxadmin", "bibbox4ever" )
        else:
            client = pyorient.OrientDB("sys-activities-orientdb", 2424)
            return   client.db_open( "activities-v1", "bibboxadmin", "bibbox4ever" )
    except:
        print ("ERROR cannot conenct to orientDB")
        raise

def get_graphdatabse():
    orientDBclient  = getattr(g, '_orientDBclient', None)
    if orientDBclient is None:
        orientDBclient = g._orientDBclient = _graphdatabase_connect()
    return orientDBclient

def close_connection(exception):
    orientDBclient = getattr(g, '_orientDBclient', None)
    if orientDBclient is not None:
        # TODO close and cleanup orientDB connection, is there anything to do
        print("Close the connection")