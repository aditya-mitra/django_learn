from django.urls import path

from profiles.views import ProfileListViewset

profile_list = ProfileListViewset.as_view({"get": "list"})
profile_detail = ProfileListViewset.as_view({"get": "retrieve"})

urlpatterns = [
    path("profiles/", profile_list, name="profile_list"),
    path("profiles/<int:pk>/", profile_detail, name="profile_detail"),
]
