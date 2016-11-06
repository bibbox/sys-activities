from flask import Flask
from flask_restful import Resource, Api, fields, marshal, reqparse
from activities.common import datastore

app = Flask(__name__, static_url_path="")

datastore.init(app)
api = Api(app)

