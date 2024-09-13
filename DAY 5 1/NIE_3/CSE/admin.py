from django.contrib import admin

# Register your models here.
from CSE.models  import Student 
from CSE.models  import employee

admin.site.register(Student)
admin.site.register(employee)