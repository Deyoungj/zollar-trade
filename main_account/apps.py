from django.apps import AppConfig


class MainAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_account'

    def ready(self):
        import main_account.signals
