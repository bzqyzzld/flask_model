# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 22:37


from flask import Blueprint


good_print = Blueprint("goods", __name__, url_prefix="/goods")

from . import views
