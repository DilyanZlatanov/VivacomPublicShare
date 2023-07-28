from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
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
