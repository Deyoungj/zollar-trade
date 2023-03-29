from django.urls import path 
from . import views


urlpatterns = [
    path('dashboard/',views.dashboard, name="dashboard" ),
    path('redeem/',views.redeem, name="redeem" ),
    path('profile/', views.profile, name="profile"),
    path('change-password/', views.change_password, name="changepassword"),
    path('invest-check/<str:ref>/<str:amount>/', views.invest_approved, name="invest-check"),
    path('invest/', views.invest, name="invest"),
    path('transaction_history/', views.transactions, name="transaction"),
    path('referral/', views.referral, name="referral"),
    path('withdraw/', views.withdraw, name="withdraw"),
    path('contact/', views.contact, name="contact"),
    path('contact/done/', views.contact_done, name="contact_done"),
    path('terms/', views.terms, name="terms"),
]