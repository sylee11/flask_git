from flask import Flask, Response, Request
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig
from .rest.user import user_blueprint

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    # db.create_all()
    app.register_blueprint(user_blueprint)

    return app