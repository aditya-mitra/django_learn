from django.urls import path
from products.views import (
    # ProductListView,
    # ProductDetailView,
    product_list,
    product_detail,
    ManufacturerListView,
    ManufacturerDetailView,
)

urlpatterns = [
    path("products", product_list, name="product_list"),
    path("products/<int:pk>", product_detail, name="product_detail"),
    path("manus", ManufacturerListView.as_view(), name="manu_list"),
    path("manus/<int:pk>", ManufacturerDetailView.as_view(), name="manu_detail"),
]
