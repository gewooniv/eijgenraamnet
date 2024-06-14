from django.db import models as m

# Create your models here.

class Picture(m.Model):
    name = m.CharField(max_length=255)
    image = m.ImageField(upload_to='gallery/') 
    description = m.TextField()
    date = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.date}'
