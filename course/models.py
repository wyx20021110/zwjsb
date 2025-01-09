from django.db import models

# Create your models here.

class Column(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title


