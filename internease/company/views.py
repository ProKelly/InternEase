from django.shortcuts import render,redirect
from company.models import Company
from company.forms import CompanyRegistrationForm
from django.contrib import messages

def company_register(request):
    form = CompanyRegistrationForm()
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            registered_company = form.save(commit=False)
            registered_company.name = registered_company.name.lower()
            registered_company.save()
            return redirect('base:home')
        else:
            messages.error(request, "failed to register, the credetials you provided might contain invalid input")
    context = {'form':form}
    return render(request, 'company/register.html', context)