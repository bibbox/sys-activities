from flask import Flask
from flask_restful import Resource, Api, fields, marshal, reqparse
from common import datastore

class ActivityAPI(Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(ActivityAPI, self).__init__()

    def get(self, id):
        activity = [activity for activity in activities if activity['id'] == id]
        if len(activity) == 0:
            abort(404)
        return {'activity': marshal(activity[0], activity_fields)}

    def put(self, id):
        activity = [activity for activity in activities if activity['id'] == id]
        if len(activity) == 0:
            abort(404)
        activity = activity[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                activity[k] = v
        return {'activity': marshal(activity, activity_fields)}

    def delete(self, id):
        activity = [activity for activity in activities if activity['id'] == id]
        if len(activity) == 0:
            abort(404)
        activities.remove(activity[0])
        return {'result': True}
