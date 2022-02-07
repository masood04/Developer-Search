from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver 
from django.core.mail import send_mail
from django.conf import settings


# @receiver(post_save, sender=User)
def profile_create(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
        
        subject = 'Wellcome To dev Search'
        message_ = 'lorem'
        
        send_mail(
            subject,
            message_,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
            
        )
        
        
def delete_user(sender, instance, **kawrgs):
    user = instance.user
    user.delete()
    print('deleted!')
    
    
def update_user(sender, instance, created, **kwargs):    
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

post_save.connect(profile_create, sender=User)
post_delete.connect(delete_user, sender=Profile)
post_save.connect(update_user, sender=Profile)