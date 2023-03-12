from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    contry = models.CharField(max_length=150)
    BTC_Wallet_Address = models.CharField(max_length=200)
    Ethereum_Bep20_Address = models.CharField(max_length=200)
    Tether_USDT_TRC20 = models.CharField(max_length=200)