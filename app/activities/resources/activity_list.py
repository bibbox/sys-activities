import pickle
import json
import redis
from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, fields, marshal, reqparse, request
from common import datastore


class ActivityListAPI(Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        super(ActivityListAPI, self).__init__()

    def get(self):
        redis = datastore.get_datastore()
        finished = request.args.get('finished')

        start = 0
        end = -1
        if 'offset' in request.args:  start = int( request.args.get('offset'))
        if 'limit' in request.args:   end = start + int(request.args.get('limit')) -1


		cAll = redis.zcount ('sortet-activities:all', '-inf', '+inf')
        cFinished = redis.zcount ('sortet-activities:finished', '-inf', '+inf')
        cNotFinished = cAll - cFinished

        if (finished == 'true'):
            actKeys = redis.zrevrange ('sortet-activities:finished', start, end)
			total = cFinished
        else:
            actKeys = redis.zrevrange ('sortet-activities:all', start, end)
			total = cAll
			
        allActivities = []
        for k in actKeys:
            activityencoded = redis.hget('activitieshash', k)
            if activityencoded != None:
                activity = pickle.loads(activityencoded)
                activity['url'] = request.url + "/" +   str(activity['id'])
                allActivities.append(activity)

       
        limit = end - start + 1
        resultset = {"count": len(actKeys), "total": total, offset":start, "limit" :limit, "pending":cNotFinished}
        fullresponse = {"metadata" :resultset, "content" : allActivities}
        return fullresponse, 200


    def post(self):
        redis = datastore.get_datastore()

        # get a dict from the response
        activity = request.get_json(force=True)

        position = int(redis.get ('activityindex'))
        redis.incr ('activityindex', 1)
        activity['id'] =  str(position)

        akey = "activity:" + str(  activity['id'] )
        redis.hset ('activitieshash', akey, pickle.dumps(activity))

        redis.zadd ('sortet-activities:all', position, akey)
        if (activity['state'] == "FINISHED"):
             redis.zadd ('sortet-activities:finished', position, akey)
        else:
             redis.zadd ('sortet-activities:notfinished', position, akey)
        return activity, 201


