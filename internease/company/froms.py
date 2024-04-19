from company.models import Company
from django import forms 

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('created', 'updated', 'location', )