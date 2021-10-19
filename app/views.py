from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from .serializers import *
from .models import *

@api_view(['GET'])
def api_over_view(request):
    api_urls = {
        'Login': '/api/v1/token/',
        'Refresh': '/api/v1/token/refresh/',
        'Register': '/api/v1/register/',

        'List procuct': '/api/v1/list/product/',
        'Order': '/api/v1/order/',
        'Payment transaction': '/api/v1/payment/transaction/',

        'List users': '/api/v1/admin/users/',
        'Analytics': '/api/v1/admin/analytics/',
        'Ledger': '/api/v1/admin/ledger/',
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

@api_view(['GET'])
def product_list(request):
    try:
        prds = Product.objects.all()
        serializer = ProductSerializer(prds, context={'request': request}, many=True)
        return Response(serializer.data, status=200)
    except:
        data = {'error': 'Something went wrong!'}
        return Response(data, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'POST'])
def order(request):
    """
    Sample data for posting in this view.
    {
        "user" : "admin",
        "products" : [1, 2, 3]
    }
    """
    if request.method == 'GET':
        try:
            order = Order.objects.filter()
            serializer = OrderSerializer(order, many=True)
        except Order.DoesNotExist:
            message = 'An order does not exist in this ID({})!'.format(order)
            data = {'error': message}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        user = request.data['user']
        products = request.data['products']

        try:
            user_qry = User.objects.get(username=user)
        except User.DoesNotExist:
            message = 'An user does not exist in this name({})!'.format(user)
            data = {'error': message}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        try:
            total_amount = 0
            for prd in products:
                prd_qry = Product.objects.get(id=prd)
                total_amount += prd_qry.price
        except Product.DoesNotExist:
            message = 'An product does not exist in this ID({})!'.format(prd)
            data = {'error': message}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        ordr = Order()
        ordr.user = user_qry
        ordr.total_amount = total_amount
        ordr.save()
        ordr.product.set(products)

        data = {'Success': 'Success'}
        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def payment_transaction(request):
    """
    Sample data for posting in this view.
    {
        "user" : "admin",
        "order" : 5,
        "amount": 100
    }
    """
    if request.method == 'POST':
        user = request.data['user']
        order = request.data['order']
        amount = request.data['amount']

        try:
            user_qry = User.objects.get(username=user)
        except User.DoesNotExist:
            message = 'An user does not exist in this name({})!'.format(user)
            data = {'error': message}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        try:
            ordr = Order.objects.get(id=order)
        except Order.DoesNotExist:
            message = 'An order does not exist in this ID({})!'.format(order)
            data = {'error': message}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

      
            
        if ordr.total_amount < amount:
            data = {'error': 'You provided the amount longer than you have payable!'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        if Payment.objects.filter(order=order):
            payment = Payment.objects.get(order=order)

            if payment.balance_amount < amount:
                data = {'error': 'You provided the amount longer than you have payable!'}
                return Response(data, status=status.HTTP_403_FORBIDDEN)
            
            payment.paid_amount += amount
            payment.balance_amount -= amount
            payment.save()

        else:
            payment = Payment()
            payment.user = user_qry
            payment.order = ordr
            payment.total_amount = ordr.total_amount
            payment.paid_amount = amount
            payment.balance_amount = ordr.total_amount - amount
            payment.save()

        data = {'Success': 'Success'}
        return Response(data, status=status.HTTP_201_CREATED)

