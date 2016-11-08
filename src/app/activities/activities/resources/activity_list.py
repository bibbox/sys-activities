import pickle
import json
from flask import Flask, jsonify
from flask_restful import Resource, Api, fields, marshal, reqparse, request
from common import datastore

class ActivityListAPI(Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        super(ActivityListAPI, self).__init__()


    def get(self):
        redis = datastore.get_datastore()


        print request.url

        finished = request.args.get('finished')
        offset = request.args.get('offset')
        limit = request.args.get('limit')

        # TODO implement offset and limit using ZSCAN

        if (finished == 'true'):
            actKeys = redis.zrevrange ('sortet-activities:finished', 0, -1)
        else:
            actKeys = redis.zrevrange ('sortet-activities:all', 0, -1)

        allActivities = []
        for k in actKeys:
            activity = pickle.loads( redis.hget ('activitieshash', k))
            allActivities.append(activity)

        print json.dumps(allActivities)
        jsonString = json.dumps(allActivities)

        resultset = {"count": len(actKeys), "offset":0, "limit" :-1}

        fullresponse = {"metadata" :resultset, "content" : allActivities}
        return fullresponse, 200


    def post(self):
        redis = datastore.get_datastore()

        # get a dict from the response
        activity = request.get_json(force=True)
        aid = int (redis.llen('activities-dict'))
        print aid
        activity['id'] = aid
        redis.lpush('activities-dict', pickle.dumps(activity) )

        akey = "activity:" + str( redis.llen('activities-dict'))
        redis.hset ('activitieshash', akey, pickle.dumps(activity))

        redis.zadd ('sortet-activities:all', aid, akey)
        if (activity['state'] == "FINISHED"):
             redis.zadd ('sortet-activities:finished', aid, akey)
        else:
             redis.zadd ('sortet-activities:notfinished', aid, akey)

        redis.hset ('activitieshash', akey, pickle.dumps(activity))

        return activity, 201
