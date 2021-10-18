# from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *


@api_view(['GET'])
def api_over_view(request):
    api_urls = {
        'login': '/api/v1/token/',
        'refresh': '/api/v1/token/refresh/',
        'register': '/api/v1/register/',

        'list procuct': '/api/v1/list/product/',
        # 'detail snippet': '/api/v1/detail/snippet/<id>/',
        # 'create snippet' : '/api/v1/create/snippet/',
        # 'delete snippet' : '/api/v1/delete/snippet/<id>/',
        # 'update snippet' : '/api/v1/update/snippet/<id>/',

        # 'list tag': '/api/v1/list/tag/',
        # 'detail tag': '/api/v1/detail/tag/<id>/',

        'list_users': '/api/v1/users/',
    }
    return  Response(api_urls, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        srzl = UserRegisterSerializer(data=request.data)
        
        if not srzl.is_valid():
            data = {'error': 'Something went wrong!'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        srzl.save()

        user = User.objects.get(username=srzl.data['username'])
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_201_CREATED)
