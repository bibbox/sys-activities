import os
import redis

from flask import Flask, make_response, jsonify
from flask_restful import Resource, Api, fields, marshal, reqparse
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")

print "REDIS INIT"

if os.environ.has_key('PYCHARM_HOSTED'):
    print "RUNNING IN DEBUG MODE"
    app.redis = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, password="devpassword")
else:
    print "RUNNING IN DOCKER"
    app.redis = redis.StrictRedis(host='instancetaskmanager_redis_1', port=6379, db=0, password="devpassword")

app.redis.append("heimo", "ist wirklich der beste # ")
print app.redis.get("heimo")

print "REDIS OK"

api = Api(app)

activities = [
    {
        'id': 1,
        'title': u'Install APP',
        'description': u'INSTALL the TASK MANAGER Openspecimen',
        'done': False
    },
    {
        'id': 2,
        'title': u'Stop Instance',
        'description': u'Stop the Instance 7',
        'done': False
    }
]

activity_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('activity')
}



