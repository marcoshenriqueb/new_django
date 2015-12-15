from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.response import Response
from project_mailer.mailer import MailgunMailer
import string
import random

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('picture',)
        depth = 1

class UserSerializer(serializers.ModelSerializer):

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


    def create(self, validated_data):
        u = User(
            first_name=validated_data['first_name'] if 'first_name' in validated_data else '',
            last_name=validated_data['last_name'] if 'first_name' in validated_data else '',
            username=validated_data['username'],
            email=validated_data['email'],
            is_active=False
        )
        u.set_password(validated_data['password'])
        u.save()
        random_str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(40))
        if 'profile' in validated_data:
            if 'picture' in validated_data['profile']:
                p = UserProfile(
                    picture=validated_data['profile']['picture'],
                    verified_token=random_str,
                    user=u
                )
                p.save()
        else:
            p = UserProfile(
                verified_token=random_str,
                user=u
            )
            p.save()

        m = MailgunMailer()
        m.sendRegisterConfirmation([u.email,], p.verified_token)

        return u
