from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .custom_manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = "email"

    objeet = CustomUserManager
    
    def __str__(self) -> str:
        return self.full_name

    class Meta:
        ordering = ('-created_at',)



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg")
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=150, blank=True)
    contry = models.CharField(max_length=150, blank=True)
    BTC_Wallet_Address = models.CharField(max_length=200, blank=True)
    Ethereum_Bep20_Address = models.CharField(max_length=200, blank=True)
    Tether_USDT_TRC20 = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.user





