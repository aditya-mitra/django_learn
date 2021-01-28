from rest_framework import generics
from rest_framework import permissions

from profiles.models import Profile, ProfileStatus
from profiles.serializers import ProfileSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]