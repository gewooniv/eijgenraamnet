from django.db import models as m
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(m.Model):
    title = m.CharField(max_length=64)
    slug = m.SlugField(default='', blank=True, null=False, db_index=True)
    date = m.DateField()
    excerpt = m.TextField(max_length=200)
    content = m.TextField(max_length=20000)
    
    def __str__(self):
        return f'{self.title}, ({self.date})'
    
    def get_absolute_url(self):
        return reverse("post_page", args=[self.slug])
    
    '''
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    '''
        
    