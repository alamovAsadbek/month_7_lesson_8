from django.db import models

from app_users.models import UserModel
from common.models import BaseModel


class DebtView(BaseModel):
    DEBT_TYPE_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('lent', 'Lent'),
    ]
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    debt_type = models.CharField(max_length=10, choices=DEBT_TYPE_CHOICES)
