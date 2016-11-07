import pickle
import json
from flask import Flask, jsonify
from flask_restful import Resource, Api, fields, marshal, reqparse, request
from common import datastore

class ActivityListAPI(Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        super(ActivityListAPI, self).__init__()
        redis = datastore.get_datastore()

    def get(self):
        redis = datastore.get_datastore()

        activitiesFromRedisDict = redis.hgetall('activitieshash')

        print activitiesFromRedisDict

        allActivities = []
        for k, v in activitiesFromRedisDict.items():
            activity =  pickle.loads(v)
            print k
            allActivities.append(activity)

        print json.dumps(allActivities)
        jsonString = json.dumps(allActivities)

        resultset = {"count": redis.hlen('activitieshash'), "offset":0, "limit" :-1}

        fullresponse = {"metadata" :resultset, "content" : allActivities}
        return fullresponse, 200


    def post(self):
        redis = datastore.get_datastore()

        # get a dict from the response
        activity = request.get_json(force=True)
        activity['id'] = redis.llen('activities-dict')
        redis.lpush('activities-dict', pickle.dumps(activity) )
        akey = "activity:" + str( redis.llen('activities-dict'))
        redis.hset ('activitieshash', akey, pickle.dumps(activity))
        return activity, 201




'''
CODEFRIEHOF
  activitiesFromRedis = redis.lrange('activities', 0, -1)
        allInOneString = "["
        c = 0;
        l = len (activitiesFromRedis)
        for a in activitiesFromRedis:
            allInOneString += a
            if (c<l-1): allInOneString += ","
            c += 1
        allInOneString += "]"
        return json.loads(allInOneString), 200

     redis.lpush('activities', json.dumps(activity) )


'''
