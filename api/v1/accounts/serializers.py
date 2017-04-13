from rest_framework import serializers

from api.v1.accounts.models import Account, Transaction
from api.v1.users.serializers import UserSerializer
from api.v1.bets.serializers import BetSerializer


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'name')


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    transaction = TransactionSerializer(read_only=True)
    bet = BetSerializer(read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'user', 'receiver', 'bet', 'transaction', 'description', 'history', 'value')

class AccountCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        obj = Account.objects.add_credit(**validated_data)
        return obj


    class Meta:
        model = Account
        fields = ('id','receiver', 'value')