from django.apps import AppConfig


class LablesConfig(AppConfig):
    """
    Configuration class for the 'lables' app.

    This class defines the configuration for the 'lables' app in the Django project.
    It specifies the default auto field and the name of the app.

    Attributes:
        default_auto_field (str): The name of the default auto field for model primary keys.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lables'
