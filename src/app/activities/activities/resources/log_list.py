import pickle
import json
import redis
from flask import Flask, jsonify
from flask_restful import Resource, Api, fields, marshal, reqparse, request
from common import datastore

class LogListAPI(Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        super(LogListAPI, self).__init__()


    def get(self, id):
        redis = datastore.get_datastore()

        start = 0
        end = -1
        if 'offset' in request.args:  start = int( request.args.get('offset'))
        if 'limit' in request.args:   end = start + int(request.args.get('limit')) -1

        akey = akey = "activity:" + str(id) + ":logs"
        logsEncoded =  redis.lrange (akey, start, end)
        allLogs = []

        for l in logsEncoded:
            allLogs.append (pickle.loads(l))

        limit = end - start + 1
        resultset = {"count": len(allLogs), "offset": start, "limit": limit}
        fullresponse = {"metadata": resultset, "content": allLogs}
        return fullresponse, 200

    def post(self, id):
        redis = datastore.get_datastore()

        log = request.get_json(force=True)
        akey =  akey = "activity:" + str(id) + ":logs"
        redis.lpush (akey, pickle.dumps(log) )
        # get a dict from the response
        log = request.get_json(force=True)
        return log, 201

