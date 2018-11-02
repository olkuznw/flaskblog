from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# nice time
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    # to do init app

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    return app