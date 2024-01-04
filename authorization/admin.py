from django.contrib import admin
from . import models

admin.site.register(models.Authorization)
admin.site.register(models.Role)
