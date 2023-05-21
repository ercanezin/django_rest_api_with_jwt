from django.urls import path
from authentication.views import RegisterView, LoginAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", LoginAPIView.as_view(), name="auth-login"),
    path('register/', RegisterView.as_view(), name='auth-register'),
]
