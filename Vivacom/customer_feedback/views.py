from django.shortcuts import render, redirect
from django.views.generic import View

from Vivacom.customer_feedback.forms import CustomerFeedbackForm


class CustomerFeedbackView(View):
    def get(self, request):
        form = CustomerFeedbackForm
        return render(request, 'customer_feedback/feedback.html', {'form': form})

    def post(self, request):
        form = CustomerFeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('base')
        else:
            return render(request, 'customer_feedback/feedback.html', {'form': form})
