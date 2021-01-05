from rest_framework import generics, mixins

from core.seraializers import EBookSerializer
from core.models import EBooks


class EBookListCreateAPIView(
    mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView
):

    queryset = EBooks.objects.all()
    serializer_class = EBookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
