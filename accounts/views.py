from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomPasswordChangeForm, CustomLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomLoginForm

def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  

    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request, user)  
            return redirect('home')  
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def custom_logout_view(request):
    logout(request)
    return redirect('login')

def custom_register_view(request):
    if request.user.is_authenticated:
        return redirect('home')  

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def custom_password_change_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            user = form.save() 
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {'form': form})
