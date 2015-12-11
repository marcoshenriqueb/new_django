from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('picture',)
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer()

    def create(self, validated_data):
        u = User(
            first_name=validated_data['first_name'] if 'first_name' in validated_data else '',
            last_name=validated_data['last_name'] if 'first_name' in validated_data else '',
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False
        )
        u.save()
        if 'profile' in validated_data:
            if 'picture' in validated_data['profile']:
                p = UserProfile(
                    picture=validated_data['profile']['picture'],
                    user=u
                )
                p.save()

        return u

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'is_superuser',
            'last_login',
            'is_active',
            'date_joined'
        )
        depth = 1