from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

from profiles.models import Profile, ProfileStatus
from profiles.serializers import ProfileSerializer


class ProfileListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
