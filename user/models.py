from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True,default='avatars/default.png')
    bio = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.username