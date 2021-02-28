from django.contrib import admin
from infoapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno','marks','location']

admin.site.register(Student,StudentAdmin)
