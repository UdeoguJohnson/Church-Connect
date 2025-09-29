from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import registerChurchForm, signUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import churchModel

# Create your views here.
def registerChurchView(request):
    
    if request.method == 'POST':
        form = registerChurchForm(request.POST)

        if form.is_valid():
            user = form.save(commit= False)
            login(request, user)
            return redirect('core:dashboard')
    else:
        form = registerChurchForm()
        
    return render(request, 'accounts/register_church.html',{form: 'form' })
        

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:dashboard')
    else:
        form = signUpForm()
    return render(request, 'accounts/signup.html')

@csrf_exempt
def signin(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/signin.html', {form: 'form' }) 


def signout(request):
    logout(request)
    return redirect('accounts:signin')

