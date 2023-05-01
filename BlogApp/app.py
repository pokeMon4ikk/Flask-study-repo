from time import time
from flask import Flask, request, g
import socket

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return 'Hello'


# for test
@app.route("/getUserInfo", methods=["GET"])
def user():
    example_user_info = {'id': '1', 'name': 'Grisha', "surname": 'Glinkin', 'age': 22}
    got_id = request.args.get("id")

    if got_id == example_user_info['id']:
        return f"User name: {example_user_info['name']}, User surname: {example_user_info['surname']}, " \
               f"User age: {example_user_info['age']}"

    return "Hello, User"


@app.before_request
def process_before_request():
    g.start_time = time()


@app.after_request
def process_after_request(response):
    if hasattr(g, "start_time"):
        response.headers["Process-time"] = time() - g.start_time
        response.headers["User-IP"] = socket.gethostbyname(socket.gethostname())
        return response
