from tastypie import constants
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from api.models import Company

class CompanyResource(ModelResource):

  class Meta:
    queryset = Company.objects.all()
    resource_name = 'companies'
    authorization = Authorization()
    always_return_data = True
    filtering = {
      "name": constants.ALL_WITH_RELATIONS
    }
