from django.apps import AppConfig
from scripts import hexa

class TgbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tgbot'
    def ready(self):
        import os
        #from . import jobs

        # RUN_MAIN check to avoid running the code twice since manage.py runserver runs 'ready' twice on startup
        if os.environ.get('RUN_MAIN', None) != 'true':
            hexa.run()
            # Your function to run the bot goes here
