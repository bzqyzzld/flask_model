# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 23:30

from ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)



