import os

from flask import Flask

import config_logger
from db import db
from bp_api.views import bp_api
from bp_posts.views import bp_posts

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def create_and_config_app(config_path):
    app = Flask(__name__)

    app.register_blueprint(bp_posts)
    app.register_blueprint(bp_api, url_prefix="/api")

    app.config.from_pyfile(config_path)
    config_logger.config(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app


app = create_and_config_app("config.py")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
