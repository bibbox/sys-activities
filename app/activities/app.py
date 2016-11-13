from flask import Flask
from flask_restful import Resource, Api, fields, marshal, reqparse
from flask_httpauth import HTTPBasicAuth
from common import datastore
from common import graphdatabase

from resources.activity import ActivityAPI
from resources.activity_list import ActivityListAPI
from resources.log_list import LogListAPI
from resources.activity_commands import ActiviyListReset

print ("APP STARTED")

app = Flask(__name__)
datastore.init(app)
graphdatabase.init(app)

api =   Api(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None
'''
@app.errorhandler(Exception)
def all_exception_handler(error):
   return 'Some Python Error appeared', 500
'''

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


api.add_resource(ActiviyListReset, '/activities/api/v1.0/reset',          endpoint='reset')
api.add_resource(ActivityListAPI, '/activities/api/v1.0/activities',      endpoint='activities')
api.add_resource(ActivityAPI, '/activities/api/v1.0/activities/<int:id>', endpoint='activity')
api.add_resource(LogListAPI, '/activities/api/v1.0/activities/<int:id>/logs', endpoint='logs')


if __name__ == '__main__':
    app.run(debug=True)
