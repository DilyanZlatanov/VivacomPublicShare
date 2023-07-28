from django.urls import path

from Vivacom.common import views

urlpatterns = [
    path('', views.base_page, name='base')
]
