from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': 'your@email.com',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': '@username',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': '*********',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': '*********',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': '@username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': '*********',
    }))

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': '*********',
    }))
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': '*********',
    }))
    new_password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
        'class': 'border border-gray-300 rounded-lg w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-500',
        'placeholder': '*********',
    }))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
