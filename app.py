from flask import Flask
from flask import request
from flask import make_response
from json import dumps
from time import sleep
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from aws_xray_sdk.core import xray_recorder
import os

app = Flask(__name__)

xray_recorder.configure(service='htt-echo')
XRayMiddleware(app, xray_recorder)

@app.route('/wait', methods=['GET'])
def wait_http_echo():
    sleep(10)
    return http_echo()

@app.route('/', methods=['GET'])
def http_echo():

    message = {}
    headers = {}
    environment = {}
    
    for item in request.headers.to_wsgi_list():
        headers[item[0]] = item[1]

    for key in request.environ.keys():
        value = request.environ[key]
        if type(value) is str or type(value) is tuple or type(value) is int or type(value) is list or type(value) is dict:
            environment[key] = value

    print(environment)

    message["path"] = request.path
    message["full_path"] = request.full_path
    message["remote_addr"] = request.remote_addr
    message["url"] = request.url
    message["scheme"] = request.scheme
    message["args"] = request.args
    message["base_url"] = request.base_url
    message["headers"] = headers
    message["host"] = request.host
    message["host_url"] = request.host_url
    message["method"] = request.method
    message["origin"] = request.origin
    message["url_root"] = request.url_root
    message["url_charset"] = request.url_charset
    message["environment"] = environment
    message["host_ip"] = os.environ["HOST_IP"]
 
    response = make_response(dumps(message, sort_keys=True, indent=4))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = 200

    return response



    