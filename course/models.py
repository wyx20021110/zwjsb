from django.db import models

# Create your models here.

class Column(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title



class CoursePost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    order = models.IntegerField(blank=True,null=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    def __str__(self):
        return self.title