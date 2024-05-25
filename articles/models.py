from django.db import models

# Create your models here.

class Post(models.Model):
    slug = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    date = models.DateField()
    excerpt = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    
    def __str__(self):
        return f'{self.title}, van {self.author} ({self.date})'