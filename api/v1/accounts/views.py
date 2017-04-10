from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from api.v1.accounts.models import Account, Transaction
from api.v1.accounts.serializers import AccountSerializer, TransactionSerializer, AccountCreateSerializer


# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the Transactions-Types of the system.
    '''

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class AccountViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the Account-Transactions of the system.
    '''

    queryset = Account.objects.all()
    serializer_class = AccountSerializer    

    def create(self, request, *args, **kwargs):
        self.serializer_class = AccountCreateSerializer
        serializer = self.get_serializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)