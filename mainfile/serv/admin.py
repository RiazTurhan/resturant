from django.contrib import admin
from serv import models

class services_Admin(admin.ModelAdmin):
    list_display = ('service_icon', 'service_title', 'service_des')

admin.site.register(models.service_data, services_Admin)
# Register your models here.
