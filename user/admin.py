from django.contrib import admin
from .models import CustomUser, Profile, Account

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Account)
