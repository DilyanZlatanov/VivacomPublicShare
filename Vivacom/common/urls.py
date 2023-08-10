from django.urls import path

from Vivacom.common import views

urlpatterns = [
    path('', views.BasePageView.as_view(), name='base')
]
