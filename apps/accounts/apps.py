from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # def ready(self):
    #  from . models import save_user_profile

    def ready(self):
        # from . import signals
        import accounts.signals
