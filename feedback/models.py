from django.db import models
# from event.models import *
# from django.contrib.auth import get_user_model
# from django.core.validators import MinValueValidator, MaxValueValidator

# User = get_user_model()

# class Like(models.Model):
#     owner = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='likes'
#     )
#     event= models.ForeignKey(
#         Event,
#         on_delete=models.CASCADE,
#         related_name='likes'
#     )
#     is_like = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f'{self.owner} liked - {self.post.title}'

# class Favorite(models.Model):
#     event= models.ForeignKey(
#         Event,
#         on_delete=models.CASCADE,
#         related_name='favorites'
#     )

# class Rating(models.Model):
#     owner = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='ratings'
#     )
#     event = models.ForeignKey(
#         Event, 
#         on_delete=models.CASCADE,
#         related_name='retings'
#     )
#     rating = models.SmallIntegerField(
#         validators=[
#             MinValueValidator(1),
#             MaxValueValidator(5)
#         ],
#         blank=True, null=True
#     )

#     def __str__(self):
#         return f'{self.owner} --> {self.post.title}'