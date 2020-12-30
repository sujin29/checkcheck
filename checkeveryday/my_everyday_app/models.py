from django.db import models

# Create your models here.
class Habbit(models.Model):
    hab_title = models.CharField(max_length=255)