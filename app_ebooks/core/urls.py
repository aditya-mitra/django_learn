from django.urls import path

from core.views import EBookListCreateAPIView

urlpatterns = [
    path("ebooks/", EBookListCreateAPIView.as_view(), name="ebook-list"),
]
