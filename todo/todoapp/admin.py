from django.contrib import admin
from todoapp.models import Todo
# Register your models here.

#class TodoAdmin(admin.models)

admin.site.register(Todo)