from django.contrib import admin
from .models import Student


# Register your models here.

@admin.register(Student)
class adminStudent(admin.ModelAdmin):
    list_display = ['id','name', 'department', 'roll']
