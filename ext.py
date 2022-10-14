# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/10/14 23:26

from flask import Flask
from Apps.cars import cars_print
from Apps.goods import good_print
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DataBaseConfig

db = SQLAlchemy()
migrate = Migrate()




def create_app():
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(DataBaseConfig)

    app.register_blueprint(cars_print)
    app.register_blueprint(good_print)

    # 注册sqlalchemy
    db.init_app(app)

    # 注册migrate
    from Models.UserModel import User
    migrate.init_app(app, db)
    return app
