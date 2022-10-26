# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 22:41

from . import good_print
from Models.UserModel import User, db


@good_print.route("/")
def hello():
    r = db.session.query(User.id).filter(User.name == "张三").all()
    print(222, r, 111)
    return "goods hello"

