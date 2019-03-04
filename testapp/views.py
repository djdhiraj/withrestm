from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin
import json


# Create your views here.


class EmployeeDetailCBV(SerializeMixin, View):
    def get(self, request, id, *arge, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The required resource not avaialble'})
        else:
            json_data = self.serialize('json', [emp, ])
            return HttpResponse(json_data, content_type='application/json')


class EmployeeListCBV(SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')
