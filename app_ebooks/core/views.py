from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404

from core.seraializers import EBookSerializer, ReviewSerializer
from core.models import EBooks, Reviews


class EBookListCreateAPIView(generics.ListCreateAPIView):
    """this class is same as the commented out class for EBookListCreateAPIView"""

    queryset = EBooks.objects.all().order_by(
        "id"
    )  # provide  - sign to reverse the ordering
    serializer_class = EBookSerializer


class EBookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EBooks.objects.all()
    serializer_class = EBookSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(EBooks, pk=pk)

        review_author = self.request.user
        serializer.save(ebook=ebook, review_author=review_author)


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
