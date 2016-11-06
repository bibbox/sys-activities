from flask import g
import os
import redis


_db_config = None # Holds database config

def init(app):
    """ Function must be called to initalize this module """
    global _db_config
    global close_connection
#   _db_config = app.config['DATABASE']
#    Manually apply @app.teardown_appcontext decorator
#    close_connection = app.teardown_appcontext(close_connection)


def _datastore_connect():
#    if _db_config is None:
#        raise Exception('Call init first') # or whatever error you want

    try:
        if os.environ.has_key('PYCHARM_HOSTED'):
            print "RUNNING IN DEBUG MODE"
            return redis.StrictRedis(host='127.0.0.1', port=6379, db=0, password="devpassword")
        else:
            print "RUNNING IN DOCKER"
            return redis.StrictRedis(host='instancetaskmanager_redis_1', port=6379, db=0, password="devpassword")
    except:
        print "No connection to redis"
        pass

def get_datastore():
    datastore  = getattr(g, '_datastore', None)
    if datastore is None:
        datastore = g._datastore = _datastore_connect()
    return datastore

def close_connection(exception):
    datastore = getattr(g, '_datastore', None)
    if datastore is not None:
        print "xxx"