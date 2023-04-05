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
        
        if instance.transaction =='Investment' :
            subject = "Investment Request initiated"

            message = f"A User triggered investment request. \n \n"
            message += f"Username: {instance.user.username} \n"
            message += f"Email: {instance.user.email} \n"
            message += f"Plan: {instance.plan} \n"
            message += f"Amount: {instance.amount} \n"
            message += f"Refrence_id: {instance.refrence_id} \n"
            message += f"Status: {instance.status} "

            
            mesg = EmailMessage(subject,message, to=[settings.ADMIN_EMAIL_CUSTOM])
            mesg.send()


        if instance.transaction =='Withdrawal' :
            subject = "Withdrawal Request initiated"

            message = f"A User triggered investment request. \n \n"
            message += f"Username: {instance.user.username} \n"
            message += f"Email: {instance.user.email} \n"
            message += f"Plan: {instance.plan} \n"
            message += f"Amount: {instance.amount} \n"
            message += f"Refrence_id: {instance.refrence_id} \n"
            message += f"Status: {instance.status} "

            
            mesg = EmailMessage(subject,message, to=[settings.ADMIN_EMAIL_CUSTOM])
            mesg.send()






