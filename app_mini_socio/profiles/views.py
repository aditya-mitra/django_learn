from rest_framework import permissions, viewsets, mixins, generics

from profiles.models import Profile, ProfileStatus
from profiles.serializers import (
    ProfileSerializer,
    ProfileStatusSerializer,
    ProfileColourSerializer,
)
from profiles.permissions import IsOwnProfileOrReadOnly, IsOwnStatusOrReadOnly


class ProfileListViewset(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnProfileOrReadOnly]


class ProfileStatusViewset(viewsets.ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnStatusOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.profile)


class ProfileColourViewset(generics.UpdateAPIView):
    serializer_class = ProfileColourSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
