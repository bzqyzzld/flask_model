# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 22:18
from flask_script import Manager
from app import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
