from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models as m
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Author(m.Model):
    first_name = m.CharField(max_length=128)
    last_name = m.CharField(max_length=128)
    dob = m.DateField()
    
    def __str__(self):
        return f'{self.first_name}, {self.dob}'
    
class Comment(m.Model):
    post = m.ForeignKey(Post, on_delete=m.CASCADE, null=False, related_name='comments')
    username = m.CharField(max_length=64)
    date = m.DateField()
    text = m.TextField(max_length=1000)

class CustomUserManager(BaseUserManager):
    def create_user(
            self,
            email,
            password,
            date_of_birth,
            **extra_fields
    ):
        if not email:
            raise ValueError(_('The e-mailaddress must be set.'))
        email = self.normalize_email(email)
        user = self.model(
            date_of_birth=date_of_birth,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(
            self,
            email,
            password,
            date_of_birth,
            **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                _("Superuser must have is_staff=True.")
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                _("Superuser must have is_superuser=True.")
            )
        return self.create_user(
            email, 
            password, 
            date_of_birth, 
            **extra_fields
        )

class CustomUser(AbstractUser):
    username = None
    email = m.EmailField(_('email address'), unique=True)
    date_of_birth = m.DateField(
        verbose_name='Verjaardag',
        null=True
    )
    function = m.CharField(max_length=64)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'date_of_birth'
    ]
    objects = CustomUserManager()
    def __str__(self):
        return self.email

class Post(m.Model):
    title = m.CharField(max_length=64)
    slug = m.SlugField(default='', blank=True, null=False, db_index=True)
    header_image = m.ImageField(upload_to='headers/', null=True)
    date = m.DateField()
    author = m.ForeignKey(Author, on_delete=m.SET_NULL, null=True)
    excerpt = m.TextField(max_length=200)
    content = RichTextUploadingField(max_length=20000)
    
    def __str__(self):
        return f'{self.title}, ({self.date})'
    
    def get_absolute_url(self):
        return reverse("post-page", args=[self.slug])
    
    '''
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    '''
        
