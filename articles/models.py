from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)
    author = models.CharField(max_length=64)
    date = models.DateField()
    excerpt = models.TextField(max_length=200)
    content = models.TextField(max_length=20000)
    
    def __str__(self):
        return f'{self.title}, van {self.author} ({self.date})'
    
    def get_absolute_url(self):
        return reverse("post_page", args=[self.slug])
    
    '''
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    '''
        
    