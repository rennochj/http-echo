from flask import Flask
from flask import request
from flask import make_response
from json import dumps
from time import sleep

app = Flask(__name__)

@app.route('/wait', methods=['GET'])
def wait_http_echo():
    sleep(10)
    return http_echo()

@app.route('/', methods=['GET'])
def http_echo():

    message = {}
    headers = {}
    
    for item in request.headers.to_wsgi_list():
        headers[item[0]] = item[1]

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
 
    response = make_response(dumps(message, sort_keys=True, indent=4))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = 200

    return response



    