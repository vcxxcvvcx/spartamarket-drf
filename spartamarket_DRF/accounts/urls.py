from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'accounts', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
