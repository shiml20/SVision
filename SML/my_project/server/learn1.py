from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import config_map

# # configuration
# DEBUG = True

# create database
db = SQLAlchemy()

# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name: str 配置模式的名字 ("develop", "product")
    :return:
    """
    app = Flask(__name__)

    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 使用app初始化db
    db.init_app(app)

    return app

# instantiate the app
app = create_app("develop")

class users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    date = db.Column("date", db.String(100))
    name = db.Column("name", db.String(100))
    address = db.Column("address", db.Boolean)

    def __init__(self, date, name, address):
        self.date = date
        self.name = name
        self.address = address

    def jsondata(self):
        _jsondata = {
            'date': self.date,
            'name': self.name,
            'address': self.address,
        }
        return _jsondata

