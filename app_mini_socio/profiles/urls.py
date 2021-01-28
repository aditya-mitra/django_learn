from django.urls import path, include
from rest_framework import routers

from profiles.views import ProfileListViewset

router = routers.DefaultRouter()
router.register("profiles", ProfileListViewset)

# profile_list = ProfileListViewset.as_view({"get": "list"})
# profile_detail = ProfileListViewset.as_view({"get": "retrieve"})

urlpatterns = [
    path("", include(router.urls))
    # path("profiles/", profile_list, name="profile_list"),
    # path("profiles/<int:pk>/", profile_detail, name="profile_detail"),
]
