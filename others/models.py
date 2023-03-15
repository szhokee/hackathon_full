from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()

class Bul(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()


class Cash_Register(models.Model):
    title =models.CharField(max_length=50, null=True, blac=True)
    description = models.TextField()
