from django.contrib import admin
from .models import User, Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'completed', 'date_created', 'user')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')

admin.site.register(Todo, TodoAdmin)
admin.site.register(User, UserAdmin)
