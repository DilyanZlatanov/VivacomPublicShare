from django.urls import path, include

from Vivacom.accounts.views import UserRegistrationView, UserLoginView, UserLogoutView, \
    ChangePasswordView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', include([
        path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    ])),
]
