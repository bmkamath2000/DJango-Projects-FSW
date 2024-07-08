from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Student) 
# admin.site.register(Course)
admin.site.site_header='FDP ON Django' 
admin.site.site_title='FDP ON Django'

@admin.register(Student) 
class studentAdmin(admin.ModelAdmin): 
    list_display=['name']
    ordering=('name',) 
    search_fields=('name',) 

@admin.register(Course) 
class courseAdmin(admin.ModelAdmin): 
    list_display=['name']
    ordering=('name',) 
    search_fields=('name',) 
