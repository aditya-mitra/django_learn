from rest_framework import (
    generics,
    # mixins,
    permissions,
    exceptions,
)

from rest_framework.generics import get_object_or_404

from core.seraializers import EBookSerializer, ReviewSerializer
from core.models import EBooks, Reviews


class EBookListCreateAPIView(generics.ListCreateAPIView):
    """this class is same as the commented out class for EBookListCreateAPIView"""

    queryset = EBooks.objects.all().order_by(
        "id"
    )  # provide  - sign to reverse the ordering
    serializer_class = EBookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EBookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EBooks.objects.all()
    serializer_class = EBookSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(EBooks, pk=pk)

        review_author = self.request.user
        review = Reviews.objects.filter(ebook=ebook, reviewer=review_author)

        if review.exists():
            raise exceptions.ValidationError(
                "you can add another review for the same ebook"
            )

        serializer.save(
            ebook=ebook, reviewer=review_author
        )  # the `serializer.save()` method is directly related to the database, so the lhs has to be the field_name in the model and not in the seralizer


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


# class EBookListCreateAPIView(
#     mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView
# ):

#     queryset = EBooks.objects.all()
#     serializer_class = EBookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
