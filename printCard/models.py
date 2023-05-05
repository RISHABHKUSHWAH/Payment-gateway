from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Id_card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    address = models.CharField(max_length=250)
    file = models.FileField(upload_to= 'IdCardFiles/')
    def __str__(self):
        return self.name
        
class Adhar_card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    address = models.CharField(max_length=250)
    password = models.CharField(max_length=20)
    file = models.FileField(upload_to= 'AdharCardFiles/')
    def __str__(self):
        return self.name

class Pan_card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    address = models.CharField(max_length=250)
    file = models.FileField(upload_to= 'PanCandFiles/')
    def __str__(self):
        return self.name                