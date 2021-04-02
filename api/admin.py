from api.models import Company, Department, Employee, Task
from django.contrib import admin

admin.site.register((Company, Employee, Department, Task))
