from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category

User = get_user_model()

class Event(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='events'
    )
    title = models.CharField(max_length=50)
    time = models.DateTimeField()
    amount = models.PositiveIntegerField(default=10)
    duration = models.IntegerField()
    geo = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='event/')
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
