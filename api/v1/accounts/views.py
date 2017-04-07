from django.shortcuts import render

from rest_framework import viewsets

from api.v1.accounts.models import Account, Transaction
from api.v1.accounts.serializers import AccountSerializer, TransactionSerializer


# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
    '''
        Transaction ModelViewSet
    '''

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class AccountViewSet(viewsets.ModelViewSet):
    '''
        Account ModelViewSet
    '''

    queryset = Account.objects.all()
    serializer_class = AccountSerializer    