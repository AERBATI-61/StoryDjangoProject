from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class EmployeeList(ListView):
    model = Seller
    paginate_by = 10
    context_object_name = 'sellers'
    template_name = 'employee/employee.html'


class EmployeeDetail(DetailView):
    model = Seller
    context_object_name = 'seller'
    pk_url_kwarg = 'pk'
    template_name = 'employee/employee_detail.html'



