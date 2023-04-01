from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from user.models import CustomUser
from .models import Account, Transaction
from django.core.mail import  EmailMessage
from django.conf import settings



@receiver(post_save, sender=CustomUser)
def create_account(sender, instance, created, **kwargs):

    if created:
        acc = Account.objects.create(user=instance)
        acc.save()



@receiver(post_save, sender=Transaction)
def make_transaction(sender, instance, created, update_fields, **kwargs):

    if created:

        subject = "Investment Request initiated"

        message = f"""
        A User trigered investment request.

        username: {instance.user.username}
        email: {instance.user.email}
        plan: {instance.plan}
        amount: {instance.amount}
        refrence_id: {instance.refrence_id}
        status: {instance.status} 
            
        
        """
        mesg = EmailMessage(subject,message, to=[settings.ADMIN_EMAIL_CUSTOM])
        mesg.send()






