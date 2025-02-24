from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(Category)#ekta post a multiple category thakte pare abar ekta categorir multiple post thakte pare
    author=models.ForeignKey(User,on_delete=models.CASCADE)#ekjon authorer multiple post thakte pare
    img=models.ImageField(upload_to='posts/media/uploads/',blank=True,null=True)

    def __str__(self):
        return f'Name: {self.title}'

class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    body=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name