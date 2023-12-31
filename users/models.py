from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    """
    Custom user model.
    """
    email = models.EmailField(unique=True)
    is_verified_email = models.BooleanField(default=False)


class OTP(models.Model):
    """
    A one-to-one relationship model of the OTP code and the user model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_time = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        subject = f'Account confirmation for {self.user.username}!'
        message = f'To confirm your account {self.user.username} enter the code: {self.otp_code}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False
