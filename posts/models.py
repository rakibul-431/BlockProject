from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(Category)#ekta post a multiple category thakte pare abar ekta categorir multiple post thakte pare
    author=models.ForeignKey(Author,on_delete=models.CASCADE)#ekjon authorer multiple post thakte pare


    def __str__(self):
        return f'Name: {self.title}'