from rest_framework import permissions, viewsets, mixins, generics, filters

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

    filter_backends = [filters.SearchFilter]
    search_fields = ["colour", "desc"]


class ProfileStatusViewset(viewsets.ModelViewSet):
    serializer_class = ProfileStatusSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnStatusOrReadOnly]

    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = ProfileStatus.objects.all().filter(
                user_profile__user__username=username
            )
        return queryset

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.profile)


class ProfileColourViewset(generics.UpdateAPIView):
    serializer_class = ProfileColourSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
