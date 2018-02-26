from django.contrib.auth.models import User
from django.db import models
from djmoney.models.fields import MoneyField


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inn = models.CharField(max_length=5)
    balance = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency='USD')

    def __str__(self):
        return self.inn