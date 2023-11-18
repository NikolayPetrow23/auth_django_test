from urllib.request import Request

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import SignUpUserSerializer, UserSerializer, EmailVerificationSerializer


class SignUpViewSet(viewsets.ModelViewSet):
    """
    Вьюсет регистрации пользователей.
    """
    queryset = User.objects.all()
    http_method_names = ('post',)
    serializer_class = SignUpUserSerializer


class UserViewSet(APIView):
    """
    Вьюсет для просмотра, удаления и изменения данных пользователя.
    Пользвователь может просматривать, изменять и удалять только свои данные.
    """
    http_method_names = ('get', 'patch', 'delete')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        user = self.request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        user_id = self.request.user.id
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response(self.serializer_class.data, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request) -> Response:
        user = self.request.user
        serializer = self.serializer_class(
            user,
            data=self.request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        try:
            serializer.update(user, self.request.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EmailVerificationAPIView(APIView):
    """
    Апивью для подвтверждения почты с OTP-кодом отправленным пользователю на почту.
    """
    http_method_names = ('post',)
    serializer_class = EmailVerificationSerializer

    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() and serializer.validate_code():
            return Response({"message": "Почта успешно подтверждена!"}, status=status.HTTP_200_OK)
        else:
            return Response({"Введите правильные данные!"}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Измененный вариант TokenObtainPairView для того, чтобы токен
    мог получить только пользователь у которого подтверждена почта.
    """
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        try:
            username = self.request.data.get('username')
            user = User.objects.get(username=username)
            serializer.is_valid(raise_exception=True)

        except TokenError as e:
            raise InvalidToken(e.args[0])

        except ObjectDoesNotExist:
            return Response({'detail': 'Укажите username!'}, status=status.HTTP_400_BAD_REQUEST)

        if user.is_verified_email:
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response({'detail': 'Сначала нужно подтвердить почту!'}, status=status.HTTP_400_BAD_REQUEST)
