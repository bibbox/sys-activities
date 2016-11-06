import json
from flask import Flask, jsonify
from flask_restful import Resource, Api, fields, marshal, reqparse, request
from activities.common import datastore

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
        json_data = request.get_json(force=True)
        redis = datastore.get_datastore()
        redis.lpush('activities', json.dumps(json_data) )
        return json_data, 201

