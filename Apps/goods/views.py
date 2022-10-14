# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 22:41

from . import good_print


@good_print.route("/")
def hello():
    return "goods hello"

