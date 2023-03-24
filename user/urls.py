from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login-signup/', views.register_login, name="login-register"),
    path('logout/', views.logout_user, name="logout"),

]