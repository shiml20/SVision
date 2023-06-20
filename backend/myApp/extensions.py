# 第三方插件
from flask_sqlalchemy import SQLAlchemy  # 数据库
from flask_migrate import Migrate
from flask_cors import CORS  # 处理跨域请求

# 数据库
db = SQLAlchemy()
# 迁移模型
migrate = Migrate()
# 跨域
cors = CORS()


def config_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db=db)
    cors.init_app(app)
