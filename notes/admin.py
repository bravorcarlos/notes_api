from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Note

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated_at']

admin.site.register(Note, PostAdmin)