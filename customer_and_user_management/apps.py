from django.apps import AppConfig


class CustomerAndUserManagementConfig(AppConfig):
    """
    Configuration class for the 'customer_and_user_management' app.

    This class defines the configuration for the 'customer_and_user_management' app in the Django project.
    It specifies the default auto field and the name of the app.

    Attributes:
        default_auto_field (str): The name of the default auto field for model primary keys.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer_and_user_management'
