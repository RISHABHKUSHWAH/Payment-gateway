from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productName = models.CharField(max_length=500)
    purpose = models.CharField(default= None,max_length=500)
    amount = models.CharField(max_length=500)
    status = models.CharField(default=None, max_length=300)
    payment_request_id = models.CharField (max_length=500)
    created_at = models.CharField(default=None,max_length=500)
    modified_at = models.CharField(default=None,max_length=500)
    webhook_url = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.user.username

class Products(models.Model):
    productName = models.CharField(max_length=300)
    amount = models.IntegerField()
    deliveryCharge = models.IntegerField()
    def __str__(self):
        return self.productName