from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .custom_manager import CustomUserManager
from PIL import Image

class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    

    USERNAME_FIELD = "email"

    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return f"full name: {self.full_name} >>>>> Email: {self.email} "

    class Meta:
        ordering = ('-created_at',)



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pic")
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=150, blank=True)
    BTC_Wallet_Address = models.CharField(max_length=200, blank=True)
    Ethereum_Bep20_Address = models.CharField(max_length=200, blank=True)
    Tether_USDT_TRC20 = models.CharField(max_length=200, blank=True)    

    def __str__(self) -> str:
        return f"full name: {self.user.full_name} >>>>> Email: {self.user.email} "


    def save(self, ) -> None:
        super().save()

        img = Image.open(self.image.path)

        if img.height > 120 or img.width > 120:
            output_size = (120,120)
            img.thumbnail(output_size)
            img.save(self.image.path)

    







