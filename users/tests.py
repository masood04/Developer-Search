from django.test import TestCase
from django.core.mail import send_mail, outbox
from .signals import profile_create 
from .models import Profile

class EmailTest(TestCase):
    def test_email_sent(self):
        subject = 'Wellcome To dev Search'
        message_ = 'lorem'
        profile = Profile(username='masoodehghan')
        print(profile.id)
        
        send_mail(
            subject,
            message_,
            'masood@email.com',
            [profile.email],
            fail_silently=False,
            
                
        )
        
        print(outbox)
    