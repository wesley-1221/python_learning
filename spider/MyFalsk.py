# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月07日
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

