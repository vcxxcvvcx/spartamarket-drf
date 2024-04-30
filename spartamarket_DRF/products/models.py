from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = (
        ("F", "Fruit"),
        ("V", "Vegetable"),
        ("M", "Meat"),
        ("O", "Other"),
    )

    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default="O")  # 기본값 'Other'

    def __str__(self):
        return self.name
