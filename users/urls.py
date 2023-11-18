from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'users'

router = routers.DefaultRouter()
router.register('signup', views.SignUpViewSet, basename='signup')

urlpatterns = [
    path('me/', views.UserViewSet.as_view()),
    path('email_verification/', views.EmailVerificationAPIView.as_view(), name='email_verification'),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
]
