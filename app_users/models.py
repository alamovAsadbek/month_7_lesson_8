from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class UserModel(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
