from flask import Flask
from flask_restful import Resource, Api, fields, marshal, reqparse
from flask_httpauth import HTTPBasicAuth
from activities.common import datastore

from activities.resources.activity import ActivityAPI
from activities.resources.activity_list import ActivityListAPI

print "APP STARTED"

app = Flask(__name__)
datastore.init(app)

api =   Api(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


api.add_resource(ActivityListAPI, '/activities/api/v1.0/activities',      endpoint='activities')
api.add_resource(ActivityAPI, '/activities/api/v1.0/activities/<int:id>', endpoint='activity')

if __name__ == '__main__':
    app.run(debug=True)
