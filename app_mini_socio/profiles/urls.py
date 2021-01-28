from django.urls import path
from profiles.views import ProfileListView

urlpatterns = [path("profiles/", ProfileListView.as_view(), name="profile_list")]
