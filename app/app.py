from flask import Flask

from ext.database import mongo
from ext.celery_config import celery


def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    mongo.init_app(app)
    celery.conf.update(app.config)
    register_blueprints(app)
    return app

def register_blueprints(app):
    from views.ocr import ocr_bp
    app.register_blueprint(ocr_bp)