# -*- coding: utf-8 -*-
# Author    : ld
# Date      : 2022/12/2 18:11

workers = 4
bind = "0.0.0.0:8005"

accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"