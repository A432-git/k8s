#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: yangtao
@contact:yangtao584@126.com
@version: 1.0.0
@license: Apache Licence
@file: app.py
@time: 21/10/21 19:24
"""
from flask import Flask
import socket,os
from redis import Redis

app = Flask(__name__)
if os.environ.get("envname") == "k8s":
    redis_server = os.environ.get("REDIS_MASTER_SR_SERVICE_HOST")
    redis_port = os.environ.get("REDIS_MASTER_SR_SERVICE_PORT")
    redis = Redis(host=redis_server, port=redis_port)

else:
    redis = Redis(host="192.168.0.118", port=6379)


@app.route("/")
def hello():
    count = redis.incr('hits')
    hostname = socket.gethostname()
    return f'hello world from ' \
           f'{hostname}' \
           f'Visited at {count}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)