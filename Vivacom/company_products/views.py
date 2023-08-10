from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views import View

from Vivacom.company_products.forms import CreateProductForm
from Vivacom.company_products.models import CreateProductModel


class CreateProductView(View):
    def get(self, request):
        form = CreateProductForm()
        return render(request, 'company_products/create_product.html', {'form': form})

    def post(self, request):
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'company_products/create_product.html', {'form': form})


class ProductsListView(ListView):
    model = CreateProductModel
    template_name = 'company_products/products_list.html'
    context_object_name = 'products'
