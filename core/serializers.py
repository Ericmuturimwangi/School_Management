from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'service_number', 'rank')

    def create (self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email= validated_data['email'],
            password = validated_data['password'],
            role = validated_data['role'],
            service_number = validated_data['service_number'],
            rank = validated_data['rank']
        )
        return user
    
    