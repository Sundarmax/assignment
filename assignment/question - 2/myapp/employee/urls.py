from django.conf.urls import url
from django.urls import path
from employee.views import get_employee_data

urlpatterns = [
    path('list/employees/',get_employee_data,name="list-employees"),   
]