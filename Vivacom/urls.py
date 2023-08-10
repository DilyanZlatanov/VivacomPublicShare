from django.contrib import admin
from django.urls import path, include

from Vivacom.views import custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Vivacom.common.urls')),
    path('accounts/', include('Vivacom.accounts.urls')),
    path('customer_feedback/', include('Vivacom.customer_feedback.urls')),
    path('company_products/', include('Vivacom.company_products.urls')),
]

handler404 = custom_404_view
