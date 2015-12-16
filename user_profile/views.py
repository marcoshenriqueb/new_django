from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from user_profile.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrCreateOnly
from django.core.urlresolvers import reverse


class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrCreateOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


def ConfirmRegistration(request, verified_token):
    try:
        user = User.objects.get(profile__verified_token=verified_token)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        user.is_active = True
        user.save()
        profile = user.profile
        profile.verified_token = None
        profile.save()

        return redirect(reverse('sitefront:index'))
