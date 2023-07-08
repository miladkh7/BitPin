from django.contrib import admin

# Local
from .models import User, Profile

admin.site.register(User)
admin.site.register(Profile)