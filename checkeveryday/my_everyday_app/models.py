from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Habbit(models.Model):
    hab_title = models.CharField(max_length=255, null=False)
    hab_method = models.CharField(max_length=10, null=False, default='ox')

class CheckHab(models.Model):
    check_title = models.ForeignKey(Habbit, on_delete=models.SET_DEFAULT, default='0')
    check_method = models.CharField(max_length=10, null=False, default='ox')
    check_date = models.DateField(max_length=100, default=timezone.now)
    check_hour = models.IntegerField()