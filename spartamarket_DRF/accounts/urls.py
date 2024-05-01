from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import signup, profile_detail_view,ProfileViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('profiles/<str:username>/', profile_detail_view, name='profile_detail'),
]
