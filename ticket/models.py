from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

class Ticket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tickets')
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='tickets/')

    def __str__(self):
        return f'{self.title}'