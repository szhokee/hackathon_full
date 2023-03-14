from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)
    # duration = models.IntegerField()
    # image = models.ImageField(null=True, upload_to='category/')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    # description = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}'






