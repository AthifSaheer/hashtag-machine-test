from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.api_over_view, name="api_over_view"),
    path('api/v1/register/', views.register, name="register"),

    # path('api/v1/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
