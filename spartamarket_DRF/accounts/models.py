from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
