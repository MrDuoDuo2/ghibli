#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
app.py 只负责访问入口相关的代码
"""

from flask import url_for
from flask import jsonify
from flask import render_template
from flask import redirect
from common import app
from common import config


@app.route('/')
@app.route("/?<msg>", methods=["GET"])
def index(msg=None):
    return render_template('index.html', msg=msg)


@app.route("/add_film", methods=["GET"])
def add_html():
    return render_template('add.html')


@app.route("/get_film_list", methods=["GET"])
def films():
    from views import get_film_list

    return jsonify(get_film_list())


@app.route("/get_film_info", methods=["GET"])
def get_film_info():
    from views import get_film_info

    film = get_film_info()

    return render_template('info.html', film=film)


@app.route("/delete_film", methods=["POST"])
def del_film():
    from views import delete_film

    result = delete_film()

    return redirect(url_for('index', msg=result))


@app.route("/add_film", methods=["POST"])
def add_film():
    from views import add_film

    result = add_film()

    return redirect(url_for('index', msg=result))


if __name__ == '__main__':
    app.debug = config.debug
    app.run(
        host=config.listen,
        port=config.port
    )
