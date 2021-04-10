"""taskapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from api.api import CompanyResource, DepartmentResource, EmployeeResource, TaskResource
from django.contrib import admin
from django.urls import path
from tastypie.api import Api

v1 = Api(api_name='v1')

resources = (CompanyResource(), TaskResource(), EmployeeResource(), DepartmentResource(), )

for resource in resources:
    v1.register(resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1.urls))
]
