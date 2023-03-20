from django.urls import path
from . import views

urlpatterns = [
    path('login-signup/', views.register_login, name="login-register"),

]