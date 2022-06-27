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

        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code'
        }