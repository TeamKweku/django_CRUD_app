from multiprocessing import context
from django.shortcuts import redirect, render

from .forms import EmployeeForm
from .models import Employee

# Create your views here.
# View function for listing all employee
def employee_list(request):
    employee_list = Employee.objects.all()
    context = {
        'employee_list': employee_list,
    }
    return render(request, 'employee_register/employee_list.html', context)


# Function for updating and inserting employees
def employee_form(request, id=0 ):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = form = EmployeeForm(instance=employee)

        context = {
            'form': form,
        }
        return render(request, 'employee_register/employee_form.html', context)
    else:
        # if ID is zero meaning its an insert operation 
        if id == 0:
            form = EmployeeForm(request.POST)

        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance = employee)
            if form.is_valid():
                form.save()
        
        return redirect('employee-list')


#Functino for deleting an employee
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee-list')