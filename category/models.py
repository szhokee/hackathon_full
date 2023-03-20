from django.db import models

class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
 
    def __str__(self) -> str:
        return f'{self.title}'
