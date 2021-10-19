from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import status
from app.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def analytics(request):
    if request.method == 'GET':
        total_amount = 0
        paid_amount = 0

        orders = Order.objects.all()
        payments = Payment.objects.all()

        for ordr in orders:
            total_amount += ordr.total_amount
            
        for payment in payments:
            paid_amount += payment.paid_amount
        
        data = {
            "Number of orders" : orders.count(),
            "Total amount" : total_amount,
            "Paid amount" : paid_amount,
            "Pending amount" : total_amount - paid_amount,
        }
        return  Response(data, status=status.HTTP_201_CREATED)
    

@api_view(['GET'])
def ledger(request):
    data = []
    payments = Payment.objects.all()
    for payment in payments:
        balance_amount = payment.total_amount - payment.paid_amount
        srz = PaymentSerializer(payment, context={'request': request, 'balance_amount': balance_amount}, many=False)
        data.append(srz.data)

    return  Response(data, status=status.HTTP_201_CREATED)

