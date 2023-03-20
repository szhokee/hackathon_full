
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()

