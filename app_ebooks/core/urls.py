from django.urls import path

from core.views import (
    EBookListCreateAPIView,
    EBookDetailAPIView,
    ReviewCreateAPIView,
    ReviewDetailView,
)

urlpatterns = [
    path("ebooks/", EBookListCreateAPIView.as_view(), name="ebook-list"),
    path("ebooks/<int:pk>", EBookDetailAPIView.as_view(), name="ebook-detail"),
    path(
        "ebooks/<int:ebook_pk>/review/",
        ReviewCreateAPIView.as_view(),
        name="review-create",
    ),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
]
