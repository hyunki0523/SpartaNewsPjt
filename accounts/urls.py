from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView )
from . import views

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("logout/", TokenBlacklistView.as_view()),
    path("signup/", views.signupAPIview().as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("profile/", views.ProfileAPIView.as_view()),
]