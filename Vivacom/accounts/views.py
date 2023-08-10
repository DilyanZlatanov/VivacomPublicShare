from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from Vivacom.accounts.forms import UserRegistrationForm, UserLoginForm


class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm
        return render(request, 'accounts/registration.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/registration.html', {'form': form})


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'


class UserLogoutView(LogoutView):
    pass


class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('base')
