from django.contrib import admin
from .models import Todo

# Отображение времени создание в админ-панели.
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)