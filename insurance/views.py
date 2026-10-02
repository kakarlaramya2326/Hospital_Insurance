from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

from .models import InsurancePlan, InsuranceApplication
from .forms import (
    InsuranceApplicationForm,
    ContactMessageForm,
    SignupForm
)

def home(request):
    return render(request, 'home.html')


def plans(request):
    plans = InsurancePlan.objects.all()

    return render(request, 'plans.html', {
        'plans': plans
    })
   


@login_required
def apply_insurance(request, plan_id):


    plan = get_object_or_404(InsurancePlan, id=plan_id)

    if request.method == 'POST':

        data = request.POST.copy()
        data['email'] = request.user.email

        form = InsuranceApplicationForm(data, user=request.user)

        if form.is_valid():

            application = form.save(commit=False)
            application.user = request.user
            application.plan = plan
            application.save()

            return redirect('application_success')

    else:
        
        form = InsuranceApplicationForm(user=request.user)

    return render(request, 'apply.html', {
        'form': form,
        'plan': plan
    })


def application_success(request):
    return render(request, 'success.html')
def contact(request):

    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact_success')

    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {
        'form': form
    })


def contact_success(request):
    return render(request, 'contact_success.html')

def about(request):
    return render(request, 'about.html')

@login_required
def profile(request):
    applications = InsuranceApplication.objects.filter(
        Q(user=request.user) | Q(email=request.user.email)
    ).distinct()

    return render(request, 'profile.html', {
        'applications': applications
    })

def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })
def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('profile')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {
        'form': form
    })
def logout_view(request):
    logout(request)
    return redirect('home')