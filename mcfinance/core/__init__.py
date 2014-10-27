from django.apps import AppConfig
from django.conf import settings
from mongoengine import connect


class CoreConfig(AppConfig):

    label = 'mcfinance_core'
    verbose_name = 'MC Finance Core'
    name = 'mcfinance.core'
    models_module = 'mcfinance.core.documents'

    def ready(self):
        db = settings.MONGODB_DB
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        connect(db, host=host, port=port)
