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

    # Code to change the empty label text to SELECT
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['emp_code'].required = False
