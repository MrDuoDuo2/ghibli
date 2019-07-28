#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
app.py 只负责访问入口相关的代码
"""

from flask import Flask
from flask import jsonify
from flask_cors import *

app = Flask(__name__)
CORS(app, resources=r'/*')

# 不使用 ascii 编码来序列化JSON对象
# 显示中文
app.config['JSON_AS_ASCII'] = False


@app.route("/", methods=["GET"])
def hello():
    return "<h1>Hello World!<h1>"


@app.route("/films", methods=["GET"])
def films():
    from views import get_films

    return jsonify(get_films())


if __name__ == '__main__':
    app.debug = True
    app.run()
