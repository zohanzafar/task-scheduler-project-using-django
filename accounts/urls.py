from django.urls import path
from .views import custom_login_view, custom_logout_view, custom_register_view, custom_password_change_view

urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', custom_register_view, name='register'),
    path('change-password/', custom_password_change_view, name='change_password'),
]
