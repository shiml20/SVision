

class Config(object):
    """"配置信息"""
    SECRET_KEY = "hello"

    #数据库
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JSON_AS_ASCII = False

class DevelopmentConfig(Config):
    """"开发者模式配置信息"""
    DEBUG = True

class ProductionConfig(Config):
    """"生产环境配置信息"""
    pass

config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}