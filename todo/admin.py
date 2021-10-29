from django.contrib import admin
from .models import Breakfast, Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(Todo, TodoAdmin)
admin.site.register(Breakfast, TodoAdmin)
