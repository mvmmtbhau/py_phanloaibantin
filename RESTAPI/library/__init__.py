from flask import Flask, request, Blueprint

from .phan_loai.controller import routes

def create_app(config_file = "config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(routes)
    return app