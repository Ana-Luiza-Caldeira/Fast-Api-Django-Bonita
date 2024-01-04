from django.contrib import admin
from . import models

admin.site.register(models.Flow)
admin.site.register(models.Notification)
admin.site.register(models.OriginConnection)
admin.site.register(models.DestinyConnection)
admin.site.register(models.Data)
admin.site.register(models.Field)
admin.site.register(models.Rule)