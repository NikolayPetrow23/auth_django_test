from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    """
    email = models.EmailField(unique=True)
    is_verified_email = models.BooleanField(default=False)


class OTP(models.Model):
    """
    Модель отношения один-ко-дному OTP-кода и модели пользователей.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_time = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        subject = f'Подтверждение учетной записи для {self.user.username}!'
        message = f'Для подтверждения учетной записи {self.user.username} введите код: {self.otp_code}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False
