from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import PermissionsMixin

class Post(models.Model):
    
    title = models.CharField(max_length=150, help_text='The title of the blog')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this post."""
        return reverse('posts', args=[str(self.id)])

class UserManager(BaseUserManager):

    def create_user(self, username, email, first_name, last_name, password=None):
        
        if not email:
            raise ValueError('Must enter email.')

        user = self.model(email=self.normalize_email(email), 
                            first_name=first_name,
                            last_name=last_name,
                            )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None):
        user = self.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser):
    
    username = models.CharField(blank=True, null=True, max_length=20)
    email = models.EmailField(unique=True, max_length=40)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email + ': ' + self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this user."""
        return reverse('user', args=[str(self.id)])