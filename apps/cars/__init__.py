# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 22:37


from flask import Blueprint


cars_print = Blueprint("cars", __name__, url_prefix="/cars")

from . import views
