# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/15 0:22
from ext import init_app
from flask_script import Manager
from flask import Flask


app = Flask(__name__)

init_app(app)

if __name__ == "__main__":
    app.run()