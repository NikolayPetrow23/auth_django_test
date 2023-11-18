from smtplib import SMTPException

from django.db import transaction
from rest_framework import serializers

from users.models import User, OTP
from users.tasks import send_email_verification


class SignUpUserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер регистрации пользователей.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'password')

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(
                **validated_data
            )
            send_email_verification.delay(user.id)
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для работы с пользователями.
    """
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name')


class EmailVerificationSerializer(serializers.Serializer):
    """
    Сериалайзер проверки OTP-кода.
    """
    username = serializers.CharField()
    otp_code = serializers.CharField()

    def validate_code(self):
        username = self.validated_data.get('username')
        otp_code = self.validated_data.get('otp_code')
        user = User.objects.get(username=username)
        email_verifications = OTP.objects.filter(user=user, otp_code=otp_code)
        if email_verifications and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return True
        return False
