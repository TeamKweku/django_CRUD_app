from django.forms import ModelForm
from .models import Employee



class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = (
            'fullname',
            'emp_code',
            'mobile',
            'position',
        )