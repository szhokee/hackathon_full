from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
 
    def __str__(self) -> str:
        return f'{self.title}'


class Soup(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='soups'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='soups'
    )
    title = models.CharField(max_length=50)
    time = models.DateTimeField()
    duration = models.IntegerField()
    geo = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(null=True, upload_to='category/')
    image = models.ImageField(upload_to='soup/')
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
    



