from django.urls import path

from Vivacom.customer_feedback.views import CustomerFeedbackView

urlpatterns = [
    path('customerfeedback/', CustomerFeedbackView.as_view(), name='customer-feedback'),
]
