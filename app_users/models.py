from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
