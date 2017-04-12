from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.Model):
    '''
        This class will be responsible for recognize admins or common users
        Equivalent to rails-rolify 
    '''
    name = models.CharField(max_length=15)
    nick = models.CharField(max_length=15, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    '''
        This User extends from the Admin model User
    '''
    name = models.CharField(max_length=30)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    def has_role(self, name):
        return User.objects.get(id=self.pk).role.nick == name