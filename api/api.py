from django.contrib.auth.models import User
from tastypie import constants, fields
from tastypie import authorization
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from api.models import Company, Department, Employee, Task


class CompanyResource(ModelResource):

    class Meta:
        queryset = Company.objects.all()
        resource_name = 'companies'
        authorization = Authorization()
        always_return_data = True
        filtering = {
            "name": constants.ALL_WITH_RELATIONS
        }


class DepartmentResource(ModelResource):
    company = fields.ForeignKey(CompanyResource, 'company')

    class Meta:
        queryset = Department.objects.all()
        resource_name = 'departments'
        authorization = Authorization()
        always_return_data = True
        filtering = {

        }

class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'users'
    always_return_data = True
    authorization = Authorization()

class EmployeeResource(ModelResource):
    department = fields.ForeignKey(DepartmentResource, 'department')
    user = fields.OneToOneField(UserResource, 'user')
    class Meta:
        queryset = Employee.objects.all()
        resource_name = 'employees'
        always_return_data = True
        authorization = Authorization()


class TaskResource(ModelResource):
    employee = fields.ForeignKey(EmployeeResource, 'employee')

    class Meta:
        queryset = Task.objects.all()
        resource_name = 'tasks'
        always_return_data = True
        authorization = Authorization()
