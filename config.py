# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 23:38

import os

class DataBaseConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/newproj"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))