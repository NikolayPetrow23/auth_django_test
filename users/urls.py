from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from . import views

app_name = 'users'

router = routers.DefaultRouter()
router.register('signup', views.SignUpViewSet, basename='signup')

urlpatterns = [
    path('me/', views.UserViewSet.as_view()),
    path('email_verification/', views.EmailVerificationAPIView.as_view(), name='email_verification'),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]
