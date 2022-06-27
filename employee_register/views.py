from multiprocessing import context
from django.shortcuts import render

from .forms import EmployeeForm

# Create your views here.
# View function for listing all employee
def employee_list(request):
    context = {}
    return render(request, 'employee_register/employee_list.html', context)


# Function for updating and inserting employees
def employee_form(request):
    form = EmployeeForm()

    context = {
        'form': form,
    }
    return render(request, 'employee_register/employee_form.html', context)


#Functino for deleting an employee
def employee_delete(request):
    pass
