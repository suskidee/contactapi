from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=30, min_length=5)
    first_name = serializers.CharField(max_length=30, min_length=2)
    last_name = serializers.CharField(max_length=30, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'email already exists'})
        return super().validate(attrs)

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)
    username = serializers.CharField(max_length=50, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']
