import uuid
from django.db import models
from django.contrib.auth import get_user_model
from event.models import Event

User = get_user_model()

class Ticket(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    amount = models.PositiveIntegerField(default=1)
    confirm = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    activation_code = models.UUIDField(default=uuid.uuid4)

    def save(self, *args, **kwargs):
        self.total_price = self.amount * self.event.price
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'билет на {self.event.title}'
