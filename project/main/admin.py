from django.contrib import admin
from project.main import models

admin.site.register(models.Account)
admin.site.register(models.Payment)
# Register your models here.
