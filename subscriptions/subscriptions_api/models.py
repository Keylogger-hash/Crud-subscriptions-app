from django.db import models

# Create your models here.
class Subscriptions(models.Model):
    choices = (
    ('USD','USD'),
    ('EUR','EUR'),
    ('RUB','RUB'),
    )

    name = models.CharField(max_length=200)
    currency = models.CharField(max_length=255,choices=choices)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
