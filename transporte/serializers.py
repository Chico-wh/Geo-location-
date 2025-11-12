from rest_framework import serializers
from .models import Linha, Ponto, Motorista, Localizacao
from django.contrib.auth.models import User

class LinhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linha
        fields = '__all__'

class PontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponto
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MotoristaSerializer(serializers.ModelSerializer):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('suspenso', 'Suspenso'),
    ]
    status = serializers.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Motorista
        fields = '__all__'

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'
