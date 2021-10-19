from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('', views.api_over_view, name="api_over_view"),
    path('api/v1/register/', views.register, name="register"),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/list/product/', views.product_list, name="product_list"),

    path('api/v1/order/', views.order, name="order"),
    path('api/v1/payment/transaction/', views.payment_transaction, name="payment_transaction"),
]
