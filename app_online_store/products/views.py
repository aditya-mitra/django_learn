from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from products.models import Manufacturer, Product


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "list.html"


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = "detail.html"


class ProductListView(ListView):
    model = Product
    template_name = "list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"
