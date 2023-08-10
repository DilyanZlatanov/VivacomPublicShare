from django.urls import path

from Vivacom.company_products.views import CreateProductView, ProductsListView

urlpatterns = [
    path('create_product/', CreateProductView.as_view(), name='create-product'),
    path('products_list/', ProductsListView.as_view(), name='products-list'),
]
