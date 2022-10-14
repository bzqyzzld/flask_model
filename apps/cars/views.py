# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 22:40

from . import cars_print


@cars_print.route("/")
def hello():
    return "cars hello"

