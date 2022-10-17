# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 23:26

from flask import Flask
from Apps.cars import cars_print
from Apps.goods  import good_print
from Models.BaseModel import db
from flask_migrate import Migrate
from config import DataBaseConfig

migrate = Migrate()




def init_app(app):
    # 加载配置
    app.config.from_object(DataBaseConfig)

    # 注册sqlalchemy
    db.init_app(app)

    app.register_blueprint(cars_print)
    app.register_blueprint(good_print)


    # 注册migrate
    migrate.init_app(app, db)
