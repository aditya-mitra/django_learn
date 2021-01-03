from django.http import JsonResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from products.models import Manufacturer, Product


def manufacturer_list(request, pk):
    try:
        manu = Manufacturer.objects.get(pk=pk)
        products = manu.products.all()
        data = {
            "name": manu.name,
            "location": manu.location,
            "products": list(products.values()),
        }
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({"ERROR": "MANU NOT found"})
    return response


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "list.html"


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = "detail.html"


def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        response = JsonResponse(
            {
                "products": {
                    "name": product.name,
                    "manu": product.manufacturer.name,
                    "addedAt": product.added_at,
                }
            }
        )

    except Product.DoesNotExist:
        response = JsonResponse(
            {
                "error": "could not find that product",
            },
            status=404,
        )
    return response


class ProductListView(ListView):
    model = Product
    template_name = "list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"
