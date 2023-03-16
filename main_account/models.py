from django.db import models
from user.models import CustomUser


class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_ballance = models.DecimalField(max_digits=8, decimal_places=2)
    total_profit = models.DecimalField(max_digits=8, decimal_places=2)
    active_deposit = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return self.user.full_name