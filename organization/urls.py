from django.urls import path

from .views import *

urlpatterns = [
    path('employee', EmployeeList.as_view(), name='employee_list'),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
]