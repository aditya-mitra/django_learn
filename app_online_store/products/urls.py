from django.urls import path
from products.views import (
    ProductListView,
    ProductDetailView,
    ManufacturerListView,
    ManufacturerDetailView,
)

urlpatterns = [
    path("products", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("manus", ManufacturerDetailView.as_view(), name="manu_list"),
    path("manu/<int:pk>", ManufacturerDetailView.as_view(), name="manu_detail"),
]
