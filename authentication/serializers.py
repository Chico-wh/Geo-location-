from rest_framework import serializers
from django.contrib.auth.models import User
from transporte.models import Motorista


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterMotoristaSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=6)
    cpf = serializers.CharField(write_only=True)

    class Meta:
        model = Motorista
        fields = ['username', 'email', 'password', 'cpf']

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        cpf = validated_data.pop('cpf')

        user = User.objects.create_user(username=username, email=email, password=password)
        motorista = Motorista.objects.create(user=user, cpf=cpf)
        return motorista


class MotoristaProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Motorista
        fields = ['id', 'user', 'cpf', 'status', 'linha_atual']
