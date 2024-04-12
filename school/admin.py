from django.contrib import admin
from .models import Student,Studentclean,properties,Agent,clean_Agent,clean_properties,Teacher

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city','datetime_data','created_at']

@admin.register(Studentclean)
class StudentclnAdmin(admin.ModelAdmin):
    list_display=['name','roll','city','datetime_data']


@admin.register(clean_properties)
class clean_prop_Admin(admin.ModelAdmin):
    list_display=['listing_id','listing_mls_id','name','acre']


@admin.register(clean_Agent)
class clean_agent_Admin(admin.ModelAdmin):
    list_display=['listing_id','agent_name']

admin.site.register(properties)
admin.site.register(Agent)
admin.site.register(Teacher)


