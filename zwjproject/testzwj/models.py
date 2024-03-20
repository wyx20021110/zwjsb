from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=100)  # 标题字段
    content = models.TextField()  # 内容字段
    publish_date = models.DateTimeField(auto_now_add=True)  # 发布日期字段，自动设置为当前时间
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者字段，外键指向用户模型

    def __str__(self):
        return self.title