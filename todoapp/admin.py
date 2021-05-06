from django.contrib import admin

# Register your models here.
from todoapp.models import TodoItem

admin.site.register(TodoItem)
