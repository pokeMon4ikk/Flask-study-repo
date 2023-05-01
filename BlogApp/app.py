from time import time
from flask import Flask, request, g
import socket

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return 'Hello'
