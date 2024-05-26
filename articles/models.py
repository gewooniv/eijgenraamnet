from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    slug = models.SlugField(default='', null=False, db_index=True)
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    date = models.DateField()
    excerpt = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    
    def __str__(self):
        return f'{self.title}, van {self.author} ({self.date})'
    
    def get_absolute_url(self):
        return reverse("post_page", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super.save(*args, **kwargs)
        
    