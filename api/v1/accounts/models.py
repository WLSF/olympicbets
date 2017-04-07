from django.db import models

from api.v1.users.models import User
from api.v1.bets.models import Bet

# Create your models here.

class Transaction(models.Model):
    '''
        Transaction type
    '''
    name = models.CharField(max_length=15)

class Account(models.Model):
    '''
        User account history:
            Every transaction which affects a User account is logged here
    '''

    user = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_user", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_receiver", on_delete=models.CASCADE)
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE, null=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    # Description means what was the operation
    description = models.CharField(max_length=30)
    # History means how the user defines it's operation to him
    history = models.CharField(max_length=30, null=True)
    # The Value which will be updated on user account
    value = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)