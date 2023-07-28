from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Vivacom.common.urls')),
    path('accounts/', include('Vivacom.accounts.urls')),
    path('customer_feedback/', include('Vivacom.customer_feedback.urls')),
]
