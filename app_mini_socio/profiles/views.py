from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import mixins

from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from profiles.permissions import IsOwnProfileOrReadOnly


class ProfileListViewset(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnProfileOrReadOnly]
