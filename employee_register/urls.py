from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee-form'),
    path('<int:id>/', views.employee_form, name='employee-update'),

    path('list/', views.employee_list, name='employee-list'),
]