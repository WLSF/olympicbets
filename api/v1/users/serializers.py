from rest_framework import serializers
from api.v1.users.models import User

class UserSerializer(serializers.ModelSerializer):
    '''
        User serializer
    '''

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email')