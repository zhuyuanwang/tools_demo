# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 22:53
# @Author  : Circleone_

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello zyw"

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=8080)