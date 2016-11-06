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

    def post(self):

        redis = datastore.get_datastore()
        # get a dicht from the response
        responcse_as_dict = request.get_json(force=True)
        idcounter = {}
        idcounter['id'] = redis.llen('activities')
        activity = dict(responcse_as_dict, **idcounter)
        print activity
        redis.lpush('activities', json.dumps(activity) )
        return activity, 201

