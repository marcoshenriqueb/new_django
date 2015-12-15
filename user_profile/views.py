from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from user_profile.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrCreateOnly

class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrCreateOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

def confirm_registration(request, verified_token):
    pass
