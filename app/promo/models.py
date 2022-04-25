from __future__ import unicode_literals
from django.db import models


class PromoCreate(models.Model):
    amount = models.IntegerField()
    group = models.CharField(max_length=100)


class PromoCheck(models.Model):
    promo_code = models.CharField(max_length=100)
