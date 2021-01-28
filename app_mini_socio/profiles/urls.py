from django.urls import path, include
from rest_framework import routers

from profiles.views import (
    ProfileListViewset,
    ProfileStatusViewset,
    ProfileColourViewset,
)

router = routers.DefaultRouter()
router.register("profiles", ProfileListViewset)
router.register("status", ProfileStatusViewset)


# profile_list = ProfileListViewset.as_view({"get": "list"})
# profile_detail = ProfileListViewset.as_view({"get": "retrieve"})

urlpatterns = [
    path("", include(router.urls)),
    path("colour/", ProfileColourViewset.as_view(), name="colour_update")
    # path("profiles/", profile_list, name="profile_list"),
    # path("profiles/<int:pk>/", profile_detail, name="profile_detail"),
]
