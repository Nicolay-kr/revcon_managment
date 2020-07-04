from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'publish',  'service', 'first_name',
                    'last_name', 'email', 'mob_number', 'message',
                    )
    list_filter = ('status', 'publish',  'service')
    search_fields = ('first_name','last_name')
    # prepopulated_fields = {'slugproduct': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)
