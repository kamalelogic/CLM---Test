from django.apps import AppConfig


class ToDoListConfig(AppConfig):
    """
    Configuration class for the 'to_do_list' app.

    This class defines the configuration for the 'to_do_list' app in the Django project.
    It specifies the default auto field and the name of the app.

    Attributes:
        default_auto_field (str): The name of the default auto field for model primary keys.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'to_do_list'
