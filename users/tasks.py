from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from users.models import User, OTP
from users.utils import generate_otp_code


@shared_task
def send_email_verification(user_id: int):
    """
    The function of sending a message with an OTP code, using the Celery library.
    """
    user = User.objects.get(id=user_id)
    if OTP.objects.filter(user=user).exists():
        return user
    expiration = now() + timedelta(hours=24)
    otp_instance = OTP.objects.create(user=user, otp_code=generate_otp_code(), expiration=expiration)
    return otp_instance.send_verification_email()
