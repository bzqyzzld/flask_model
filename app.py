# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/15 0:22
from ext import create_app
from flask_script import Manager

app = create_app()

if __name__ == "__main__":
    app.run()