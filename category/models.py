from django.db import models

class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)

 
    def __str__(self) -> str:
        return f'{self.title}'
