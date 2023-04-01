from django.db import models
from user.models import CustomUser
import random
import string

class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_profit = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    active_deposit = models.DecimalField(max_digits=8, decimal_places=2, default=0)


    def __str__(self):
        return self.user.full_name
    

status = [
    ("Pending", "Pending"),
    ("Approved", "Approved"),
]

def refrence_id():
   ref = ''.join([random.choice(string.ascii_uppercase + string.digits) for i in range(26)])
   return ref

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(choices=status ,max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    transaction = models.CharField(max_length=100)
    invest_from = models.CharField(max_length=100, default="Wallet Address")
    plan = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    refrence_id = models.CharField(max_length=100, default=refrence_id)

    def __str__(self):
        return self.user.email


