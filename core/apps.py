# Import the global class AppConfig
from django.apps import AppConfig

# Add the properties for our application is its name and path
class CoreConfig(AppConfig):
    name = 'core'
    path = './core'