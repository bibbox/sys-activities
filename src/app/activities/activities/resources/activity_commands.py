import redis
import json
import os
import requests
from urllib.parse import urlsplit
from flask import Flask, jsonify
from flask_restful import Resource, Api, fields, marshal, reqparse, request
from common import datastore

import time
import _thread
import threading
from threading import Thread

class ActiviyListReset (Resource):
#    decorators = [auth.login_required]

    def __init__(self):
        super(ActiviyListReset, self).__init__()

    def get(self):
        redis = datastore.get_datastore()
        redis.flushall();
        redis.set ('activityindex', "0")
        return "SUCESS", 200





