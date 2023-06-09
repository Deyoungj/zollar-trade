from django.db.models.signals import post_save
from django.core.mail import EmailMessage
from .models import CustomUser, Profile
from django.dispatch import receiver
from django.conf import settings

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        message = f"A user just registered to zollar Trade \n \n"
        message += f"email: {instance.email} \n"
        message += f"username: {instance.username} \n"
        message += f"full name: {instance.full_name} \n"
        message += f"veiw user details in admin \n"
                    
                    
        emailmsg = EmailMessage('New Account Alert', message, to=[settings.ADMIN_EMAIL_CUSTOM])
        emailmsg.send()

        



@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
        
    instance.profile.save()
