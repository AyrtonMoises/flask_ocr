import os


class ConfigBase(object):
    TESTING = False
    UPLOAD_FOLDER = './arquivos'
    CELERY_BROKER_URL = os.environ['BROKER_URI']
    CELERY_RESULT_BACKEND = os.environ['REDIS_BACKEND']

class Config(ConfigBase):
    SECRET_KEY = os.environ['SECRET_KEY']
    MONGO_URI = 'mongodb://' + os.environ['MONGO_USER'] + ':' + os.environ['MONGO_PASSWORD'] \
    + '@mongodb:27017/' + os.environ['MONGO_DATABASE'] + '?authSource=admin'

class ConfigTesting(ConfigBase):
    SECRET_KEY = "secret_testing"
    UPLOAD_FOLDER = './arquivos_test'
    TESTING = True
    MONGO_URI = 'mongodb://' + os.environ['MONGO_USER'] + ':' + os.environ['MONGO_PASSWORD'] \
    + '@mongodb:27017/' + 'flask_ocr_test' + '?authSource=admin'
