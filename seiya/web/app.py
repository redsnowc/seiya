from flask import Flask
from seiya.web.config import configs
from seiya.web.blueprints import home_bp, job_bp, tenement_bp


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(job_bp)
    app.register_blueprint(tenement_bp)
