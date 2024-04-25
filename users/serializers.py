from rest_framework import serializers
from users.models import User, Payments


class UserSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор.'''
    class Meta:
        model = User
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор.'''
    class Meta:
        model = Payments
        fields = '__all__'
