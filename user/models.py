from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(default=12345, max_length=10)
