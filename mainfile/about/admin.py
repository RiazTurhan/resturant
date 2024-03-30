from django.contrib import admin
from about import models

class about_Admin(admin.ModelAdmin):
    list_display = ('about_des', 'experience', 'chefc')

class member_Admin(admin.ModelAdmin):
    list_display = ('image', 'name', 'work')

admin.site.register(models.about_data, about_Admin)
admin.site.register(models.members, member_Admin )
# Register your models here.
