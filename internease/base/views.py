from django.shortcuts import redirect, render
from base.forms import InternApplicationForm, InternRegistrationForm
from django.contrib import messages
from base.models import InternApplication
from django.contrib.auth.decorators import login_required


def applied_interns(request):
    interns = InternApplication.objects.filter()
    context = {'interns': interns}
    return render(request, 'base/applied_interns.html', context)

def success_page(request):
    context = {}
    return render(request, 'base/success.html', context)
def apply(request):
    form = InternApplicationForm()
    if request.method == 'POST':
        form = InternApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base:success')
    context = {'form':form}
    return render(request, 'base/apply.html', context)


def register_intern(request):
    form = InternRegistrationForm()
    if request.method == 'POST':
        form = InternRegistrationForm(request.POST)
        if form.is_valid():
            registered_intern = form.save(commit=False)
            if registered_intern.has_paid:
                register_intern.save()
                return redirect('base:success')
        else:
            messages.error(request, 'Registration Failed, maybe your credentails were not valid')
    context = {'form':form}
    return render(request, 'base/register.html', context)