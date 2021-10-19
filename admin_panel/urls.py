from django.urls import path, include
from rest_framework import routers
from . import views
# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
