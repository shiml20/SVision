from flask import Flask
from myApp.config import Config
from .extensions import config_extensions
from .Views import auth_bp, fac_bp, info_bp, monitor_bp,\
    usr_bp, veh_bp, vis_bp, warehouse_bp, warn_bp
import os
# 工厂函数
def create_app():
    app = Flask(__name__)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_object(Config)

    config_extensions(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(fac_bp)
    app.register_blueprint(info_bp)
    app.register_blueprint(monitor_bp)
    app.register_blueprint(usr_bp)
    app.register_blueprint(veh_bp)
    app.register_blueprint(vis_bp)
    app.register_blueprint(warehouse_bp)
    app.register_blueprint(warn_bp)
    return app
