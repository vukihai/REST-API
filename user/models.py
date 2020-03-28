from django.db import models

class User(models.Model):
    id = models.IntegerField(default=0, primary_key= True)
    username = models.CharField(max_length=20)
    password = models.CharField(default=12345, max_length=10)
    name = models.CharField(default="", max_length = 100)
    access_token = models.CharField(default="abc",max_length=50)

class Intent(models.Model):
    intent_name = models.CharField(max_length = 100, primary_key = True)
    quantity = models.IntegerField(default=0)
    
    
