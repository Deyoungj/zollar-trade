from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser
from .models import Account



@receiver(post_save, sender=CustomUser)
def create_account(sender, instance, created, **kwargs):

    if created:
        acc = Account.objects.create(user=instance)
        acc.save()
