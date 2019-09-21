from django.contrib import admin
from django import forms
from students.models import Student_Details


class Student_DetailsAdmin(admin.ModelAdmin):
    fieldsets=[
        ("Personal Details",{"fields":["FirstName","LastName","Username","image","City","State"]}),
        ("Academic Details",{"fields":["Department","Marks"]})
    ]


admin.site.register(Student_Details,Student_DetailsAdmin)
