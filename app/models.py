from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    images = models.ImageField(upload_to='prd_imgs')
    # quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ManyToManyField(Product, blank=True)
    total_amount = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "ID: " + str(self.id) + " | User: " + str(self.user)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    total_amount = models.IntegerField(default=0)
    paid_amount = models.IntegerField(default=0)
    balance_amount = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "ID: " + str(self.id) + " | User: " + str(self.user)