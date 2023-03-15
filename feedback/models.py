from django.db import models
from feedback.models import others 
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Like(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    others = models.ForeignKey(
        others,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    is_like = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.owner} liked - {self.post.title}'

class Favorite(models.Model):
    post = models.ForeignKey(
        others,
        on_delete=models.CASCADE,
        related_name='favorites'
    )

class Rating(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    others = models.ForeignKey(
        others, 
        on_delete=models.CASCADE,
        related_name='retings'
    )
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.owner} --> {self.post.title}'