from django.forms.models import model_to_dict
from base.models import InternApplication, InternRegistration
from django import forms

class InternApplicationForm(forms.ModelForm):
    class Meta:
        model = InternApplication
        exclude = ['created']
        
class InternRegistrationForm(forms.ModelForm):
    class Meta:
        model = InternRegistration
        exclude = ['has_paid', 'created', 'account', '']