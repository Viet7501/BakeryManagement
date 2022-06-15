from django.apps import AppConfig


class MoneyManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'money_management'


class Name_change(AppConfig):
    name = 'money_management'
    verbose_name = 'Money management'
