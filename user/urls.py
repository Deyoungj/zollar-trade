from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login-signup/', views.register_login, name="login-register"),
    path('logout/', views.logout_user, name="logout"),
    # path('password-reset/', auth_view.PasswordResetView.as_view(template_name='user/password_reset.html'), name="password_reset"),
    path('password-reset/', views.password_reset_request, name="password_reset"),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name="password_reset_confirm"),

]