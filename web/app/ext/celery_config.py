import os

from celery import Celery
from config import Config

celery = Celery(
    __name__,
    broker=Config.CELERY_BROKER_URL,
    result_backend=Config.CELERY_RESULT_BACKEND
)