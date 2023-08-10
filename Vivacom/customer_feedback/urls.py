from django.urls import path

from Vivacom.customer_feedback.views import CustomerFeedbackView

urlpatterns = [
    path('customer_feedback/', CustomerFeedbackView.as_view(), name='customer-feedback'),
]
