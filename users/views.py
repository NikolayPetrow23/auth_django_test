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
    User registration viewset.
    """
    queryset = User.objects.all()
    http_method_names = ('post',)
    serializer_class = SignUpUserSerializer


class UserViewSet(APIView):
    """
    A viewset for viewing, deleting, and changing user data.
    The user can view, change and delete only their own data.
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
        return Response({'detail': 'The account was successfully deleted!'}, status=status.HTTP_204_NO_CONTENT)

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
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EmailVerificationAPIView(APIView):
    """
    An apiview for confirming mail with an OTP code sent to the user by mail.
    """
    http_method_names = ('post',)
    serializer_class = EmailVerificationSerializer

    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() and serializer.validate_code():
            return Response({'detail': 'Mail has been successfully confirmed!'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Enter the correct data!'}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Modified version of TokenObtainPairView in order for the token
    could only be received by a user whose mail is confirmed.
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
            return Response({'detail': 'Specify username!'}, status=status.HTTP_400_BAD_REQUEST)

        if user.is_verified_email:
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response({'detail': 'First you need to confirm your email!'}, status=status.HTTP_400_BAD_REQUEST)
