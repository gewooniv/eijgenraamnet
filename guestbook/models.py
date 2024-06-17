from django.db import models as m

# Create your models here.
class Comment(m.Model):
    comment = m.ForeignKey('self', on_delete=m.CASCADE, null=True, related_name='comments')
    username = m.CharField(max_length=64)
    date = m.DateField()
    text = m.TextField(max_length=1000)