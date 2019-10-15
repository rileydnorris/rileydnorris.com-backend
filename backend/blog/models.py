from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class Post(models.Model):
    
    title = models.CharField(max_length=150, help_text='The title of the blog')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this post."""
        return reverse('posts', args=[str(self.id)])

class User(AbstractBaseUser):
    
    username = models.CharField(blank=True, null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this user."""
        return reverse('user', args=[str(self.id)])