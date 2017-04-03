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

class User(AbstractUser):
    '''
        This User extends from the Admin model User
    '''
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def get_role(self, name):
        '''
            Use this method to get the user Role,
            check if he is Admin or just a common piece of shit.
        '''
        return User.objects.get(id=self.pk).role.nick