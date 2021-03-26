from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    # how signals are used in the project
    def ready(self):
        import accounts.signals
