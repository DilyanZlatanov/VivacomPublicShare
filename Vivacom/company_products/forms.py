from django import forms

from Vivacom.company_products.models import CreateProductModel


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = CreateProductModel
        fields = ['product_name', 'description']
