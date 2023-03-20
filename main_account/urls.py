from django.urls import path 
from . import views


urlpatterns = [
    path('dashboard/',views.dashboard, name="dashboard" ),
    path('profile/', views.profile, name="profile"),
    path('change-password/', views.change_password, name="changepassword"),
    path('support/', views.support, name="support"),
    path('invest/', views.invest, name="invest"),
    path('terms/', views.terms, name="terms"),
]