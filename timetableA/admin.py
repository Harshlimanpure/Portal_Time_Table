from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Sem8)
class sem8Admin(admin.ModelAdmin):
    list_display=['id','Program','subject','subject_code','Faculty','time']
@admin.register(Sem7)
class sem7Admin(admin.ModelAdmin):
    list_display=['id','Program','subject','subject_code','Faculty','time']
@admin.register(Sem6)    
class sem6Admin(admin.ModelAdmin):
    list_display=['id','Program','subject','subject_code','Faculty','time']
@admin.register(Sem5)
class Sem5Admin(admin.ModelAdmin):
    list_display=['id','Program','subject','subject_code','Faculty','time']    
@admin.register(Sem4)
class sem4Admin(admin.ModelAdmin):
    list_display=['id','Program','subject','subject_code','Faculty','time']
@admin.register(Sem3)
class Sem3Admin(admin.ModelAdmin):
    list_display=['id','Program','subject','subject_code','Faculty','time']    
@admin.register(Sem2)
class sem2Admin(admin.ModelAdmin):
    list_display=['id','Program','subject','subject_code','Faculty','time']    
@admin.register(Sem1)
class Sem1Admin(admin.ModelAdmin):
    list_display=['id','Program','subject','subject_code','Faculty','time']    
