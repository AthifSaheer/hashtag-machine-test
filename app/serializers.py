from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

# THIS CLASSES WILL BE SERIALIZER THE MODELS
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    order = OrderSerializer()
    balance_amount = serializers.SerializerMethodField()
    
    def get_balance_amount(self, obj):
        if "balance_amount" in self.context:
            return self.context["balance_amount"]
        return None

    class Meta:
        model = Payment
        fields = '__all__'
