from django.contrib import admin
from .models import *


class ModelAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'description', 'state', 'status', 'created_at')
    list_filter = ('state', 'status', 'created_at', 'saved_by')
    search_fields = ('libelle', 'description', 'state', 'status', 'created_at')
    prepopulated_fields = {'slug': ('libelle',)}
    
    
    
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'description', 'state', 'status', 'created_at')
    list_filter = ('state', 'status', 'created_at', 'saved_by')
    search_fields = ('libelle', 'description', 'state', 'status', 'created_at')
    prepopulated_fields = {'slug': ('libelle',)}
    
admin.site.register(Model, ModelAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Deploiement)

# Register your models here.
