from django.contrib import admin
from .models import Student,Studentclean

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city','datetime_data']

@admin.register(Studentclean)
class StudentclnAdmin(admin.ModelAdmin):
    list_display=['name','roll','city','datetime_data']