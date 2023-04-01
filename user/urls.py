from django.urls import path
from . import views


urlpatterns = [
    path('login-signup/', views.register_login, name="login-register"),
    path('referral-signup/<code>/', views.referral, name="referral_code"),
    path('logout/', views.logout_user, name="logout"),
    path('password-reset/', views.password_reset_request, name="password_reset"),
    path('password-reset/done/', views.password_reset_request_done, name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_request_confirm, name="password_reset_confirm"),

]