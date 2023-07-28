from django import forms

from Vivacom.customer_feedback.models import CustomerFeedbackModel


class CustomerFeedbackForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedbackModel
        fields = ['title', 'description']
