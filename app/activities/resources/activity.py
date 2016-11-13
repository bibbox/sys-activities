import pickle
import json
from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, fields, marshal, reqparse, request
from common import datastore

class ActivityAPI(Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        super(ActivityAPI, self).__init__()

    def get(self, id):

        redis = datastore.get_datastore()
        akey = "activity:" + str(id);

        activity = {}
        activityencoded = redis.hget ('activitieshash', akey)
        if activityencoded != None: activity = pickle.loads( activityencoded)

        if len(activity) == 0:
            abort(404)

        return activity, 200

    def put(self, id):

        redis = datastore.get_datastore()
        akey = "activity:" + str(id);
        activity = pickle.loads( redis.hget ('activitieshash', akey))

        print (activity)
        inputvalues = request.get_json(force=True)

        print (inputvalues)
        for k,v in inputvalues.iteritems():
            activity[k] = v


        akey = "activity:" + str(  activity['id'] )
        position =  activity['id']

        redis.hset ('activitieshash', akey, pickle.dumps(activity))

        if (activity['state'] == "FINISHED"):
             redis.zrem ('sortet-activities:notfinished', akey)
             redis.zadd ('sortet-activities:finished', position, akey)
        else:
             redis.zrem ('sortet-activities:finished', akey)
             redis.zadd ('sortet-activities:notfinished', position, akey)

        if len(activity) == 0:
            abort(404)
        return activity, 201

    def delete(self, id):
         redis = datastore.get_datastore()
         akey = "activity:" + str(id);
         l = redis.hdel ('activitieshash', akey)
         logkey = "activity:" + str(id) + ":logs"
         ll = redis.lrem(logkey)
         if l == 0:
            abort(404)
         return {'result': True}
